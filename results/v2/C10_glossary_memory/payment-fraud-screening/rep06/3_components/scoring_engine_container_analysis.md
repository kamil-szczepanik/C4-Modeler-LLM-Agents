## Overview
- Real-Time Payment Fraud Screening System screens card-not-present payment authorizations at 3,000 TPS to protect merchant revenue while supporting case reviews and compliance, ensuring sub-50ms P99 latency.
- Built on AWS ECS Fargate in eu-west-1, the architecture processes transactions securely while strictly adhering to PCI-DSS Level 1 compliance and a 25,000 EUR monthly budget.

## Key Elements
- Payment Gateway / Core Processing System
- External Cardholder Data Environment (CDE) / Tokenization Vault
- AWS S3 Object Lock
- Dynamic Rule & Model Registry
- Scoring Engine Container (Rust / Tokio, AWS ECS Fargate)
- Case Management Container (Node.js / TypeScript, AWS ECS Fargate)
- Fallback Scoring Container (Python / FastAPI, AWS ECS Fargate)
- Audit Reporting Container (Node.js / TypeScript, AWS ECS Fargate)
- API Ingress Component (Rust / Tonic gRPC)
- Token Resolution Component (Rust / Reqwest)
- Rule & Model Execution Component (Rust / Native Eval)
- Audit Dispatcher Component (Rust / Tokio async channel)
- Circuit Breaker & Fallback Coordinator Component (Rust / custom Tokio-native wrapper)

## Relationships
- Payment Gateway / Core Processing System -> Scoring Engine Container: Sends payment authorization requests [gRPC/REST over TLS 1.3 with mTLS and OAuth2/JWT]
- Scoring Engine Container -> External Cardholder Data Environment (CDE) / Tokenization Vault: Resolves tokens securely [Secure APIs]
- Scoring Engine Container -> Dynamic Rule & Model Registry: Cryptographically validates and hot-loads signed rules [AWS KMS and ECDSA P-256]
- Scoring Engine Container -> AWS S3 Object Lock: Writes decision inputs, model versions, and explanations [AWS Firehose / S3 API]
- Scoring Engine Container -> Fallback Scoring Container: Routes to fallback during primary outages [Internal HTTP/JSON via AWS Service Discovery]

## Technology Stack
- Rust / Tokio: Selected for Scoring Engine Container to deliver sub-50ms P99 latency at 3,000 TPS with memory safety.
- AWS ECS Fargate: Provides container orchestration with predictable scaling and fixed infrastructure budgeting.
- AWS KMS & ECDSA P-256: Ensures cryptographic validation for zero-downtime hot-loaded fraud rules.
- AWS S3 Object Lock: Guarantees tamper-evident, WORM-compliant 7-year audit retention.
- Node.js / TypeScript: Powers Case Management and Audit Reporting containers for rapid administrative development.

## Rationale
- The Rust-based Scoring Engine combined with non-blocking async channels guarantees performance, latency, and memory safety under high transaction loads.
- AWS-managed services and strict compliance controls securely satisfy PCI-DSS Level 1, 7-year auditability, and budgetary limits.