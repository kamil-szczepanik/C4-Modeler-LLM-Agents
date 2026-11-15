## Overview
The Online Bookstore system provides a scalable, secure, and globally distributed e-commerce platform for browsing, purchasing physical and electronic books, reviews, and recommendations. It handles 1 million MAU with high availability and GDPR/CCPA compliance across multiple AWS regions.

## Key Elements
- **Single Page Application (SPA)**: React, TypeScript, Amazon S3, Amazon CloudFront.
- **API Gateway**: AWS API Gateway, AWS WAF, Amazon CloudFront.
- **API Gateway Internal Components**: Request Router / Reverse Proxy, Authentication & Authorization Filter, Rate Limiting & Throttling Controller, Request/Response Transformation Engine.
- **Core Containers**: Core API Application, Recommendation Service, Admin Dashboard Container (Amazon ECS Fargate).
- **Data & Caching**: Amazon Aurora PostgreSQL, Amazon ElastiCache Redis.
- **Integration & Security**: AWS Secrets Manager, AWS X-Ray, AWS PrivateLink / VPC Links, Amazon SQS, Amazon SNS, Amazon EventBridge.

## Relationships
- **SPA -> API Gateway**: Communicates securely [HTTPS/REST/GraphQL, TLS 1.3].
- **API Gateway -> Core API Application**: Dispatches traffic [mTLS, AWS PrivateLink / VPC Links].
- **API Gateway -> Recommendation Service**: Routes traffic [mTLS, AWS PrivateLink / VPC Links].
- **API Gateway -> Admin Dashboard Container**: Routes traffic with scope enforcement [mTLS, AWS PrivateLink / VPC Links].

## Technology Stack
- **Cloud Infrastructure**: AWS across us-east-1, eu-west-1, ap-southeast-1 for global reach and resilience.
- **Compute**: Amazon ECS Fargate for containerized microservices execution without server management.
- **Traffic & Edge Security**: AWS API Gateway fronted by Amazon CloudFront and AWS WAF for DDoS and OWASP protection.
- **State & Caching**: Amazon Aurora PostgreSQL for relational data and Amazon ElastiCache (Redis) for rate limiting.
- **Security & Observability**: AWS Secrets Manager for secrets and AWS X-Ray for distributed tracing.

## Rationale
This architecture uses a globally distributed, multi-region API Gateway and containerized microservices on AWS Fargate to effortlessly scale to 1 million MAU. Strict mTLS, WAF integration, and data masking ensure robust security, low latency, and full GDPR/CCPA compliance.