## Overview
This system provides real-time fraud screening for card-not-present payment authorizations to protect transactions before approval while supporting suspicious payment reviews. It processes high-throughput financial transactions securely within strict latency, compliance, and budget constraints.

## Key Elements
- **People**: Merchant / Payment Gateway, Fraud Analyst, Merchant Risk Manager, Compliance Auditor
- **Systems**: Card Schemes / External Enrichment APIs, AWS QLDB / S3 Object Lock
- **Containers**: API Gateway / Tokenization Proxy (Envoy/AWS API Gateway), Real-Time Scoring Engine (Go / AWS ECS on Fargate), Case Management API (Node.js/Java Spring Boot), Audit Log Sitter (Rust), Rule & Model Distribution Service (Python/FastAPI + S3), Event Broker (AWS MSK / Managed Kafka or AWS SQS)

## Relationships
- Merchant / Payment Gateway to API Gateway / Tokenization Proxy via HTTPS (TLS 1.3)
- API Gateway to Real-Time Scoring Engine via gRPC over AWS VPC private subnets with native TLS
- Real-Time Scoring Engine to Event Broker via TCP/TLS
- Event Broker to Audit Log Sitter and Case Management API via TCP/TLS
- Fraud Analyst and Compliance Auditor to Case Management API via HTTPS (OAuth2/OIDC, MFA)

## Technology Stack
- **Compute**: AWS ECS on Fargate with Fargate Spot for cost optimization (fits 25,000 EUR/month budget and 3-person team).
- **Languages**: Go (scoring engine performance), Rust (audit logging), Python/FastAPI (model distribution), Node.js/Java (case management).
- **Security & Networking**: TLS 1.3, AWS VPC Lattice / native TLS, AWS KMS (CMK), AWS Secrets Manager, AWS Private CA.
- **Data & Messaging**: Redis (model caching), AWS MSK or AWS SQS (decoupling), AWS QLDB / S3 Object Lock (tamper-evident audit storage).

## Rationale
The containerized microservices architecture cleanly separates high-performance, stateless real-time scoring from audit and case management, ensuring P99 latency remains below 50 ms at 3,000 TPS. Utilizing managed AWS serverless and container services minimizes operational overhead for a three-engineer team while strictly enforcing PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.