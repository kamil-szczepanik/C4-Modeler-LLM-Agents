## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations to prevent fraud and provides a case management workflow for analysts to review suspicious transactions. It ensures strict PCI-DSS Level 1 compliance while maintaining a low-latency infrastructure on AWS.

## Key Elements
- Fraud Analyst, Compliance Officer / Auditor, Cardholder
- Payment Gateway, Identity Provider (IdP), AWS S3
- Case Management API (Go, Node.js/TypeScript, AWS ECS Fargate)
- Case Controller Component
- Workflow Service Component
- Audit Logger Component
- Case Metrics / SLA Service Component
- Audit & Event Store (Amazon Aurora with immutable ledgers)

## Relationships
- Analyst Web Application -> Case Controller: Sends API requests [HTTPS/REST with mTLS, OIDC/JWT]
- Case Controller -> Workflow Service: Invokes state transitions [In-process Go function calls]
- Workflow Service -> Audit Logger: Publishes events via transactional outbox pattern
- Audit Logger -> Audit & Event Store: Sends cryptographically signed payloads [TCP/TLS]
- Workflow Service -> AWS Secrets Manager: Retrieves database credentials and cryptographic keys [HTTPS/IAM]

## Technology Stack
- Go: Chosen for low memory footprints, fast compilation, and robust concurrency within the 3-engineer team constraint.
- `chi` Router: Provides lightweight, native HTTP routing for the Case Controller.
- Amazon Aurora (Immutable Ledgers): Stores audit logs in tamper-evident form to meet the 7-year auditability constraint.
- AWS ECS (Fargate): Manages container execution with fixed infrastructure costs under 25,000 EUR per month.
- OpenTelemetry: Propagates distributed tracing across all components for system observability.
- Prometheus: Scrapes internal metrics from the Case Metrics / SLA Service for queue depth and SLA tracking.

## Rationale
This architecture uses lightweight Go containers on AWS ECS to meet strict P99 latency and high throughput requirements on a fixed budget. The modular component design within the Case Management API ensures strict PCI-DSS compliance, robust auditability, and seamless scalability for a three-engineer team.