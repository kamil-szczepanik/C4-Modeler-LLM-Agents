## Overview
The Real-Time Payment Fraud Screening System processes card-not-present payment authorizations to detect fraud within a sub-50ms latency window while providing case management for analysts. It ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a strict budget and team size.

## Key Elements
- Cardholders / Merchants: External entities initiating transactions indirectly.
- Payment Gateway / Acquirer: External system sending authorization requests via REST/gRPC.
- Fraud Analysts & Risk Managers: Internal users accessing the system for case reviews and rule updates.
- Real-Time Payment Fraud Screening System: Core software system processing scores, rules, and audit logs.
- AWS ECS on Fargate: Container platform hosting the hot-path scoring engine.
- AWS QLDB / S3 Object Lock: Storage for tamper-evident audit logs.
- AWS Cognito: Identity provider handling OAuth2/OIDC and MFA.

## Relationships
- Payment Gateway to Real-Time Payment Fraud Screening System: Sends synchronous authorization requests using gRPC/HTTPS over mTLS.
- Fraud Analysts to Real-Time Payment Fraud Screening System: Accesses case management via HTTPS (TLS 1.3).
- Real-Time Payment Fraud Screening System to AWS QLDB / S3: Streams asynchronous audit logs for tamper-evident retention.
- Fraud Screening System to AWS ECS / Fargate: Executes scalable scoring containers for low-latency decisions.

## Technology Stack
- AWS ECS on Fargate: Chosen for containerized scalability supporting 3,000 TPS within the €25k/month budget.
- gRPC / HTTPS: Ensures high-throughput, low-latency communication satisfying the <50ms P99 performance SLA.
- AWS QLDB / S3 Object Lock: Implemented to guarantee tamper-evident, cryptographically verifiable 7-year audit retention.
- AWS Cognito & IAM: Enforces OAuth2/OIDC authentication and strict RBAC to isolate PCI-DSS boundaries.
- Terraform: Utilized for Infrastructure as Code to maintain immutable infrastructure and automated deployments.

## Rationale
This architecture balances strict sub-50ms latency and PCI-DSS compliance requirements by decoupling heavy audit logging from the synchronous hot path. Leveraging managed AWS services ensures high availability and fail-open resilience while remaining within the fixed €25k monthly budget and 3-engineer operational capacity.