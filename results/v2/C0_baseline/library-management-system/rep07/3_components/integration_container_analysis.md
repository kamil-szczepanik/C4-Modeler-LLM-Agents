## Overview
- Solution: Library Management System for public and academic libraries to catalogue items and manage circulation.
- Core Purpose: Manages external APIs, third-party digital content ingestion, and secure payment processing within EU data residency constraints.

## Key Elements
- Integration Container (Node.js/TypeScript)
- Webhook Handler Component (Node.js/Express)
- Vendor Ingestion Service (Node.js/TypeScript with Zod)
- Outbox Dispatcher Component
- Audit Logging Component (Node.js/Winston or Pino)
- Third-Party Vendors / Digital Content Providers
- EU Payment Gateway
- Async Event Broker (Apache Kafka/RabbitMQ)
- Core Domain Container (PostgreSQL, EU-hosted)

## Relationships
- Third-Party Vendors -> Vendor Ingestion Service: Ingests digital content [HTTPS / SFTP with TLS 1.3]
- EU Payment Gateway -> Webhook Handler Component: Sends secure financial webhooks [HTTPS with HMAC verification]
- Outbox Dispatcher -> Async Event Broker: Publishes events reliably [SASL/SCRAM, mTLS]
- Audit Logging Component -> Core Domain Container: Persists immutable audit trails [gRPC/REST over TLS within EU-isolated VPC]
- Kubernetes NetworkPolicies: Enforces egress allowlisting to authorized payment gateways and vendors only

## Technology Stack
- Node.js & TypeScript: Chosen for asynchronous I/O performance in integration workloads
- Zod: Provides strict schema validation for untrusted external payloads
- Kubernetes & HPA: Enables proactive scaling based on event broker queue depth and SFTP payload volume
- OpenTelemetry: Implements end-to-end distributed tracing across components
- Secrets Manager: Injects API keys and SFTP private keys securely without environment variables

## Rationale
- Decomposing the Integration Container into isolated components satisfies the 5-minute digital content ingestion SLA and ensures resilience against transient gateway timeouts.
- Mandatory cryptographic verification, strict network egress rules, and EU-hosted audit logging enforce required data residency and financial security constraints.