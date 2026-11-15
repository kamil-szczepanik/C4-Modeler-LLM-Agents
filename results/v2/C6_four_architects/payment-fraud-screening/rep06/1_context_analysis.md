## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at 3,000 TPS while managing analyst review cases. It ensures PCI-DSS Level 1 compliance, 7-year auditability, and sub-50ms latency within a 25,000 EUR monthly AWS budget.

## Key Elements
* Real-Time Payment Fraud Screening System
* Payment Gateway / Core Ledger (External System)
* Fraud Analysts (Internal Users)
* Identity Provider / IdP (External System)
* Compliance Archive / AWS S3 Object Lock (External Storage)
* API Gateway / AWS ALB (Container)
* Fraud Scoring Engine (Container)
* Case Management Backend (Container)
* AWS ElastiCache / Redis (Container)
* Amazon Aurora Serverless v2 PostgreSQL (Container)

## Relationships
* Payment Gateway -> API Gateway / ALB: Synchronous gRPC over TLS for payment scoring
* Fraud Analysts -> IdP: HTTPS for authentication
* Fraud Analysts -> Case Management Backend: HTTPS for case reviews
* Fraud Scoring Engine -> AWS ElastiCache (Redis): In-memory TCP for feature lookup
* Fraud Scoring Engine -> Compliance Archive: AWS VPC Gateway Endpoints for asynchronous S3 Object Lock exports

## Technology Stack
* AWS ECS Fargate: Container runtime selected to eliminate Kubernetes control-plane operational overhead for a 3-engineer team
* AWS ALB / gRPC over TLS: Low-latency transport protocol ensuring P99 decision latency under 50 ms
* Amazon Aurora Serverless v2 (PostgreSQL): Transactional database for case management and rule metadata within budget constraints
* AWS ElastiCache (Redis): In-memory data store for feature stores and fallback circuit-breaking ensuring 1-minute availability recovery
* AWS S3 Object Lock & KMS: WORM storage providing tamper-evident 7-year auditability

## Rationale
This architecture uses managed serverless and container primitives on AWS to achieve sub-50ms latency and strict PCI-DSS compliance without exceeding the 25,000 EUR monthly budget. The lean stack minimizes operational overhead, enabling a three-engineer team to operate the system reliably.