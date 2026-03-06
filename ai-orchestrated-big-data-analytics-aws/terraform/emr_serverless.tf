# Upload Spark Script to S3

resource "aws_s3_object" "spark_script" {
  bucket = var.bucket_name
  key    = "jobs/hvfhs_analytics.py"
  source = "${path.module}/../spark_jobs/hvfhs_analytics.py"
  etag   = filemd5("${path.module}/../spark_jobs/hvfhs_analytics.py")

  depends_on = [
    aws_s3_bucket.data_lake
  ]
}
# EMR Serverless Application

resource "aws_emrserverless_application" "spark_app" {
  name          = "ai-bigdata-spark-app"
  release_label = "emr-6.12.0"
  type          = "SPARK"

  auto_stop_configuration {
    enabled              = true
    idle_timeout_minutes = 5
  }

  initial_capacity {
    initial_capacity_type = "Driver"

    initial_capacity_config {
      worker_count = 1

      worker_configuration {
        cpu    = "2 vCPU"
        memory = "4 GB"
        disk   = "20 GB"
      }
    }
  }

  initial_capacity {
    initial_capacity_type = "Executor"

    initial_capacity_config {
      worker_count = 2

      worker_configuration {
        cpu    = "4 vCPU"
        memory = "8 GB"
        disk   = "20 GB"
      }
    }
  }

  maximum_capacity {
    cpu    = "32 vCPU"
    memory = "128 GB"
  }
}