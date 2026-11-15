## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for fraud before approval and provides case management for analysts. It ensures sub-50ms latency, PCI-DSS Level 1 compliance, and 7-year auditability on a fixed 25,000 EUR monthly budget.

## Key Elements
- Fraud Analyst, Risk / Compliance Officer (Users)
- Merchant / Payment Gateway, Tokenization Provider, Audit Archive (External Systems)
- AWS API Gateway / Ingress (Amazon API Gateway, AWS WAF, AWS ACM Private CA)
- Fraud Screening Engine (Go/Rust, Amazon ECS on EC2)
- Case Management Frontend (Amazon React SPA, Amazon CloudFront, Amazon S3)
- Case Management Backend (Python FastAPI)
- Audit & Compliance Worker (Python, Amazon SQS)
- Amazon ElastiCache for Redis, AWS S3 Object Lock, Amazon Athena, AWS Secrets Manager, Amazon ECR

## Relationships
- Merchant / Payment Gateway -> AWS WAF: Forwards authorization requests [HTTPS / TLS 1.3]
- AWS WAF -> API Gateway HTTP API: Filters requests [Internal AWS routing]
- API Gateway HTTP API -> Fraud Screening Engine: Invokes real-time scoring [mTLS / HTTPS over Private VPC subnets, <10ms latency]
- Case Management Frontend -> API Gateway HTTP API: Sends administrative traffic [HTTPS / JWT OAuth 2.0]
- Fraud Screening Engine -> Amazon ElastiCache for Redis: Caches rules/models [Redis Protocol]
- Audit & Compliance Worker -> AWS S3 Object Lock: Stores immutable decision logs [HTTPS / AWS S3 API]

## Technology Stack
- Amazon API Gateway: HTTP API configuration for low latency (<50ms P99 at 3,000 RPS)
- AWS ACM Private CA: Native mTLS termination at the edge without Lambda compute overhead
- AWS WAF: OWASP Top 10 rule enforcement and DDoS mitigation
- Go / Rust (Amazon ECS on EC2): High-performance real-time fraud scoring engine
- Amazon ElastiCache for Redis: Low-latency in-memory rule retrieval
- AWS S3 Object Lock: Tamper-evident 7-year audit data storage

## Rationale
This serverless-edge and containerized architecture uses native AWS services to eliminate compute bottlenecks on the critical path, guaranteeing the P99 <50ms latency SLA at 3,000 RPS. Rigorous logging sanitization, WAF protection, and native mTLS meet strict PCI-DSS Level 1 and 7-year auditability requirements within the 25,000 EUR budget.