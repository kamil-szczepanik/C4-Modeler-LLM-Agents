## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals for libraries. The Analytics Worker container processes asynchronous business events to generate operational metrics for administrators.

## Key Elements
- **Users**: Library Member (Patron), Librarian / Library Staff, Library Administrator
- **External Systems**: Payment Gateway, Digital Content Providers, Notification System
- **Containers**: Web Application (React/TypeScript SPA), API Gateway (NGINX / Spring Cloud Gateway), Core Business Services (Spring Boot), Search Engine (Elasticsearch / OpenSearch), Database (PostgreSQL managed service, EU-hosted), Analytics Worker (Python/Spring + Apache Kafka/RabbitMQ)
- **Analytics Worker Components**: Event Consumer Component, Aggregation Engine Component, Analytics Datastore Writer Component

## Relationships
- **Core Business Services -> Event Consumer**: Streams business events [Apache Kafka with mTLS and SASL/SCRAM]
- **Event Consumer -> Aggregation Engine**: Passes validated event payloads [In-memory]
- **Aggregation Engine -> Analytics Datastore Writer**: Transfers structured metric payloads [In-memory / Method Call]
- **Analytics Datastore Writer -> Database**: Persists aggregated reporting metrics [SQL/TLS 1.3, EU-hosted, restricted least-privilege role]

## Technology Stack
- **Python / Spring Boot**: Powers the Analytics Worker components for high-throughput event processing.
- **Apache Kafka**: Manages event streaming with Apache Avro schema validation and Schema Registry.
- **PostgreSQL**: Stores aggregated metrics with transparent data encryption (TDE), TLS 1.3, and least-privilege `INSERT` permissions.
- **HashiCorp Vault / Cloud Secret Manager**: Dynamically injects runtime secrets and Kafka mTLS certificates.

## Rationale
The asynchronous event-driven architecture using Kafka decouples analytics processing from core transactional paths, ensuring high search performance under 800 ms. Strict isolation and least-privilege database access enforce EU data residency constraints and protect patron PII.