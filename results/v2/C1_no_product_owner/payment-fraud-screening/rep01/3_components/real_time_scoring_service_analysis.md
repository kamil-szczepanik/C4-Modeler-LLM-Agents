## Overview
This system provides real-time fraud screening for card-not-present payment authorizations, ensuring secure evaluation, compliance, and case management for financial analysts. It processes high-throughput transactions while maintaining strict auditability and low-latency availability.

## Key Elements
- API Handler Component (Go `net/http` + `grpc`)
- Token Resolution Client Component (Go `net/http`)
- Feature Store Cache Component (Embedded Go LRU Cache / Redis Client)
- Scoring Engine Component (Go WebAssembly / ONNX runtime)
- Audit & Event Dispatcher Component (Go AWS SDK)
- Circuit Breaker / Fallback Component (Go `gobreaker`)

## Relationships
- API Gateway & Routing Layer -> API Handler Component: Forwards low-latency evaluation requests [gRPC]
- Token Resolution Client Component -> Card Networks & Tokenization Vault: Fetches tokenized attributes [mTLS / HTTPS]
- Audit & Event Dispatcher Component -> Amazon DynamoDB: Writes immutable decision payloads and audit logs [AWS KMS / DynamoDB API]
- Scoring Engine Component -> Model Training Environment: Ingests signed model artifacts [AWS Signer / KMS]

## Technology Stack
- Go: Chosen for high-throughput, low-latency execution fitting the 50ms P99 requirement.
- Amazon ECS on EC2: Provides predictable CPU performance and cost control within the 25,000 EUR/month budget.
- ONNX Runtime: Executes lightweight machine learning models in-memory without Python runtime overhead.
- AWS KMS: Secures encryption keys, token data, and cryptographic audit signature chains.

## Rationale
This architecture uses Go microservices deployed on Amazon ECS on EC2 to guarantee the required 50ms P99 latency at 3,000 TPS. Integrated cryptographic controls and immutable audit trails satisfy strict PCI-DSS Level 1 compliance and 7-year auditability mandates within budget.