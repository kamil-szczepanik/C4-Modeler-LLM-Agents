## Overview
The system provides real-time payment fraud screening for card-not-present authorizations to protect transactions while ensuring sub-50ms latency. It handles case management, secure tokenization, and auditable decision-making under strict PCI-DSS Level 1 constraints.

## Key Elements
- Payment Gateway / Core Processing Engine
- AWS Network Load Balancer (NLB)
- AWS API Gateway (HTTP API)
- AWS WAF
- Fraud Scoring Engine (Go)
- Case Management Backend (Java / Spring Boot with React UI)
- Audit Logger (AWS Lambda / Worker)
- Feature Store (AWS ElastiCache for Redis)
- Relational Store (Amazon RDS for PostgreSQL)
- Tamper-Evident Storage (Amazon S3 with Object Lock in Compliance Mode)
- Message Queue (Amazon SQS with AWS KMS encryption)

## Relationships
- Payment Gateway / Core Processing Engine -> AWS Network Load Balancer: Forwards raw traffic [TCP/TLS]
- AWS Network Load Balancer -> AWS API Gateway: Forwards decapsulated requests [HTTP]
- AWS API Gateway -> Fraud Scoring Engine: Invokes real-time scoring [gRPC via VPC Link with mTLS]
- Fraud Scoring Engine -> Feature Store: Retrieves scoring features [RESP/TCP]
- Fraud Scoring Engine -> Message Queue: Publishes audit payloads [AWS SDK / SQS]
- Audit Logger -> Tamper-Evident Storage: Stores immutable compliance logs [HTTPS / S3 API]

## Technology Stack
- AWS (eu-west-1): Target cloud infrastructure within the 25,000 EUR monthly budget constraint.
- Go: Powers the Fraud Scoring Engine for high-throughput, low-latency processing.
- Java / Spring Boot & React: Powers the Case Management Backend and Analyst UI.
- Amazon RDS for PostgreSQL: Relational storage for structured transactional and case data.
- Amazon S3 with Object Lock: Tamper-evident storage satisfying the 7-year auditability requirement.

## Rationale
This architecture uses Go and gRPC to guarantee sub-50ms P99 latency at 3,000 TPS. Edge tokenization via AWS services successfully minimizes the PCI-DSS Level 1 compliance boundary while remaining within the fixed budget.