## Overview
- Real-Time Payment Fraud Screening System screens card-not-present payment authorizations in the AWS `eu-west-1` region.
- Enables automated fraud scoring and provides case management tools for fraud analysts.

## Key Elements
- Payment Gateway
- Fraud Analysts & Risk Managers
- Identity Provider (AWS Cognito/Okta)
- AWS ECS Fargate
- Application Load Balancer
- AWS QLDB and S3 Object Lock
- AWS KMS

## Relationships
- Payment Gateway interacts with Fraud Screening System via mTLS and gRPC.
- Fraud Analysts and Risk Managers interact with Fraud Screening System via HTTPS and TLS 1.3 using OAuth2/OIDC.
- Fraud Screening System interacts with AWS KMS and AWS QLDB/S3 via AWS IAM and TLS.

## Technology Stack
- AWS ECS Fargate: Container orchestration for predictable low-latency scaling without serverless cold starts.
- AWS QLDB and S3 Object Lock: Tamper-evident, append-only data stores for 7-year audit compliance.
- AWS KMS: AES-256 encryption at rest.
- TLS 1.3 and mTLS: Secure data in transit and upstream integrations.
- Managed IdP (AWS Cognito/Okta): Authentication and OAuth2/OIDC enforcement.

## Rationale
- Managed AWS services reduce operational overhead for a 3-engineer team while respecting the 25,000 EUR monthly budget constraint.
- ECS Fargate and containerized components meet the stringent sub-50ms P99 latency and high-throughput reliability requirements.