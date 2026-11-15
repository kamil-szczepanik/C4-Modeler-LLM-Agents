## Overview
This system provides real-time fraud screening for card-not-present payment authorizations, enabling automated approvals, declines, or reviews while maintaining strict PCI-DSS Level 1 compliance. It processes 3,000 transactions per second under a 50 ms P99 latency constraint with a fixed monthly budget of 25,000 EUR.

## Key Elements
* API Gateway / Ingestion Service
* Fraud Scoring Engine
* Case Management API
* Analyst Web Application
* Audit Query API
* Audit & Compliance Portal
* Audit & Event Store (Amazon Aurora)
* AWS ECS (Fargate)

## Relationships
* Payment Gateway to API Gateway via HTTPS/JSON
* API Gateway to internal containers via gRPC with mTLS via AWS VPC security groups and AWS Certificate Manager
* Analyst Web Application and Audit & Compliance Portal to backend APIs via HTTPS with OIDC/JWT authentication
* Fraud Scoring Engine to Audit & Event Store via synchronous cryptographic ledger writes

## Technology Stack
* **Language & Runtime:** Rust for the Fraud Scoring Engine to eliminate garbage collection pauses and meet P99 latency targets; Go, Node.js/TypeScript for other services.
* **Orchestration:** AWS ECS on Fargate to minimize operational overhead for a three-engineer team.
* **Database & Storage:** Amazon Aurora with immutable ledgers for tamper-evident 7-year audit storage; AWS S3 with Object Lock for log archiving.
* **Security & Observability:** AWS Secrets Manager for zero hardcoded secrets; AWS X-Ray for distributed tracing; Resilience4j for circuit breakers.

## Rationale
The architecture uses Rust and ECS Fargate to guarantee deterministic sub-50 ms tail latencies at 3,000 TPS within a strict 25,000 EUR cloud budget. Synchronous ledger writes and strict memory-level tokenization enforce PCI-DSS compliance and 7-year tamper-evident auditability without overburdening the three-engineer operations team.