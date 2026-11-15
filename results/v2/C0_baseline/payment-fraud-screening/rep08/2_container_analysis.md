## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and provides case management for fraud analysts. It ensures PCI-DSS compliance while processing 3,000 transactions per second under strict latency constraints.

## Key Elements
- Fraud Analysts & Risk Managers
- Payment Gateway / Merchants
- Identity Provider
- BI / Analytics Tool
- API Gateway & Routing Layer
- Scoring Engine Container
- Case Management Container
- Audit & Event Store Container
- Messaging Backbone
- Model Storage & Management

## Relationships
- Payment Gateway to API Gateway & Routing Layer via HTTPS (REST/JSON)
- API Gateway to Scoring Engine Container via gRPC with mTLS
- Scoring Engine Container to Model Storage via HTTPS (S3 API)
- Scoring Engine & Case Management Containers to Messaging Backbone via HTTPS (SQS/SNS)
- Fraud Analysts to Case Management Container via HTTPS (OAuth2/OIDC)
- Case Management to Audit & Event Store Container via AWS SDK (DynamoDB API)

## Technology Stack
- **Cloud Provider:** AWS (eu-west-1 region) within a 25,000 EUR monthly budget
- **Ingress & Routing:** AWS API Gateway / ALB with built-in circuit breaker
- **Scoring Engine:** Go or Rust running on AWS Fargate Spot for high-performance low-latency execution
- **Case Management:** Node.js / React SPA backend with Amazon RDS (PostgreSQL) for relational state and row-level encryption
- **Audit & Event Store:** Amazon DynamoDB secured with AWS KMS Customer Managed Keys and S3 Object Lock for tamper-evident logs
- **Messaging:** Amazon SQS / SNS for serverless, low-maintenance event publishing
- **Model Storage & Secrets:** Amazon S3 for dynamic model weights and AWS Secrets Manager for credentials

## Rationale
The serverless-heavy container architecture minimizes operational overhead for a three-engineer team while keeping costs well within the 25,000 EUR monthly limit. Stateless Go/Rust scoring containers on Fargate Spot achieve sub-50 ms P99 latencies at scale, while encrypted databases and DynamoDB tamper-evident audit trails ensure full PCI-DSS Level 1 compliance.