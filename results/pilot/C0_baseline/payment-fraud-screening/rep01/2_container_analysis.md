## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at 3,000 TPS within a sub-50ms P99 latency SLA. It provides a secure case management portal for fraud analysts while maintaining PCI-DSS Level 1 compliance and a 7-year tamper-evident audit trail.

## Key Elements
- Merchants and API Gateway / Network Load Balancer (NLB)
- Fraud Analysts and Identity Provider
- Scoring Engine Container (Go, AWS ECS Fargate)
- Case Management Portal Container (Node.js/TypeScript, PostgreSQL)
- Audit Storage & Processing (Amazon SQS, Amazon Kinesis Firehose, S3 Object Lock)
- Feature Store (Redis Cluster)

## Relationships
- Merchant Integration Systems to API Gateway via HTTPS (REST/JSON)
- API Gateway to Scoring Engine via gRPC over HTTP/2
- Scoring Engine to Redis Cluster via TCP (In-memory feature lookups)
- Scoring Engine to Amazon SQS via AWS SDK (Async audit events)
- Case Management Portal to PostgreSQL via TLS
- Kinesis Firehose to S3 Object Lock via HTTPS (WORM audit storage)

## Technology Stack
- **Compute:** AWS ECS Fargate for container orchestration with Go (Scoring Engine) and Node.js/TypeScript (Case Management Portal) for optimal performance and memory safety.
- **Data & Caching:** Redis Cluster for low-latency feature lookups; PostgreSQL for relational case management persistence.
- **Messaging & Streaming:** Amazon SQS for asynchronous event decoupling; Amazon Kinesis Firehose for ingestion into storage.
- **Storage & Compliance:** Amazon S3 with S3 Object Lock in compliance mode for 7-year tamper-evident audit retention.
- **Security & Networking:** mTLS for inter-container communication, OAuth2/OIDC for Identity Provider integration, AWS Cloud Map for internal service discovery.

## Rationale
This architecture decouples the high-throughput real-time payment path from analytical case management to protect the sub-50ms SLA and strict security boundaries. Standardizing on managed AWS services enables a three-engineer team to operate the platform reliably within the €25,000 monthly budget while satisfying PCI-DSS Level 1 and 7-year audit requirements.