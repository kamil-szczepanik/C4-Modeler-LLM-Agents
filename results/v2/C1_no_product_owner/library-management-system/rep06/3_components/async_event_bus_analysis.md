## Overview
The Library Management System provides cataloging, circulation, and self-service portals with strict EU data residency. The Async Event Bus decouples core transactions from search indexing to meet performance goals.

## Key Elements
- Topic Manager (Managed Kafka Topics: `item-events`, `circulation-events`)
- Access Control & Auth Component (Kafka ACLs)
- Schema Registry (Confluent Schema Registry with Avro)
- Event Router / Partition Key Strategist
- Dead Letter Queue (DLQ) & Poison Pill Handler

## Relationships
- Core Domain Service -> Schema Registry: Validates event schemas [HTTP/REST]
- Core Domain Service -> Topic Manager: Publishes partitioned events [Kafka protocol]
- Search Service -> Topic Manager: Consumes ordered event streams [Kafka protocol]

## Technology Stack
- Managed Kafka: Provides scalable EU-hosted event streaming infrastructure
- Confluent Schema Registry: Ensures safe contract evolution and payload-level PII encryption
- SASL/SCRAM-SHA-512 & mTLS: Secures service authentication and data in transit
- Prometheus JMX Exporters: Monitors consumer lag to enforce performance SLAs

## Rationale
This architecture guarantees EU data residency via regional cloud selection while securing PII and operational integrity. Event-driven decoupling protects search performance to satisfy the 800ms response time SLA.