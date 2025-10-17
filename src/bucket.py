from constructs import Construct
from aws_cdk import (
    RemovalPolicy,
    aws_s3 as s3,
)

class StaticSiteBucket(Construct):
    def __init__(self, scope: Construct, construct_id: str,
                 index_document: str = "index.html",
                 error_document: str = "error.html") -> None:
        super().__init__(scope, construct_id)

        # Bucket privado para origin de CloudFront
        self.bucket = s3.Bucket(
            self,
            "SiteBucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
