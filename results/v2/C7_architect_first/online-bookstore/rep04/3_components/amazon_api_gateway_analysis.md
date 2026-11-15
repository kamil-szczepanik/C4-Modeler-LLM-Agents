## Overview
This architecture establishes the component-level decomposition of the Amazon API Gateway for a global online bookstore system handling 1M MAU. It ensures secure, scalable, and multi-region routing across AWS infrastructure while complying with GDPR, CCPA, and OWASP standards.

## Key Elements
- Routing & Regional Edge Component (AWS Regional API Gateway, CloudFront, AWS WAF, AWS Shield)
- Authentication & Authorization Component (AWS Lambda Authorizer, Amazon Cognito)
- Rate Limiting & Throttling Component (API Gateway Usage Plans, Token Bucket)
- Request/Response Transformation Component (VTL/AWS Lambda mappers)
- API Versioning & Routing Component (Path/header-based routing engine)
- Monetization & Usage Analytics Component (AWS CloudWatch, Amazon Kinesis Data Firehose)

## Relationships
- SPA -> Routing & Regional Edge Component [HTTPS / JSON]
- Authentication & Authorization Component -> Amazon Cognito [HTTPS / OIDC]
- Routing & Regional Edge Component -> API Versioning & Routing Component [Internal HTTP]
- API Versioning & Routing Component -> Catalog & Order ECS Containers [HTTP/2]
- Monetization & Usage Analytics Component -> Amazon Kinesis [Async JSON]

## Technology Stack
- AWS API Gateway & CloudFront: Manages global ingress, edge routing, and mTLS termination.
- AWS Lambda: Executes custom token authorization, request validation, and payload transformation.
- Amazon Cognito: Provides identity management and OIDC-compliant JWT generation.
- Amazon Kinesis Data Firehose & CloudWatch: Captures sanitized monetization metrics and operational telemetry.
- AWS CDK & GitHub Actions: Enables GitOps-driven, multi-region infrastructure deployment.

## Rationale
Decomposing the API Gateway isolates critical cross-cutting concerns like security, routing, and rate limiting to protect backend microservices. This design directly satisfies the 99.95% availability SLA, multi-region scaling requirements (`us-east-1`, `eu-west-1`, `ap-southeast-1`), and strict data privacy regulations.