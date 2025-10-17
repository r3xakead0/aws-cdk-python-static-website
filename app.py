#!/usr/bin/env python3
import os
import aws_cdk as cdk
from src.site_stack import StaticSiteStack

app = cdk.App()

StaticSiteStack(
    app,
    "StaticSiteStack",
    env=cdk.Environment(
        region=os.getenv("CDK_DEFAULT_REGION"),
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
    ),
)

app.synth()
