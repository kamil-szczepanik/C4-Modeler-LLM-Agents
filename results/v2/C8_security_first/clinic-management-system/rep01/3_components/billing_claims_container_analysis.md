## Overview
The Clinic Management System is a resilient, hybrid-cloud platform designed to automate patient admissions, clinical workflows, and financial operations for healthcare providers. It ensures high availability, strict compliance, and seamless interoperability for medium-sized hospitals and clinics.

## Key Elements
- Envoy / NGINX API Gateway
- Billing & Claims Container (Node.js / TypeScript)
- Primary Database (PostgreSQL with Citus)
- Event Broker (Redpanda)
- External Insurance Claim Processors / Payment Gateways
- Scheduling Engine Container (Java / Spring Boot)
- Internal Components: API Controller, Claims & Invoicing Engine, Denial & Exception Handler, Payment & Clearinghouse Adapter, Outbox Processor, Fee Estimation Service, Audit & Event Publisher, Data Access Layer

## Relationships
- Envoy / NGINX API Gateway -> Billing & Claims Container: Routes billing requests [HTTP/2 / gRPC over mTLS]
- Billing & Claims Container -> Primary Database: Executes encrypted database transactions [Encrypted internal TCP]
- Billing & Claims Container -> Redpanda: Publishes domain events and handles DLQ queues [Encrypted internal TCP]
- Billing & Claims Container -> Insurance Claim Processors / Payment Gateways: Submits claims and processes payments [TLS 1.3 over HTTPS]
- Scheduling Engine Container -> Billing & Claims Container: Fetches real-time fee estimates [gRPC]

## Technology Stack
- Node.js / TypeScript: Selected for the Billing & Claims Container to ensure rapid development and robust asynchronous IO processing.
- PostgreSQL with Citus: Provides scalable, distributed relational storage for structured financial and patient data.
- Redpanda: Handles event streaming with high throughput and low latency for asynchronous communication.
- HashiCorp Vault: Secures sensitive credentials, API keys, and mTLS certificates via a CSI Secret Store provider.
- OpenTelemetry & Prometheus: Powers distributed tracing and SLO-based monitoring for 99.99% uptime.

## Rationale
This architecture uses an active-active hybrid cloud deployment combined with an outbox pattern to guarantee transactional integrity and 99.99% availability. Application-layer encryption, strict RBAC/ABAC controls, and TLS 1.3 ensure comprehensive HIPAA and GDPR compliance for sensitive financial data.