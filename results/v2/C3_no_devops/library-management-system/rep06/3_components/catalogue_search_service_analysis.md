## Overview
The Catalogue & Search Service catalogues physical and digital library items while delivering sub-second search responses for patrons and staff. It processes searches and acquisitions within an EU-compliant cloud environment.

## Key Elements
- Search Controller (Spring MVC)
- Catalogue Manager (Spring Data JPA)
- Index Synchronizer (Spring Integration + Kafka Consumer)
- Analytics Publisher (Spring Cloud Stream)
- Elasticsearch Cluster
- PostgreSQL Database
- Apache Kafka Message Broker

## Relationships
- API Gateway -> Search Controller: Routes search and catalogue requests [gRPC over mTLS]
- Search Controller -> Elasticsearch Cluster: Queries index [Elasticsearch Native Transport / TCP]
- Catalogue Manager -> PostgreSQL: Persists catalogue metadata [JDBC over TLS]
- Index Synchronizer -> Apache Kafka: Consumes item mutation events [Kafka protocol over TLS]
- Search Controller -> Analytics Publisher: Dispatches asynchronous search telemetry [In-process Spring ApplicationEvent]
- Analytics Publisher -> Apache Kafka: Publishes anonymized search event streams [Kafka protocol over TLS]

## Technology Stack
- Spring Boot / Java: Core framework for robust, enterprise-grade service implementation
- Elasticsearch: Powers fast, facet-filtered, fuzzy-matched searches meeting the < 800 ms latency requirement
- PostgreSQL: Provides transactional relational storage for catalogue metadata with AES-256 encryption-at-rest
- Apache Kafka: Enables decoupled, asynchronous event streaming for indexing and analytics
- Spring Cloud Stream: Simplifies event publishing for usage telemetry

## Rationale
This architecture decouples heavy search operations and asynchronous telemetry from transactional catalogue management, ensuring the < 800 ms performance target. Furthermore, it enforces EU-only data residency and strict security controls like JWT validation, PII scrubbing, and AES-256 encryption.