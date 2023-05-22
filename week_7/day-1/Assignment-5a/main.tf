terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.39"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-east-1"
}

variable "bucket_name" {
  description = "Name of the S3 bucket"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = var.bucket_name
  acl    = "private"
}

output "s3_bucket" {
  value = aws_s3_bucket.my_bucket.id
}
