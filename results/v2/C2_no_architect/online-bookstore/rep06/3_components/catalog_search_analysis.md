## Overview
An AWS-hosted online bookstore e-commerce platform supporting 1M MAU with global catalog browsing, search, and secure multi-currency transactions. The architecture prioritizes sub-2-second page loads and strict GDPR/CCPA compliance across three global regions.

## Key Elements
- **Users**: Book Buyer, Store Administrator, Author/Publisher Partner
- **External Systems**: Third-Party Payment Gateways, Shipping APIs, AWS CloudFront & WAF
- **Containers**: Catalog & Search (Amazon ECS/EKS), Personalization Engine (AWS Lambda@Edge), Checkout/Payment, Localization/Currency, Notification Container
- **Data & Infrastructure**: OpenSearch on AWS, AWS SQS/SNS, Amazon Kinesis Data Firehose, Amazon S3 & Athena, AWS App Mesh

## Relationships
- AWS CloudFront & WAF -> Catalog & Search: Routes requests via HTTPS / mTLS over AWS App Mesh
- Catalog & Search -> OpenSearch on AWS: Executes catalog and keyword queries via private VPC networking
- Catalog & Search -> Amazon Kinesis Data Firehose: Streams asynchronous search telemetry via FluentBit

## Technology Stack
- **Compute & Orchestration**: Amazon ECS/EKS with HPA for container scaling supporting 1M MAU
- **Search & Caching**: OpenSearch on AWS with cross-cluster replication; AWS CloudFront for regional edge caching
- **Networking & Security**: AWS WAF for input sanitization, AWS App Mesh for mTLS, AWS KMS for encryption at rest
- **Analytics & Telemetry**: FluentBit, Amazon Kinesis Data Firehose, Amazon S3, and Amazon Athena for asynchronous PII-masked search analytics

## Rationale
Decoupling search infrastructure via OpenSearch and asynchronous telemetry via Kinesis ensures sub-2-second latency under high loads. Private VPC isolation, mTLS, and automated PII masking satisfy strict security, OWASP, and GDPR/CCPA compliance requirements.