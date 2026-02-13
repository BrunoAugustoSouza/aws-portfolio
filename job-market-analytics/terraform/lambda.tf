resource "aws_lambda_function" "job_ingestion" {
  function_name = "${var.project_name}-ingestion"

  runtime = "python3.10"
  handler = "handler.lambda_handler"

  role = aws_iam_role.lambda_role.arn

  filename         = "../lambda/lambda.zip"
  source_code_hash = filebase64sha256("../lambda/lambda.zip")

  timeout      = 10
  memory_size  = 512

  environment {
    variables = {
      BUCKET_NAME = var.bucket_name
      SOURCE_NAME = "themuse"
    }
  }
}
