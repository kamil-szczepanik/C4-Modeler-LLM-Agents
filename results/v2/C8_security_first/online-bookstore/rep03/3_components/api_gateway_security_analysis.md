## Overview
- The system is an online bookstore providing catalog browsing, secure checkout, reviews, and recommendations for a global audience.
- Its core purpose is to deliver a secure, multi-currency, and highly scalable retail platform meeting strict GDPR, CCPA, and uptime constraints.

## Key Elements
- Shopper / Reviewer and Store Administrator (Users)
- Single Page Application (React, TypeScript, Amazon CloudFront, Amazon S3)
- API Gateway & Security (AWS API Gateway, AWS WAF, AWS Lambda Authorizer)
- Backend Containers: Catalogue Service, Shopping Cart & Checkout Service, Review Service, Localization & Currency Service (AWS ECS Fargate)
- Data Tier: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis)
- External Systems: Payment Gateway, Shipping Provider APIs, Recommendation Engine, Notification Service

## Relationships
- Single Page Application -> API Gateway & Security: Client requests [HTTPS/REST, TLS 1.3]
- API Gateway & Security -> ECS Fargate Services: Internal routing [gRPC with mTLS, ACM certificates]
- API Gateway & Security -> AWS Secrets Manager: Credential retrieval [AWS SDK / IAM]
- API Gateway & Security -> Amazon Kinesis Data Firehose: Log streaming [AWS SDK]

## Technology Stack
- Cloud Infrastructure: AWS (us-east-1, eu-west-1, ap-southeast-1) managed via AWS CDK for repeatable deployments.
- Edge & Security: AWS API Gateway, AWS WAF, and AWS Lambda Authorizer for perimeter defense, JWT validation, and RBAC enforcement.
- Internal Communication: gRPC with mTLS for secure, low-latency service-to-service messaging.
- Observability: AWS X-Ray and Amazon CloudWatch for distributed tracing, correlation ID propagation, and analytics.
- Data Storage: Amazon Aurora PostgreSQL, Amazon DynamoDB, and Amazon ElastiCache (Redis) for scalable data persistence and caching.

## Rationale
- This architecture combines multi-region AWS services to guarantee 99.95% uptime and sub-2-second page loads for 1M MAU.
- Perimeter security controls, automated canary deployments, and PII redaction ensure full compliance with GDPR, CCPA, and OWASP Top-10 requirements.