from constructs import Construct
from aws_cdk import (
    Stack,
    CfnOutput,
)
from .bucket import StaticSiteBucket
from .distribution import StaticSiteDistribution

class StaticSiteStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1) S3
        site_bucket = StaticSiteBucket(self, "StaticSiteBucket").bucket

        # 2) CloudFront (sin dominio/certificado)
        dist = StaticSiteDistribution(
            self,
            "StaticSiteDistribution",
            bucket=site_bucket,
            index_document="index.html",
            is_spa=True,
        ).distribution

        # Salidas
        CfnOutput(self, "BucketName", value=site_bucket.bucket_name)
        CfnOutput(self, "CloudFrontDomain", value=dist.domain_name)
