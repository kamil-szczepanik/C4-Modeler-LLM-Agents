## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for libraries while strictly enforcing EU data residency. The architecture uses an asynchronous messaging backbone to decouple heavy backend workflows and maintain sub-second search responsiveness.

## Key Elements
- **Integration/Messaging Container**: Apache Kafka cluster (EU-hosted)
- **Topics**: `circulation.events`, `catalog.events`, `circulation.dlq` (Dead-Letter Queue)
- **Producers**: Staff Management API
- **Consumers**: Search Engine, Notification Dispatcher (Go/Worker service)
- **Monitoring & Compliance**: Observability Platform & SIEM

## Relationships
- `Staff Management API` -> `Integration/Messaging Container`: Produces domain events [Kafka TCP binary protocol, mTLS, SASL/SCRAM-512]
- `Integration/Messaging Container` -> `Notification Dispatcher`: Consumes notification events [Kafka Consumer Group, TCP, mTLS]
- `Integration/Messaging Container` -> `Search Engine`: Feeds catalogue updates [Kafka Connect Sink connector, TCP]
- `Integration/Messaging Container` (`circulation.dlq`) -> `Staff Management API`: Exposes manual resolution interface [HTTP REST]

## Technology Stack
- **Apache Kafka**: Standardized as the sole broker to eliminate operational complexity and handle high-throughput domain events.
- **TLS 1.3 & mTLS**: Secures all client-to-broker and inter-broker communication in transit.
- **SASL/SCRAM-512**: Provides strong client identity authentication.
- **AES-256**: Encrypts all persistent storage volumes at rest.
- **Kafka Connect**: Integrates asynchronous catalogue updates into the search index.

## Rationale
Standardizing on a single EU-hosted Apache Kafka cluster minimizes operational overhead and attack surfaces while strictly enforcing EU data residency constraints. Implementing Kafka consumer groups, exponential backoff retries, and a dedicated Dead-Letter Queue ensures high availability, fault tolerance, and strict compliance with the 2-second event delivery SLA.