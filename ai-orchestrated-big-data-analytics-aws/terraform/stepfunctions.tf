# CloudWatch Log Group

resource "aws_cloudwatch_log_group" "stepfn_logs" {
  name              = "/aws/stepfunctions/ai-bigdata-orchestrator"
  retention_in_days = 7
}


# Step Function Definition


locals {
  state_machine_definition = jsonencode({
    Comment = "AI Big Data Orchestrator with EMR Serverless"
    StartAt = "IngestData"

    States = {

      IngestData = {
        Type     = "Task"
        Resource = "arn:aws:states:::lambda:invoke"

        Parameters = {
          FunctionName = aws_lambda_function.data_ingestion.arn
          Payload      = {}
        }

        Retry = [{
          ErrorEquals     = ["States.ALL"]
          IntervalSeconds = 10
          MaxAttempts     = 3
          BackoffRate     = 2
        }]

        Next = "RunSparkJob"
      }

      RunSparkJob = {
        Type     = "Task"
        Resource = "arn:aws:states:::emr-serverless:startJobRun.sync"

        Parameters = {
          ApplicationId    = aws_emrserverless_application.spark_app.id
          ExecutionRoleArn = aws_iam_role.emr_serverless_role.arn

          JobDriver = {
            SparkSubmit = {
              EntryPoint = "s3://${aws_s3_bucket.data_lake.bucket}/jobs/hvfhs_analytics.py"

              EntryPointArguments = [
                aws_s3_bucket.data_lake.bucket
              ]

              SparkSubmitParameters = "--conf spark.sql.shuffle.partitions=16 --conf spark.executor.memory=4g --conf spark.driver.memory=4g"
            }
          }
        }

        Retry = [{
          ErrorEquals     = ["States.ALL"]
          IntervalSeconds = 30
          MaxAttempts     = 1
          BackoffRate     = 1
        }]

        Next = "RunGlueCrawler"
      }

      RunGlueCrawler = {
        Type     = "Task"
        Resource = "arn:aws:states:::aws-sdk:glue:startCrawler"

        Parameters = {
          Name = aws_glue_crawler.hvfhs_crawler.name
        }

        TimeoutSeconds = 60

        Retry = [{
          ErrorEquals     = ["States.ALL"]
          IntervalSeconds = 20
          MaxAttempts     = 3
          BackoffRate     = 2
        }]

        Next = "WaitCrawler"
      }

      WaitCrawler = {
        Type    = "Wait"
        Seconds = 20
        Next    = "CheckCrawler"
      }

      CheckCrawler = {
        Type     = "Task"
        Resource = "arn:aws:states:::aws-sdk:glue:getCrawler"

        Parameters = {
          Name = aws_glue_crawler.hvfhs_crawler.name
        }

        TimeoutSeconds = 30

        Retry = [{
          ErrorEquals     = ["States.ALL"]
          IntervalSeconds = 10
          MaxAttempts     = 3
          BackoffRate     = 2
        }]

        Next = "isCrawlerFinished"
      }

      isCrawlerFinished = {
        Type = "Choice"

        Choices = [
          {
            Variable     = "$.Crawler.State"
            StringEquals = "READY"
            Next         = "CrawlerDone"
          }
        ]

        Default = "WaitCrawler"
      }

      CrawlerDone = {
        Type = "Succeed"
      }
    }
  })
}


# Step Function

resource "aws_sfn_state_machine" "orchestrator" {
  name     = "ai-bigdata-orchestrator"
  role_arn = aws_iam_role.stepfn_role.arn

  definition = local.state_machine_definition

  depends_on = [
    aws_lambda_function.data_ingestion,
    aws_emrserverless_application.spark_app,
    aws_iam_role_policy_attachment.stepfn_attach,
    aws_s3_bucket.data_lake,
    aws_cloudwatch_log_group.stepfn_logs
  ]


  #logging_configuration {
  #  log_destination        = "${aws_cloudwatch_log_group.stepfn_logs.arn}:*"
  #  include_execution_data = true
  #  level                  = "ALL"
  #}
}