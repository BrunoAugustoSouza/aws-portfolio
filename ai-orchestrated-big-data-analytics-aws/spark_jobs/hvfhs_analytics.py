from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    hour,
    sum as _sum,
    avg,
    count,
    when,
    round
)
from pyspark.sql.functions import col, broadcast
import sys

spark = SparkSession.builder.appName("HVFHS Analytics Mart").getOrCreate()

spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")

BUCKET_NAME= sys.argv[1]

input_path = f"s3://{BUCKET_NAME}/bronze/hvfhs/"
output_path = f"s3://{BUCKET_NAME}/silver/"
aux_path = f"s3://{BUCKET_NAME}/bronze/aux/taxi_zone_lookup.csv"

df = (
    spark.read.parquet(input_path)
    .select(
        "pickup_datetime",
        "trip_time",
        "trip_miles",
        "base_passenger_fare",
        "tolls",
        "sales_tax",
        "congestion_surcharge",
        "airport_fee",
        "shared_match_flag",
        "cbd_congestion_fee",
        "hvfhs_license_num",
        "driver_pay",
        "PULocationID",
        "DOLocationID"
    )
)

zone_lookup = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(aux_path)
)

# ------------------------------------------------------------------------------
# Feature Engineering
# ------------------------------------------------------------------------------


df_enriched = (
    df
    .filter(col("pickup_datetime").isNotNull())
    .withColumn("pickup_hour", hour(col("pickup_datetime")))
    .withColumn("trip_minutes", col("trip_time") / 60)
    .withColumn(
        "total_passenger_payment",
        col("base_passenger_fare")
        + col("tolls")
        + col("sales_tax")
        + col("congestion_surcharge")
        + col("airport_fee")
    )
    .withColumn(
        "revenue_per_mile",
        when(col("trip_miles") > 0,
             col("total_passenger_payment") / col("trip_miles"))
        .otherwise(None)
    )
    .withColumn(
        "is_shared",
        when(col("shared_match_flag") == "Y", 1).otherwise(0)
    )
    .withColumn(
        "is_congestion_trip",
        when(col("cbd_congestion_fee") > 0, 1).otherwise(0)
    )
)



zone_lookup = zone_lookup.select(
    col("LocationID"),
    col("Borough").alias("pickup_borough"),
    col("Zone").alias("pickup_zone_name"),
    col("service_zone").alias("pickup_service_zone")
)

df_enriched = (
    df_enriched
    .join(
        broadcast(zone_lookup),
        df_enriched.PULocationID == zone_lookup.LocationID,
        "left"
    )
    .drop("LocationID")
)

zone_lookup_drop = zone_lookup.select(
    col("LocationID").alias("DO_LocationID"),
    col("pickup_borough").alias("dropoff_borough"),
    col("pickup_zone_name").alias("dropoff_zone_name"),
    col("pickup_service_zone").alias("dropoff_service_zone")
)

df_enriched = (
    df_enriched
    .join(
        broadcast(zone_lookup_drop),
        df_enriched.DOLocationID == zone_lookup_drop.DO_LocationID,
        "left"
    )
    .drop("DO_LocationID")
)


# ------------------------------------------------------------------------------
# Aggregated Analytics Mart
# ------------------------------------------------------------------------------

analytics_mart = (
    df_enriched
    .groupBy(
        "hvfhs_license_num",
        "pickup_borough",
        "pickup_zone_name",
        "pickup_service_zone",
        "pickup_hour"
    )
    .agg(
        count("*").alias("total_trips"),
        _sum("total_passenger_payment").alias("total_revenue"),
        _sum("driver_pay").alias("total_driver_pay"),
        avg("trip_miles").alias("avg_trip_miles"),
        avg("trip_minutes").alias("avg_trip_minutes"),
        avg("revenue_per_mile").alias("avg_revenue_per_mile"),
        avg("is_shared").alias("shared_trip_ratio"),
        avg("is_congestion_trip").alias("congestion_trip_ratio")
    )
    .withColumnRenamed("hvfhs_license_num", "platform")
    .withColumnRenamed("PULocationID", "pickup_zone")
)

# ------------------------------------------------------------------------------
# Write Output (Partitioned for Performance)
# ------------------------------------------------------------------------------

analytics_mart.write \
    .mode("overwrite") \
    .partitionBy("platform") \
    .parquet(output_path)

spark.stop()