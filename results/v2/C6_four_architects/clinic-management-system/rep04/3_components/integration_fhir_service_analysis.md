## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, 99.99% availability, and ten-year data retention.

## Key Elements
- **Users**: Doctors, Nurses, Receptionists, Billing Staff
- **External Systems**: Identity Provider (IdP), Payment Gateway, Insurance Clearinghouse, External Lab & Imaging Systems
- **Frontend Container**: Single-Page Application (React / TypeScript)
- **Edge Container**: API Gateway (Kong / Envoy)
- **Core Containers**: Core Clinical Microservice (Spring Boot), Scheduling Microservice (Go), Billing & Claims Microservice (.NET)
- **Integration Containers**: Integration / FHIR Service (Node.js), FHIR Integration Broker (Apache Camel)
- **Data & Infrastructure Containers**: Distributed Relational Database (CockroachDB / PostgreSQL), Message Broker / Event Bus (Apache Kafka), State Caching Layer (Redis Enterprise), Key Management Service (Vault / Cloud KMS), Audit Log Store (Elasticsearch / Immutable Storage), Observability & Telemetry Collector (OpenTelemetry / Prometheus / Loki), Service Mesh (Istio)
- **Integration / FHIR Service Components**: FHIR Facade Controller, Authentication & SMART-on-FHIR Authorizer, FHIR-to-Domain Mapper, Outbound Sync Engine, FHIR Storage Repository, Audit & Compliance Interceptor, FHIR Profile Validator, FHIR Caching Manager

## Relationships
- API Gateway -> Core Containers: Routes traffic [gRPC over mTLS via Istio]
- Integration / FHIR Service -> Message Broker / Event Bus: Publishes domain events [Kafka producer, JSON over TCP]
- Integration / FHIR Service -> Distributed Relational Database: Persists canonical data [PostgreSQL wire protocol over TLS 1.3]
- Outbound Sync Engine -> FHIR Integration Broker: Forwards sync payloads [gRPC over mTLS]
- FHIR Facade Controller -> FHIR Caching Manager: Caches resources [TCP over TLS 1.3 to Redis Enterprise]

## Technology Stack
- Node.js & TypeScript: Powers the Integration / FHIR Service for modular routing and mapping
- Apache Kafka: Event bus ensuring asynchronous, decoupled communication
- PostgreSQL / CockroachDB: Distributed relational storage supporting high availability
- Redis Enterprise: State caching layer ensuring sub-second performance (P95 < 1s)
- Istio Service Mesh & Vault: Secures communications via mTLS and manages encryption keys (AES-256)

## Rationale
This hybrid microservices architecture meets strict HIPAA and GDPR regulations using robust encryption, mTLS, and immutable audit logs. Active-active multi-region deployment and event-driven asynchronous messaging ensure 99.99% uptime and sub-second performance.