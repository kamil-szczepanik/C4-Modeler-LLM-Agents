## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides a case management interface for fraud analysts. It guarantees sub-50ms P99 decision latency at 3,000 transactions per second while maintaining PCI-DSS Level 1 compliance and a 7-year audit trail.

## Key Elements
- Fraud Analyst / Risk Manager, Merchant Operations Manager, Compliance Officer
- Payment Gateway / Processing Engine, Identity Provider, Payment Card Network / Tokenization Vault, Secure Audit Archive
- API Gateway (Nginx / AWS ALB)
- Fraud Scoring Engine (Java/Quarkus or Go with embedded ONNX Runtime)
- Case Management Service (Node.js / TypeScript)
- Audit & Compliance Ledger (Rust or Go with AWS KMS-backed signing)
- Analytics Export Stream (Fluent Bit sidecar)
- Data Store (AWS Aurora PostgreSQL & Amazon Redis)

## Relationships
- Payment Gateway to API Gateway via HTTPS (REST/JSON)
- API Gateway to Fraud Scoring Engine via gRPC over internal ALB with mTLS
- Fraud Scoring Engine to Redis via TCP (TLS) for feature lookup
- Case Management Service to Identity Provider via OAuth2/OIDC over HTTPS
- Audit & Compliance Ledger to AWS S3 / Glacier via HTTPS (TLS)
- Fluent Bit sidecar to Amazon Athena/S3 via HTTPS

## Technology Stack
- AWS ECS on AWS Fargate: Compute platform for lightweight container deployment within the 25,000 EUR/month budget
- Java/Quarkus or Go with ONNX Runtime: Core scoring engine technology to guarantee sub-50ms P99 latency
- AWS KMS: Asymmetric key generation for cryptographic non-repudiation and tamper-evident audit logging
- Amazon Aurora PostgreSQL & Redis: Relational storage for cases/audit and in-memory storage for low-latency feature stores
- Fluent Bit: Lightweight sidecar for scrubbing PII and streaming anonymized metrics

## Rationale
The architecture combines serverless AWS Fargate containers with low-latency Go/Quarkus runtimes to meet the strict 3,000 TPS and 50ms P99 performance requirements within a fixed 25,000 EUR monthly budget. Security isolations, mTLS, and AWS KMS-backed signing ensure strict PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.