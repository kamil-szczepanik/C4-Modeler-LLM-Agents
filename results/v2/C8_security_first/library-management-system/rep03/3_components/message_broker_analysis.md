## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It uses an asynchronous message broker to decouple services, guarantee event delivery, and meet strict EU data residency constraints.

## Key Elements
*   **Apache Kafka**: Core message broker container deployed as a 3-node multi-AZ cluster.
*   **Ingestion Engine**: Component handling TLS termination, mTLS authentication, and SASL/SCRAM authorization.
*   **Event Log Manager**: Component managing append-only commit logs, 7-day retention, and consumer offsets.
*   **Replication Controller**: Component synchronizing partition replicas across EU nodes.
*   **Circulation & Catalogue Microservice**: Producer of asynchronous circulation events.
*   **Notification Dispatcher**: Consumer of events for alerts and notifications.

## Relationships
*   Circulation & Catalogue Microservice -> Ingestion Engine: Publishes events using SASL_SSL [Kafka Protocol]
*   Ingestion Engine -> Event Log Manager: Appends verified payloads to topic partitions [Internal IPC]
*   Event Log Manager -> Notification Dispatcher: Streams unacknowledged events and routes failures to DLQ [Kafka Protocol]

## Technology Stack
*   **Apache Kafka**: Selected for durable, partitioned commit logs and high-throughput event streaming.
*   **SASL_SSL**: Used for secure producer/consumer transport connections.
*   **AES-256 / LUKS**: Enforces broker-level encryption at rest on EU-hosted storage volumes.
*   **HashiCorp Vault**: Manages automated credential rotation for service accounts.
*   **Prometheus**: Provides metrics for consumer lag, partition saturation, and request latency.

## Rationale
This architecture guarantees at-least-once delivery for critical circulation events while decoupling microservices to protect search performance (<800 ms). Furthermore, it enforces EU-only data residency and high availability through multi-AZ replication and robust security controls.