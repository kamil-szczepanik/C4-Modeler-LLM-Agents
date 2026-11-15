## Overview
The Library Management System provides item cataloguing, circulation management, and self-service portals for public and academic libraries. It utilizes an asynchronous event-driven architecture to decouple core workflows and guarantee EU-only data residency.

## Key Elements
* Library Patrons (Members) & Librarians
* Patron Portal (React.js SPA) & Librarian Back-office (Next.js Web App)
* API Gateway (NGINX / Envoy)
* Catalogue Service (Java / Spring Boot) & Circulation Service (Node.js / Express)
* Event Broker (Apache Kafka / Confluent Platform, EU-hosted)
* PostgreSQL Database (EU-hosted) & Elasticsearch (EU-hosted)
* Schema Registry & Kafka Streams PII Tokenization App
* Tiered Storage Manager (EU-hosted S3-compatible storage)

## Relationships
* Catalogue Service -> Event Broker: Publishes cataloguing events [mTLS, SASL/SCRAM, TLS-encrypted streams]
* Circulation Service -> Event Broker: Publishes check-out workflows [mTLS, SASL/SCRAM, TLS-encrypted streams]
* Kafka Topics -> Schema Registry: Validates payload schemas on ingestion [HTTPS]
* Kafka Streams -> Elasticsearch: Streams masked projections [Kafka Connect, TLS]
* Event Broker -> Tiered Storage Manager: Offloads historical segments [Encrypted storage]

## Technology Stack
* Apache Kafka: Log-based architecture for replayability, partitioning, and EU data residency.
* Schema Registry: Enforces Avro/Protobuf schemas for backward compatibility and security.
* Kafka Streams: Performs real-time PII tokenization and data masking for GDPR compliance.
* Elasticsearch: Delivers 99th-percentile search response times under 800 ms.
* mTLS & SASL/SCRAM: Secures client connections and enforces topic-level ACLs.

## Rationale
This architecture uses Apache Kafka with strict security and data-masking controls to decouple high-throughput workflows while strictly adhering to EU data residency mandates. The tiered storage and indexing components ensure high-performance self-service operations and rapid search retrieval.