## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations to protect transactions before approval. It is hosted on AWS in the eu-west-1 region to serve a mid-size payment processor.

## Key Elements
- Fraud Analysts
- Payment Gateway / Acquirer Systems
- Card Networks / Tokenization Vaults
- Audit / Compliance Archive
- Identity Provider (IdP)
- Amazon API / Application Load Balancer (ALB)
- Fraud Scoring Engine (ECS Fargate container in Go or Rust)
- Case Management Service (ECS Fargate container in Node.js/Python)
- Amazon ElastiCache Serverless (Redis sidecar)
- Amazon DynamoDB and Amazon Aurora Serverless v2
- Amazon QLDB / S3 Object Lock buckets
- AWS KMS (Key Management Service)

## Relationships
- Payment Gateway to Amazon API Gateway / ALB via HTTPS (REST/JSON)
- API Gateway to Fraud Scoring Engine via gRPC over mTLS
- API Gateway to Case Management Service via gRPC over mTLS
- Fraud Scoring Engine to ElastiCache Serverless via Redis protocol over mTLS
- Case Management Service to Amazon Aurora Serverless v2 via TLS
- Fraud Scoring Engine and Case Management Service to DynamoDB and QLDB via AWS SDK over TLS
- Fraud Analysts to Case Management Service via HTTPS using OIDC/SAML via AWS IAM Identity Center

## Technology Stack
- **Compute:** AWS ECS Fargate for serverless, zero-ops container orchestration.
- **Languages:** Go or Rust for high-throughput, low-latency fraud scoring.
- **Databases:** Amazon DynamoDB and Amazon Aurora Serverless v2 for managed, low-maintenance persistence.
- **Caching:** Amazon ElastiCache Serverless for in-memory model and rule caching.
- **Audit Storage:** Amazon QLDB and S3 Object Lock for immutable, tamper-evident 7-year retention.
- **Security:** AWS KMS for customer-managed encryption keys, API Gateway tokenization, and distroless container base images.

## Rationale
Serverless and managed AWS services minimize operational toil for a small three-engineer team while easily adhering to the 25,000 EUR monthly budget constraint. In-memory caching, gRPC, and stateless Fargate containers guarantee P99 latencies under 50ms at 3,000 requests per second to meet strict performance demands.