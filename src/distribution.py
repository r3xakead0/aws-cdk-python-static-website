from constructs import Construct
from aws_cdk import (
    Duration,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3 as s3,
)

class StaticSiteDistribution(Construct):
    def __init__(self, scope: Construct, construct_id: str, *,
                 bucket: s3.IBucket,
                 index_document: str = "index.html",
                 is_spa: bool = True,
                 default_ttl_seconds: int = 3600) -> None:
        super().__init__(scope, construct_id)

        origin = origins.S3Origin(bucket)

        error_responses = []
        if is_spa:
            error_responses = [
                cloudfront.ErrorResponse(
                    http_status=403, ttl=Duration.seconds(10),
                    response_http_status=200, response_page_path=f"/{index_document}"
                ),
                cloudfront.ErrorResponse(
                    http_status=404, ttl=Duration.seconds(10),
                    response_http_status=200, response_page_path=f"/{index_document}"
                ),
            ]

        self.distribution = cloudfront.Distribution(
            self,
            "Distribution",
            default_root_object=index_document,
            default_behavior=cloudfront.BehaviorOptions(
                origin=origin,
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                cache_policy=cloudfront.CachePolicy.CACHING_OPTIMIZED,
            ),
            # sin domain_names ni certificate
            error_responses=error_responses,
        )
