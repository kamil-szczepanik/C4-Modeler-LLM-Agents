## Overview
[Real-time Payment Fraud Screening Platform: Screens card-not-present payment authorizations for fraud in real-time, and provides case management for fraud analysts reviewing suspicious payments.]

## Key Elements
- Fraud Scoring API (Go)
- Case Management Backend (Node.js)
- Case Management UI (React)
- Audit & Event Store (AWS Aurora PostgreSQL)
- Payment Gateway / Processor Core
- Identity Provider (IdP)

## Relationships
- Payment Gateway / Processor Core -> Fraud Scoring API (gRPC / mTLS)
- Fraud Analyst -> Case Management UI (HTTPS / OIDC)
- Fraud Scoring API -> Audit & Event Store (TCP/TLS)
- Case Management Backend -> Audit & Event Store (TCP/TLS)
- Case Management UI -> Case Management Backend (HTTPS)

## Technology Stack
- Go: Embedded ONNX runtime for sub-millisecond fraud scoring latency
- Node.js & React: Streamlined case management workflows for fraud analysts
- AWS Aurora PostgreSQL: Tamper-evident, 7-year append-only audit data retention
- AWS ECS Fargate: Container orchestration within the 25,000 EUR monthly budget
- AWS KMS & Secrets Manager: PCI-DSS Level 1 encryption and secret management

## Rationale
[Embedding ONNX directly into the Go-based Fraud Scoring API eliminates network hops to meet the strict 50ms P99 latency requirement while reducing operational overhead for a three-engineer team. Furthermore, utilizing AWS managed services ensures PCI-DSS Level 1 compliance and immutable 7-year auditability within the fixed budget.]