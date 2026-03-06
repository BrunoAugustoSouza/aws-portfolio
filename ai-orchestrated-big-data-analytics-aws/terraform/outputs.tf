output "bucket_name" {
  value = aws_s3_bucket.data_lake.bucket
}

output "emr_application_id" {
  value = aws_emrserverless_application.spark_app.id
}

output "step_function_arn" {
  value = aws_sfn_state_machine.orchestrator.arn
}