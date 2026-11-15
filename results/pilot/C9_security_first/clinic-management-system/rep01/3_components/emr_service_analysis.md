## Overview
The EMR Service is a core container of the Clinic Management System designed to securely process, store, and retrieve electronic medical records with sub-second performance. It ensures compliance with HIPAA/GDPR while supporting high-availability clinical workflows in a hybrid cloud environment.

## Key Elements
- **EMR Service Container**: Spring Boot application running on Kubernetes (`on-prem-k8s` and `eu-central-1`).
- **EMR Query Component**: Internal component utilizing read-optimized Redis caching and PostgreSQL read replicas.
- **FHIR Mapper Component**: Internal component utilizing HAPI FHIR libraries and Apache Camel for interoperability.
- **Audit Service Component**: Internal component managing asynchronous, tamper-evident compliance logging.
- **Distributed PostgreSQL Database**: Primary data store with AES-256 encryption at rest and schema-per-service isolation.
- **Redis Caching Layer**: In-memory cache utilizing application-layer encryption for patient chart fragments.
- **Apache Kafka Event Broker**: Event streaming backbone using SASL/SCRAM authentication.

## Relationships
- **NGINX/Kong API Gateway -> EMR Service**: Routes external requests using gRPC with mTLS.
- **EMR Service -> Distributed PostgreSQL Database**: Persists and queries transactional health data via JDBC with HikariCP connection pooling.
- **EMR Service -> Redis Caching Layer**: Retrieves and stores encrypted patient chart fragments via Spring Data Redis (Lettuce).
- **EMR Service -> Apache Camel Integration Service**: Transforms and transmits clinical payloads using internal gRPC stubs.
- **FHIR Mapper Component -> External Lab & Imaging Systems**: Exchanges standardized data using HL7 FHIR R4 over mTLS.
- **EMR Service -> Apache Kafka Event Broker**: Streams domain events using SASL/SCRAM authentication.

## Technology Stack
- **Java & Spring Boot**: Core application runtime chosen for enterprise maturity and robust dependency injection.
- **gRPC with mTLS**: Inter-service communication protocol ensuring high performance and encrypted transport.
- **PostgreSQL**: Relational database providing ACID guarantees, replication, and AES-256 volume encryption.
- **Redis**: In-memory data store providing sub-second read performance for cached EMR queries.
- **Apache Camel & HAPI FHIR**: Integration framework and library for HL7 FHIR R4 interoperability.
- **Kubernetes & Istio**: Container orchestration and service mesh enabling 99.99% active-active hybrid availability.
- **ArgoCD & OpenTelemetry**: GitOps continuous delivery and distributed tracing for observability.

## Rationale
The architecture decouples read-heavy chart retrieval from transactional persistence and FHIR transformation, guaranteeing sub-second P95 response times. Strict ABAC, field-level encryption, and append-only audit logging satisfy rigorous HIPAA, GDPR, and 10-year data retention mandates without compromising clinical throughput.