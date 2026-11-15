## Overview
The Scheduling & Billing Service manages resource clash checks, appointment scheduling, billing, insurance claims, and automated patient reminders for the Clinic Management System. It operates within a hybrid cloud architecture (`on-prem-k8s` and `eu-central-1`) to serve patients, clinicians, and billing staff.

## Key Elements
- Appointment Scheduler Component (NestJS / TypeScript)
- Billing & Claims Processor Component (NestJS / TypeScript)
- Notification Handler Component (NestJS / TypeScript)
- Data Access & Encryption Component (TypeORM / AES-256)
- Redis Cluster (Multi-node with automatic failover)
- PostgreSQL (Shared database with Outbox table and row-level security)
- Payment Gateway / Insurance Clearinghouse (External System)
- External Notification Service (External System)

## Relationships
- Appointment Scheduler Component -> Redis Cluster: Acquires distributed locks via Redlock [TCP/TLS]
- Appointment Scheduler Component -> PostgreSQL (Outbox Table): Persists transactional events [TypeORM / TCP]
- Billing & Claims Processor Component -> PostgreSQL: Utilizes transactional outbox table for claim dispatch [TypeORM / TCP]
- Billing & Claims Processor Component -> Payment Gateway / Insurance Clearinghouse: Submits claims and processes payments [HTTPS/REST with mTLS]
- Billing & Claims Processor Component -> Patient Self-Service Portal: Exposes itemized billing data [gRPC/REST]
- Notification Handler Component -> External Notification Service: Dispatches scrubbed reminders [HTTPS/REST]
- Notification Handler Component -> Redis/PostgreSQL: Utilizes durable local queue for retry logic [TCP/TLS]

## Technology Stack
- Node.js / NestJS: Chosen for modular, asynchronous backend service development.
- Redis Cluster: Selected for high-availability distributed locking and resilient retry queues.
- PostgreSQL with TypeORM: Used for transactional data persistence and outbox pattern implementation.
- AES-256 & mTLS: Enforced for application-layer encryption at rest and secure transport.
- Istio Service Mesh: Deployed for gRPC traffic routing and JWT token validation.

## Rationale
This architecture ensures 99.99% high availability and HIPAA/GDPR compliance through decentralized resilience, outbox patterns, and encrypted storage. It balances rapid patient self-service workflows with robust administrative controls across hybrid deployments.