# EventBridge

# Everyday às 04:00 p.m. UTC (or 01:00 p.m in Brazil)
resource "aws_cloudwatch_event_rule" "daily_pipeline" {
  name                = "ai-bigdata-daily-trigger"
  description         = "Trigger Step Function daily"
  schedule_expression = "cron(0 16 * * ? *)"

  tags = {
    Project = "ai-bigdata"
  }
}

# Invoke Step fun

resource "aws_iam_role" "eventbridge_role" {
  name = "ai-bigdata-eventbridge-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "events.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_policy" "eventbridge_policy" {
  name = "ai-bigdata-eventbridge-policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "states:StartExecution"
      ]
      Resource = aws_sfn_state_machine.orchestrator.arn
    }]
  })
}

resource "aws_iam_role_policy_attachment" "eventbridge_attach" {
  role       = aws_iam_role.eventbridge_role.name
  policy_arn = aws_iam_policy.eventbridge_policy.arn
}

# Target → Step Function

resource "aws_cloudwatch_event_target" "stepfn_target" {
  rule      = aws_cloudwatch_event_rule.daily_pipeline.name
  arn       = aws_sfn_state_machine.orchestrator.arn
  role_arn  = aws_iam_role.eventbridge_role.arn

  input = jsonencode({
    trigger = "scheduled"
  })

  depends_on = [
    aws_iam_role_policy_attachment.eventbridge_attach
  ]
}