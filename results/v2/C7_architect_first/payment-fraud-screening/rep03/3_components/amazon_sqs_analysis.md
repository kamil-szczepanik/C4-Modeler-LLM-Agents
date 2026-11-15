## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and manages suspicious payment reviews for a mid-size payment processor.]

## Key Elements
- Fraud Scoring Engine
- Case Management API & UI
- Amazon SQS (Standard Queue with DLQ)
- AWS KMS (Key Management Service)
- AWS VPC Endpoints (PrivateLink)
- AWS CloudTrail and CloudWatch

## Relationships
- Fraud Scoring Engine -> Amazon SQS Ingestion Interface: Sends asynchronous case messages via HTTPS (TLS 1.3, SigV4, AWS SDK)
- Amazon SQS Polling & Dispatcher -> Case Management API & UI: Delivers asynchronous cases via HTTPS Long-Polling
- Amazon SQS -> AWS KMS: Encrypts and decrypts message payloads at rest via customer-managed keys
- Amazon SQS -> AWS CloudTrail & CloudWatch: Streams audit logs and operational metrics

## Technology Stack
- Amazon SQS (Standard): Chosen over FIFO to avoid throughput bottlenecks and maintain high availability at 3,000 req/sec
- AWS KMS: Implemented with server-side encryption and annual rotation for PCI-DSS Level 1 compliance
- AWS VPC Endpoints (PrivateLink): Secures data transport without traversing the public internet
- Terraform: Manages infrastructure deployment within the 25,000 EUR monthly budget

## Rationale
[This architecture satisfies PCI-DSS Level 1 compliance and sub-50ms decision performance constraints while remaining easily operable by a three-engineer team. Utilizing managed AWS services like Standard SQS and KMS ensures robust security, tamper-evident auditability, and scalability within a fixed monthly budget.]