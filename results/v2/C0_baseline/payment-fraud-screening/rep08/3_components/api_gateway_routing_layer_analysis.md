## Overview
The system provides real-time card-not-present payment fraud screening and case management for a payment processor. It securely scores authorization requests while maintaining strict PCI-DSS Level 1 compliance and low latency.

## Key Elements
* Payment Gateway / Merchants
* AWS API Gateway (API Gateway Authorizer, AWS WAF / Edge Terminator, Routing & Circuit Breaker Proxy)
* Scoring Engine Container (Go or Rust on AWS Fargate Spot)
* Case Management Container (Node.js / React SPA backend with Amazon RDS)
* Audit & Event Store Container (Amazon DynamoDB & S3)
* Amazon SQS / SNS Messaging Backbone
* Amazon S3 & AWS Secrets Manager (Model & Secret Storage)

## Relationships
* Payment Gateway -> API Gateway Authorizer: Submits payment authorizations via [HTTPS (REST/JSON)]
* API Gateway Authorizer -> Routing Proxy: Transmits validated requests via [Internal TLS / HTTP/2]
* Routing Proxy -> Scoring Engine Container: Routes scoring requests via [gRPC with mTLS]
* Scoring Engine Container -> Audit & Event Store: Stores immutable decision logs via [AWS SDK / HTTPS]

## Technology Stack
* AWS API Gateway: Ingress management chosen for built-in rate limiting and AWS WAF integration.
* AWS Fargate Spot: Container execution chosen to optimize compute costs within the 25,000 EUR/month budget.
* Go / Rust: High-performance languages selected for the Scoring Engine to achieve sub-50ms P99 latency.
* AWS Secrets Manager: Used for secure storage and SHA-256 hashing of API credentials.

## Rationale
This architecture uses serverless and managed AWS services to minimize operational overhead for a three-engineer team while respecting a fixed 25,000 EUR monthly budget. It meets strict performance, auditability, and PCI-DSS Level 1 security requirements.