## Overview
- Real-time payment fraud screening system for card-not-present transactions.
- Purpose is screening authorizations, case management, and tamper-evident auditing.

## Key Elements
- Fraud Analysts and Risk Operations Managers (Users)
- Payment Gateway / Acquirer and Card Schemes (External Systems)
- API Gateway & Tokenization Proxy (Java / Spring Cloud Gateway)
- Fraud Scoring Engine (Java / Spring Boot)
- Case Management & Rule UI (Node.js / TypeScript)
- Amazon DynamoDB (AWS DynamoDB)
- Amazon S3 with Object Lock (Amazon S3)
- Amazon SQS (Amazon SQS)

## Relationships
- Fraud Scoring Engine -> Amazon S3 with Object Lock: Rule distribution and audit logs [HTTPS / TLS 1.2+ via VPC Gateway Endpoint]
- Case Management & Rule UI -> Amazon S3 with Object Lock: Audit logs storage [HTTPS / TLS 1.2+ via VPC Gateway Endpoint]
- API Gateway -> Fraud Scoring Engine: Authorization scoring [REST / gRPC]
- Fraud Scoring Engine -> Amazon DynamoDB: State and session storage [AWS SDK]

## Technology Stack
- AWS Cloud (eu-west-1): Target cloud provider for scalability and PCI-DSS compliance.
- Java / Spring Boot: Core language for high-performance fraud scoring.
- Node.js / TypeScript: Frontend and case management API stack.
- Amazon S3 with Object Lock: Implements 7-year tamper-evident audit storage in Compliance Mode.
- Amazon S3 Glacier Flexible Retrieval: Lifecycle tiering for cost optimization.
- AWS KMS: Encryption via Customer Managed Keys for security and tokenization compliance.

## Rationale
- Meets PCI-DSS Level 1 and 7-year audit requirements within a 25,000 EUR monthly budget.
- Achieves P99 latency below 50 ms for high-throughput fraud scoring and case management.