## Overview
[The system is a Library Management System designed to catalogue items, manage circulation, and provide self-service portals.]
[It uses a secure, event-driven architecture to deliver real-time operational insights while strictly enforcing EU data residency constraints.]

## Key Elements
* Library Patrons, Librarians / Circulation Staff, Library Administrators
* Catalogue Database, External Institutional BI Tools / Municipal Dashboards
* API Gateway (OAuth2/OIDC, JWT)
* Self-Service Portal Container & Circulation Management Container (Kubernetes, Istio)
* Analytics/Reporting Container (Kubernetes, OpenTelemetry)
* Message Broker (Kafka / RabbitMQ, Strimzi operator)
* Schema Registry (Confluent Schema Registry)
* Secret Management (HashiCorp Vault / Kubernetes Secrets Store CSI driver)

## Relationships
* Circulation Management Container -> Message Broker: Publishes events asynchronously [Kafka/RabbitMQ protocol over TLS 1.3 with mTLS & SCRAM-SHA-512]
* Message Broker -> Analytics/Reporting Container: Streams events for analytics [Kafka/RabbitMQ protocol over TLS 1.3]
* Message Broker -> Dead Letter Queue (DLQ): Routes malformed/unprocessable events securely

## Technology Stack
* Kubernetes & Istio: Container orchestration and internal mesh traffic isolation
* Kafka / RabbitMQ (Strimzi): Managed asynchronous event streaming with 3-broker cluster and replication factor of 2
* TLS 1.3 & AES-256: Transport encryption and EU-resident persistent volume encryption
* Confluent Schema Registry: Event schema governance to prevent breaking changes
* HashiCorp Vault: Dynamic mTLS certificate rotation and credential management
* OpenTelemetry: End-to-end event latency tracking and consumer lag monitoring

## Rationale
[This architecture fits requirements by decoupling asynchronous event streaming from core circulation tasks, protecting search performance well under the 800ms NFR.]
[It strictly enforces EU data residency, GDPR pseudonymization, and transport-level security to satisfy compliance mandates while delivering real-time analytics.]