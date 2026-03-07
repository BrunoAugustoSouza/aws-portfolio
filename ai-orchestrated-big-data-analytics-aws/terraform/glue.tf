resource "aws_glue_catalog_database" "analytics_db" {
  name = "nyc_tlc_analytics"
}

resource "aws_glue_crawler" "hvfhs_crawler" {

  name = "hvfhs-analytics-crawler"
  role = aws_iam_role.glue_role.arn
  database_name = aws_glue_catalog_database.analytics_db.name

  s3_target {
    path = "s3://${aws_s3_bucket.data_lake.bucket}/curated/hvfhs_analytics_mart/"
  }

  schema_change_policy {
    delete_behavior = "LOG"
    update_behavior = "UPDATE_IN_DATABASE"
  }
}