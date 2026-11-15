## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations to prevent fraud while enabling analysts to review suspicious transactions. It ensures compliance, low-latency processing, and high availability within strict budget constraints.

## Key Elements
- **Payment Gateway:** External upstream system submitting authorizations
- **Fraud Analyst & Risk Manager:** Internal users handling case management and rule updates
- **Compliance Auditor:** External user accessing audit logs
- **Tokenization / Vault Service:** External system handling card data
- **AWS API Gateway / ALB:** Edge proxy for ingress, rate limiting, and circuit-breaking
- **Core Scoring Engine:** Containerized service handling real-time evaluations
- **AWS CloudWatch:** Telemetry, audit logging, and observability service

## Relationships
- **Payment Gateway -> AWS API Gateway / ALB:** Submits authorizations via synchronous gRPC/HTTPS
- **AWS API Gateway -> Core Scoring Engine:** Forwards screened payloads via gRPC
- **Fraud Analyst -> Case Management UI:** Reviews suspicious transactions via HTTPS
- **Core Scoring Engine -> Tokenization / Vault Service:** Queries masked/tokenized data via mutual TLS (mTLS)
- **Core Scoring Engine -> AWS CloudWatch:** Exports tamper-evident logs via OpenTelemetry

## Technology Stack
- **Compute:** AWS ECS/EKS with automated canary deployments to support zero-downtime model updates within the 3-engineer capacity
- **Languages:** Java/Go for high-throughput, low-latency scoring services
- **Protocols:** gRPC for internal low-latency communication; HTTPS/TLS for external interfaces and UI access
- **Security:** AWS KMS and centralized logging for 7-year tamper-evident auditability and PCI-DSS Level 1 compliance

## Rationale
This architecture uses fully managed AWS services and containerization to maintain high availability and sub-50ms P99 latency at 3,000 TPS within a €25,000 monthly budget. It strictly bounds the PCI-DSS scope by delegating card vaulting while ensuring complete auditability for a three-engineer team.