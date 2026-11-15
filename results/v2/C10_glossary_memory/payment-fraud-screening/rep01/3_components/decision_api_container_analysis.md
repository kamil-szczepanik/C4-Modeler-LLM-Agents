## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud and manages analyst reviews. It ensures high performance and PCI-DSS compliance under strict latency constraints.

## Key Elements
- Decision API Container (Go, AWS Fargate)
- Scoring Engine Container (Python, FastAPI, AWS Fargate)
- Case Management Portal Container (AWS Fargate)
- Amazon Aurora PostgreSQL (Amazon Aurora PostgreSQL)
- API Handler Component (Go)
- Circuit Breaker & Fallback Manager (Go)
- Audit Dispatcher Component (Go)

## Relationships
- Merchant / Payment Gateway -> Decision API Container [gRPC / HTTPS]
- API Handler Component -> Scoring Engine Container [Internal VPC gRPC / mTLS]
- API Handler Component -> Circuit Breaker & Fallback Manager [Internal]
- Audit Dispatcher Component -> AWS Audit & Compliance Store [HTTPS / S3 API]
- API Handler Component -> Amazon Aurora PostgreSQL [TLS / SQL]

## Technology Stack
- Go: Chosen for high-throughput, low-latency API handling.
- AWS Fargate: Provides container orchestration within a €25,000 monthly budget.
- Amazon Aurora PostgreSQL: Stores transactional case data with encrypted storage.
- AWS KMS: Encrypts data at rest using AES-256 and customer-managed keys.

## Rationale
This architecture uses Go and Fargate to achieve sub-50ms P99 latency at 3,000 TPS. Robust encryption, tokenization, and audit trails ensure full compliance with PCI-DSS Level 1 and 7-year audit requirements.