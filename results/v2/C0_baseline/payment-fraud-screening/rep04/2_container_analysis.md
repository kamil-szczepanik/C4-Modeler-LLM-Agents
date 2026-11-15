## Overview
- Real-time payment fraud screening system for card-not-present transactions.
- Provides sub-50ms latency scoring, PCI-DSS Level 1 compliance, and 7-year tamper-evident audit logging.

## Key Elements
- Shopper / Cardholder & Merchant (External)
- AWS API Gateway (Ingress & Tokenization Boundary)
- Scoring Engine (Rust service on Amazon ECS Fargate)
- Case Management App (Node.js/Python backend on ECS Fargate)
- Feature Store & Cache (Amazon ElastiCache Redis & Amazon DynamoDB)
- Audit & Streaming Pipeline (Amazon Kinesis Data Streams & Kinesis Firehose)
- Audit Storage (Amazon S3 with Object Lock in Compliance Mode)
- External IdP (OAuth2/OIDC for analyst authentication)

## Relationships
- Shopper to AWS API Gateway via REST/JSON over HTTPS (TLS 1.3)
- API Gateway to Scoring Engine via internal ALB / gRPC
- Scoring Engine to Amazon ElastiCache and DynamoDB via TCP/TLS
- Case Management App to Amazon Kinesis Data Streams via HTTPS
- Kinesis Firehose to Amazon S3 via AWS internal storage APIs
- Analysts to Case Management App via OAuth2/OIDC over HTTPS

## Technology Stack
- AWS API Gateway: Low-overhead HTTP/2 ingress and edge tokenization boundary for PAN data
- Amazon ECS (Fargate): Serverless container orchestration for lightweight operational footprint
- Rust (Tokio): High-performance, low-latency execution for the real-time scoring engine
- Amazon ElastiCache (Redis): In-memory caching for low-latency feature lookups (<50ms P99)
- Amazon S3 with Object Lock: Tamper-evident 7-year compliance audit log storage
- AWS KMS & Secrets Manager: Data encryption at rest and secure credential management

## Rationale
- Decouples real-time scoring from asynchronous case management to protect sub-50ms latency under high load.
- Uses serverless ECS Fargate and managed AWS services to satisfy strict cost, security, and compliance requirements within a 3-engineer team capacity.