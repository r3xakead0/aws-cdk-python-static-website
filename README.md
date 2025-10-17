# Static website with AWS CDK + Python

Sample project deploying a static website on AWS using Amazon S3 as the file repository and Amazon CloudFront as the CDN. The site content explains the services involved and is served from the [`public`](public) folder.

![diagram](diagram/static_website.png?raw=true)

## Prerequisites

- Python 3.9 or newer.
- Node.js 16+ and AWS CDK Toolkit (`npm install -g aws-cdk`).
- AWS CLI configured with credentials that can create S3, Cloudfront, and CloudFormation resources.
- Internet access to install Python packages.

## Install Dependencies

```bash
python3 -m venv .venv
. .venv/bin/activate

pip install -r requirements.txt
```
## Deploy

```bash
# First time only per account/region
cdk bootstrap aws://<ACCOUNT_ID>/<REGION>

# Review CloudFormation template
cdk synth

# Deploy
cdk deploy
```

## Publish website

```bash
aws s3 sync ./public/ s3://$(cdk output StaticSiteStack.BucketName)
```

## Cleaning Up

```bash
cdk destroy
```
