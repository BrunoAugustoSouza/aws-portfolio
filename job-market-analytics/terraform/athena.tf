resource "aws_athena_workgroup" "job_analytics_wg" {
  name = "job-analytics-wg"

  configuration {
    result_configuration {
      output_location = "s3://${aws_s3_bucket.job_analytics.bucket}/athena-results/"
    }
  }
}
