## Overview
The system is a real-time payment fraud screening platform that processes card-not-present payment authorizations and provides case management for fraud analysts. It ensures PCI-DSS Level 1 compliance while maintaining a low-latency, highly available architecture within a fixed infrastructure budget.

## Key Elements
- Fraud Analyst / Compliance Auditor (Users)
- API Gateway / Tokenization Proxy (Envoy / AWS API Gateway)
- Real-Time Scoring Engine (Go / AWS ECS on Fargate, Redis)
- Case Management API (Java Spring Boot 3.x, AWS ECS on Fargate)
- Event Broker (AWS MSK / Managed Kafka)
- Audit Log Sitter (Rust)
- Persistence & Storage (AWS RDS PostgreSQL with AWS KMS, AWS QLDB / S3 Object Lock)

## Relationships
- Fraud Analyst -> Case Management API: Accesses case management workflows, bulk actions, and metrics via HTTPS (OAuth2/OIDC, MFA) [TLS 1.3]
- Compliance Auditor -> Case Management API: Accesses audit and compliance records via HTTPS (OAuth2/OIDC, MFA) [TLS 1.3]
- Event Broker -> Case Management API: Streams review events and case data via TCP/TLS [mTLS]
- Case Management API -> AWS RDS PostgreSQL: Persists case states, SLA tracking, and audit data via JDBC [TLS 1.3]
- Case Management API -> Audit Log Sitter: Sends cryptographically signed action records via TCP/TLS [mTLS]

## Technology Stack
- Java 21 / Spring Boot 3.x: Core framework for the Case Management API, providing enterprise security ecosystems.
- Spring Batch: Handles parallelized batch state transitions for bulk case operations.
- AWS RDS PostgreSQL: Encrypted relational database for case state management, secured with AWS KMS CMK.
- AWS ECS on Fargate: Container orchestration enforcing strict CPU and memory ceilings for the 3-engineer team.
- AWS Secrets Manager: Manages and rotates database credentials and OIDC client secrets every 30 days.

## Rationale
This architecture uses enterprise-grade Java frameworks and AWS managed services to guarantee strict PCI-DSS Level 1 compliance, tamper-evident 7-year auditability, and high availability. It balances robust security controls, automated scaling, and operational simplicity to fit a three-engineer team and a 25,000 EUR monthly budget.