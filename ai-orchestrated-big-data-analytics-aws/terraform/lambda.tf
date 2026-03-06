# Lambda Packaging

data "archive_file" "lambda_zip" {
  type        = "zip"
  source_dir  = "${path.module}/../lambda"
  output_path = "${path.module}/lambda.zip"
}

# Lambda Function

resource "aws_lambda_function" "data_ingestion" {
  function_name = "ai-bigdata-raw-ingestion"
  role          = aws_iam_role.lambda_role.arn

  handler = "handler.lambda_handler"
  runtime = "python3.11"

  filename         = data.archive_file.lambda_zip.output_path
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256

  timeout     = 420
  memory_size = 512

  environment {
    variables = {
      BUCKET_NAME = aws_s3_bucket.data_lake.bucket
    }
  }
}