## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMRs, scheduling, and billing for clinics. The Billing & Claims component automates financial workflows, insurance claims, and self-service payments.

## Key Elements
- Billing Specialist & Patient (Users)
- Billing & Claims Container (Kubernetes, Encrypted Distributed Storage)
- External Clearinghouses & Payment Gateways
- EMR Container & Patient Portal Container
- HashiCorp Vault & Apache Kafka / RabbitMQ

## Relationships
- Billing Specialist -> Billing & Claims: Manages financial workflows via HTTPS (TLS 1.3), OAuth2/OIDC MFA
- Patient -> Billing & Claims: Accesses itemized billing via REST API with OAuth2 scopes
- Billing & Claims -> EMR: Accesses encounter data via gRPC / REST using mTLS
- Billing & Claims -> External Clearinghouses: Submits insurance claims via mTLS and asynchronous messaging

## Technology Stack
- Kubernetes: Container orchestration for active-active high availability (99.99%)
- Encrypted Distributed Storage: Ensures AES-256 data at rest compliance
- Apache Kafka / RabbitMQ: Queue-based load leveling for asynchronous claim submissions
- HashiCorp Vault: Dynamic database credential rotation and secret management
- OAuth2/OIDC: Fine-grained RBAC and ABAC access control

## Rationale
Active-active Kubernetes clustering across on-premise and AWS `eu-central-1` ensures 99.99% availability and zero financial data loss. End-to-end encryption, mTLS, and immutable audit logs satisfy strict HIPAA and GDPR compliance mandates.