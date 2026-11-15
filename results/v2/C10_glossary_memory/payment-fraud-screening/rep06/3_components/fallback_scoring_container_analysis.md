## Overview
The Real-Time Payment Fraud Screening System evaluates card-not-present payment authorizations at 3,000 TPS to detect fraud while enabling analyst case reviews and compliance auditing. It ensures sub-50ms P99 latency and PCI-DSS Level 1 compliance within a 25,000 EUR monthly AWS budget.

## Key Elements
- Fraud Analyst (Person)
- Risk Manager (Person)
- Compliance & Audit Officer (Person)
- Payment Gateway / Core Processing System (External System)
- External Cardholder Data Environment (CDE) / Tokenization Vault (External System)
- AWS S3 Object Lock (External System)
- Dynamic Rule & Model Registry (External System)
- Scoring Engine Container (Rust / Tokio, AWS ECS Fargate)
- Case Management Container (Node.js / TypeScript, AWS ECS Fargate)
- Fallback Scoring Container (Python / FastAPI, AWS ECS Fargate)
- Audit Reporting Container (Node.js / TypeScript, AWS ECS Fargate)

## Relationships
- Payment Gateway / Core Processing System -> Scoring Engine Container (gRPC/REST over TLS 1.3 with mTLS and OAuth2/JWT)
- Scoring Engine Container -> External Cardholder Data Environment (CDE) / Tokenization Vault (Secure APIs)
- Scoring Engine Container -> Dynamic Rule & Model Registry (AWS KMS and ECDSA P-256)
- Scoring Engine Container -> AWS S3 Object Lock (AWS Firehose / S3 API)
- Scoring Engine Container -> Fallback Scoring Container (HTTPS over mTLS via AWS Service Discovery/App Mesh)
- Fraud Analyst -> Case Management Container (HTTPS Web UI)
- Risk Manager -> Case Management Container (HTTPS Web UI)
- Compliance & Audit Officer -> Audit Reporting Container (HTTPS Web UI)
- Audit Reporting Container -> AWS S3 Object Lock (AWS SDK / S3 API)

## Technology Stack
- AWS ECS Fargate: Container orchestration matching the 25k EUR budget
- Rust / Tokio: High-performance low-latency runtime for the Scoring Engine
- Node.js / TypeScript: Rapid administrative and auditing interface development
- Python / FastAPI: Lightweight heuristic evaluation during primary outages
- AWS S3 Object Lock: WORM storage ensuring 7-year tamper-evident auditability

## Rationale
This architecture uses high-performance Rust for real-time scoring to meet the stringent sub-50ms P99 latency constraint at 3,000 TPS. ECS Fargate and multi-tier containerization ensure strict PCI-DSS Level 1 security, fault-tolerant fallback handling, and robust 7-year auditability within fixed infrastructure budgets.