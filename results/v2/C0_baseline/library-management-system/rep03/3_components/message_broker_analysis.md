## Overview
[The system is an event-driven Library Management System utilizing a resilient, secure message broker for cataloging, circulation, and self-service portals. Its core purpose is to handle asynchronous domain events while guaranteeing EU data residency and strict performance SLAs.]

## Key Elements
- Apache Kafka (Event Router / Broker Core)
- Confluent Schema Registry / Apicurio (Schema Registry)
- Apache Kafka DLQ Topics (Dead-Letter Queue)
- Kafka-UI / Custom Admin CLI (Event Replay & Administration Tooling)
- Strimzi Kubernetes Operator
- HashiCorp Vault

## Relationships
- Core Business Service -> Event Router: Publishes raw domain events [gRPC / Kafka Protocol]
- Integration Service -> DLQ Topic: Routes failed consumption events [Kafka Protocol]
- Event Replay Tool -> Event Router: Re-publishes corrected events from DLQ [Kafka Protocol]
- Notification & Audit Service -> Event Router: Consumes sanitized events [Kafka Consumer API]

## Technology Stack
- Apache Kafka: Distributed event streaming platform chosen for high throughput and horizontal scalability.
- Strimzi: Kubernetes operator selected for automated, resilient broker deployments across availability zones.
- HashiCorp Vault: Centralized secret management for mTLS certificates, RBAC, and encryption keys.
- TLS 1.3 / mTLS: Protocol standards enforced for secure in-transit data protection.

## Rationale
[This architecture uses managed Kafka infrastructure with native security controls and automated DLQ retries to protect the 800ms performance SLA. It strictly enforces EU data residency and GDPR compliance via strict topic isolation, encryption at rest, and pii masking.]