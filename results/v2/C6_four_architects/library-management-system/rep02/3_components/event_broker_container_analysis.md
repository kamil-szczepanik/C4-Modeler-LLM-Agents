## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals for academic and public libraries. It uses a decoupled event-driven architecture to meet strict EU-only data residency and sub-800ms search performance requirements.

## Key Elements
- **Event Broker Container:** Central Apache Kafka container with KRaft-based broker storage.
- **Event Ingestion Engine:** Java/JVM Kafka broker component handling writes with EU node partition replication.
- **Topic Routing & Schema Registry:** Confluent Schema Registry enforcing Avro/JSON schemas.
- **Stream Processing / Consumer Group Manager:** Kafka Connect / KStreams managing asynchronous event consumption.
- **DLQ Manager:** Kafka Topic & Consumer Router capturing poisoned messages.
- **Broker Metrics & Health Monitor:** Prometheus JMX Exporter tracking consumer lag.
- **Access Control & mTLS Gateway:** Kafka Authorizer enforcing mutual TLS and ACLs.

## Relationships
- **Core Services Container -> Access Control & mTLS Gateway:** Authenticates and connects securely [mTLS / Kafka Protocol]
- **Access Control & mTLS Gateway -> Event Ingestion Engine:** Forwards authorized message streams [Internal TCP]
- **Event Ingestion Engine -> Topic Routing & Schema Registry:** Validates event schemas [HTTP/REST over TLS]
- **Event Ingestion Engine -> Search Service Container:** Streams change data capture [Kafka Protocol over TLS]
- **Stream Processing / Consumer Group Manager -> Background Worker Container:** Dispatches asynchronous background jobs [Kafka Protocol over TLS]
- **Stream Processing / Consumer Group Manager -> DLQ Manager:** Routes failed messages after max retry exhaustion [Internal Kafka routing]
- **DLQ Manager -> Background Worker Container:** Forwards failed events for manual inspection [Kafka Protocol over TLS]
- **Stream Processing / Consumer Group Manager -> Broker Metrics & Health Monitor:** Reports consumer lag [JMX / Prometheus scrape over TLS]

## Technology Stack
- **Apache Kafka (KRaft mode):** Provides ZooKeeper-free event broker storage within EU data boundaries.
- **Confluent Schema Registry:** Enforces strict event contract compatibility.
- **Prometheus JMX Exporter:** Monitors consumer lag to ensure <800ms search latency compliance.
- **mTLS & Kafka ACLs:** Secures inter-container transport and topic access.

## Rationale
This architecture uses KRaft-based Apache Kafka and rigorous access controls to enforce EU data residency. Dedicated streaming, monitoring, and DLQ components guarantee the high reliability and low latency required for search performance.