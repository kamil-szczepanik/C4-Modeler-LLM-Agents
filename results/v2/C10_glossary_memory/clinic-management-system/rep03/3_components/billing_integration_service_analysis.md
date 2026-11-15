## Overview
The Clinic Management System is a hybrid clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It provides secure, highly available clinical and financial services to patients, clinical staff, and administrative users.

## Key Elements
- Billing Specialist
- Hospital Administrator
- Patient
- Billing & Integration Service
- Claim Submission Handler
- Payment Workflow Orchestrator
- Gateway Integration Client
- Financial Ledger & Audit Store
- Billing Notification Trigger
- Payment Gateway
- Notification & Messaging Service

## Relationships
- Billing Specialist -> API Gateway / Reverse Proxy [HTTPS (TLS 1.3) via WAF with risk-based adaptive MFA]
- API Gateway / Reverse Proxy -> Billing & Integration Service [HTTPS / mTLS]
- Claim Submission Handler -> Payment Workflow Orchestrator [Internal Go Channel / gRPC]
- Payment Workflow Orchestrator -> Gateway Integration Client [Internal gRPC]
- Gateway Integration Client -> Payment Gateway [Payment REST APIs over encrypted HTTPS]
- Payment Workflow Orchestrator -> Financial Ledger & Audit Store [Encrypted SQL over mTLS]
- Payment Workflow Orchestrator -> Billing Notification Trigger [Internal Go Channel]
- Billing Notification Trigger -> Notification & Messaging Service [AMQP / Kafka over mTLS]

## Technology Stack
- Go: Powers core handlers and integration clients for high concurrency and performance.
- Temporal.io: Manages stateful, long-running financial retry workflows and sagas.
- Encrypted SQL: Stores immutable transaction and audit logs securely.
- HashiCorp Vault: Supplies ephemeral secrets and dynamic credentials.
- OpenTelemetry & Prometheus: Provides distributed tracing and metrics monitoring.

## Rationale
This architecture uses Temporal.io and Go to guarantee 99.99% uptime and resilient financial workflows for payment retries and claims. Strict security controls, tokenization, and audit logging satisfy HIPAA, GDPR, and PCI-DSS compliance requirements.