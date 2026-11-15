## Overview
Real-time payment fraud screening system for card-not-present transactions, ensuring sub-50ms decisions and 7-year tamper-evident auditability. Operated by 3 engineers on AWS under a €25,000/month budget with PCI-DSS Level 1 compliance.

## Key Elements
- **Users**: Fraud Analyst, Risk/Compliance Officer
- **External Systems**: Payment Processor Systems, Identity Provider, Model Registry / Feature Store, Immutable Audit Storage (AWS QLDB / S3 Object Lock)
- **Containers**: AWS API Gateway / Envoy, Scoring Engine Container (Go/Rust, AWS ECS Fargate), Case Management Backend (Node.js/Python, ECS Fargate), Case Management UI (React, AWS S3 + CloudFront), Rule & Model Distribution Service (AWS SQS + S3), Audit Writer Sidecar (Go, ECS Fargate), Amazon ElastiCache (Redis)
- **Components (Audit Writer Sidecar)**: Audit Event Consumer, Tamper-Evident Formatter & Signer (Ed25519/AWS KMS), Immutable Storage Client, DLQ & Metric Forwarder, Local Ring Buffer & Persistence Manager (`mmap`)

## Relationships
- **Scoring Engine** ➔ *(Local IPC / UNIX Domain Socket)* ➔ **Audit Event Consumer** (High-throughput, low-latency)
- **Tamper-Evident Formatter** ➔ *(AWS KMS SDK)* ➔ **AWS KMS** (Envelope encryption)
- **Immutable Storage Client** ➔ *(HTTPS / TLS 1.3)* ➔ **AWS QLDB / S3 Object Lock** (Write-once, append-only)
- **DLQ & Metric Forwarder** ➔ *(AWS SDK)* ➔ **Amazon SQS / CloudWatch**
- **Client UI** ➔ *(HTTPS / TLS 1.3)* ➔ **AWS API Gateway / Envoy**

## Technology Stack
- **AWS ECS Fargate**: Low-maintenance serverless container orchestration fitting the 3-engineer team constraint
- **Go / Rust**: High-performance languages ensuring strict P99 latency < 50ms at 3,000 TPS
- **Amazon ElastiCache (Redis)**: Low-latency feature store for real-time scoring inputs
- **AWS QLDB / S3 Object Lock**: Tamper-evident, append-only storage guaranteeing 7-year regulatory auditability
- **Ed25519 & AWS KMS**: Cryptographic signing and envelope encryption ensuring data security and PCI-DSS Level 1 compliance

## Rationale
Decoupling asynchronous audit logging via a sidecar pattern protects the critical 50ms scoring SLA while guaranteeing strict tamper-evident compliance. Managed AWS services minimize operational overhead for a three-engineer team within a fixed €25,000 monthly budget.