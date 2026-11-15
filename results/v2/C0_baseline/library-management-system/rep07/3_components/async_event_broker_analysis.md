## Overview
[A resilient Library Management System providing cataloging, circulation, and self-service portals for public and academic libraries. Built with strict EU-only data residency guarantees.]

## Key Elements
* Apache Kafka (Async Event Broker container, deployed via Strimzi operator across 3 EU availability zones)
* KRaft Metadata Quorum (Replaces ZooKeeper for broker state management)
* Confluent Schema Registry (Co-located within Strimzi footprint for Avro schema validation)
* Core Domain Container (Java/Spring Boot, PostgreSQL, publishes domain events)
* Integration Container (Node.js/TypeScript, consumes events asynchronously with DLQs)
* HashiCorp Vault / Kubernetes Secrets (Dynamic credential rotation)

## Relationships
* Core Domain Container -> Apache Kafka: Publishes domain events via [mTLS, SASL/SCRAM-512]
* Integration Container -> Apache Kafka: Consumes events and reads DLQs via [mTLS, SASL/SCRAM-512]
* Apache Kafka -> Apache Kafka: Inter-broker communication secured via [Internal mTLS]
* Strimzi Operator -> Apache Kafka: Manages deployment and KRaft consensus

## Technology Stack
* Apache Kafka: Append-only log architecture chosen for event sourcing and partition-level ordering.
* Strimzi Operator: Kubernetes operator for automated multi-AZ broker deployment and lifecycle management.
* KRaft: Eliminates ZooKeeper to reduce operational complexity and failure modes.
* Avro / Confluent Schema Registry: Co-located to enforce contract compatibility without excessive SRE overhead.
* mTLS & SASL/SCRAM-512: Mandated for all client-broker and inter-broker authentication/encryption.
* LUKS: Persistent volume encryption protecting EU data at rest.

## Rationale
[This event-driven architecture decouples heavy third-party integrations and notifications from core cataloging, ensuring high availability and compliance with the 99th-percentile search response SLA (<800 ms). Strict security, encryption, and partitioning enforce EU data residency and GDPR mandates.]