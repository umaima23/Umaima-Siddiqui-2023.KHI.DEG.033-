provider "aws" {
  region = "us-east-1" 
}


module "s3_module" {
  source       = "../Assignment-5a"
  bucket_name  = "ifra-saleem-bucket"
}

resource "aws_s3_bucket_object" "directory" {
  bucket = module.s3_module.s3_bucket
  key    = "day2/IaC/"
  acl    = "private"
}
