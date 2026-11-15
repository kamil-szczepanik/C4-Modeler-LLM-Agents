## Overview
The EMR Service is a Java/Spring Boot modular monolith within the Clinic Management System designed to handle electronic medical records and clinical workflows. It ensures high-performance clinical data management while maintaining strict HIPAA and GDPR compliance across a hybrid cloud architecture.

## Key Elements
* EMR API Controller (Spring MVC/WebFlux)
* Clinical Record Manager (Core domain & Clinical Summary Generator)
* Audit Trail Service & Compliance Dashboard Feed
* Consent & Preference Handler
* FHIR Interoperability Adapter
* Vault Transit Client (HashiCorp Vault)
* PostgreSQL Databases with read replicas & Redis caching layer
* Apache Kafka Event Broker

## Relationships
* API Gateway -> EMR API Controller: Routes requests via gRPC / Internal Mesh with mTLS
* EMR API Controller -> Consent & Preference Handler: Pre-processes patient consent validation via internal calls
* Clinical Record Manager -> PostgreSQL Databases: JDBC over TCP / TLS with HikariCP pooling
* Clinical Record Manager -> Redis: Caches encrypted PHI summaries over TCP / TLS with Resilience4j
* Audit Trail Service -> Apache Kafka Event Broker: Streams signed events via Spring Kafka over TCP / TLS
* EMR Service components -> HashiCorp Vault: Manages encryption keys and envelope encryption via Vault Transit Client
* FHIR Interoperability Adapter -> External Systems: Communicates via HL7 FHIR APIs with OAuth2/OIDC mutual TLS

## Technology Stack
* Java / Spring Boot: Core runtime for the modular monolith providing robust enterprise features
* PostgreSQL: Primary transactional persistence with automated table-partitioning for 10-year data retention
* Redis: High-availability caching layer ensuring P95 load times under 1 second
* Apache Kafka: Asynchronous event broker for tamper-evident audit streaming
* HashiCorp Vault: Provides envelope encryption, Vault Transit Client, and dynamic key rotation
* Micrometer & OpenTelemetry: Observability and distributed tracing for 99.99% uptime monitoring

## Rationale
This architecture uses a modular Spring Boot design combined with Redis caching and PostgreSQL read-replicas to consistently achieve the sub-second P95 latency required for clinical efficiency. Strict envelope encryption via HashiCorp Vault, immutable Kafka auditing, and OAuth2/OIDC mTLS integration guarantee uncompromised HIPAA and GDPR compliance without sacrificing high availability.