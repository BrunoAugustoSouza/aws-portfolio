output "lambda_name" {
  value = aws_lambda_function.job_ingestion.function_name
}

output "bucket_name" {
  value = aws_s3_bucket.job_analytics.bucket
}
