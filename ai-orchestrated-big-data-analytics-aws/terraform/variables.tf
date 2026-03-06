variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "sa-east-1"
}

variable "project_name" {
  description = "Project prefix"
  type        = string
  default     = "ai-big-data-orchestrator"
}

variable "bucket_name" {
  description = "S3 bucket name"
  type        = string
}