## Overview
The Library Management System provides cataloging, circulation, and self-service portals for academic and public libraries. It uses an event-driven architecture enforcing EU-only data residency and sub-800ms search responses.

## Key Elements
- Library Patrons, Librarians / Circulation Staff, Library Administrators
- Web Application (React, TypeScript, Nginx)
- API Gateway (Spring Cloud Gateway, Java)
- Core Services Container (Spring Boot, Java)
- Search Container (Elasticsearch / OpenSearch)
- PostgreSQL (AWS RDS EU)
- Message Broker (Apache Kafka / RabbitMQ)
- Event Bus (Kafka Cluster)
- Access Control Manager
- Schema Registry (Confluent Schema Registry / Apicurio Registry)
- DLQ Handler (Kafka Consumer Group + Storage)

## Relationships
- Core Services Container -> Event Bus: Produces and consumes domain events [Kafka Protocol with mTLS/SASL]
- Core Services Container -> Schema Registry: Validates event structure [HTTP/REST]
- Core Services Container -> Access Control Manager: Authenticates and authorizes connections [SASL/SCRAM over TLS]
- Event Bus -> DLQ Handler: Forwards unacknowledged/failed messages after max retries [Kafka Protocol]

## Technology Stack
- Apache Kafka: Handles high-throughput asynchronous event streaming
- AES-256: Encrypts data at rest across event storage volumes and DLQ topics
- mTLS and SASL/SCRAM: Secures cluster transport and authenticates clients
- Confluent Schema Registry / Apicurio Registry: Enforces schema evolution and regex-based PII sanitization

## Rationale
This architecture guarantees high availability and sub-800ms search performance through asynchronous event handling. Strict EU data residency and privacy mandates are met via localized AWS hosting, AES-256 encryption, zero-PII payloads, and rigorous topic-level ACLs.