## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability, HIPAA/GDPR-compliant clinical IT operations across a hybrid cloud infrastructure.

## Key Elements
* API Gateway (Envoy / NGINX)
* Web Application Container (React / Next.js)
* Clinical & EMR Core Container (Spring Boot / Java)
* Billing & Claims Container (Node.js / Express)
* HL7 FHIR Integration Container (Apache Camel)
* Edge Sync Container (Go Daemon)
* Primary DB & Audit Store (PostgreSQL with Patroni)
* Internal Components: Patient Demographic Service, Scheduling Engine, EMR Management Service, Audit & Compliance Interceptor, Local State Cache & Sync Coordinator

## Relationships
* API Gateway -> Clinical & EMR Core Container: Routes validated requests [TLS / JWT / gRPC]
* Clinical & EMR Core Container -> Primary DB & Audit Store: Reads/writes clinical data [Pooled JDBC / PostgreSQL Protocol]
* Clinical & EMR Core Container -> HL7 FHIR Integration Container: Communicates internally [gRPC]
* Clinical & EMR Core Container -> Identity Provider: Authenticates users [OIDC / SAML]
* EMR Management Service -> Local State Cache & Sync Coordinator: Accesses cached patient data [In-Memory / Local IPC]

## Technology Stack
* Spring Boot / Java: High-performance core container runtime
* PostgreSQL with Patroni: Primary stateful persistence and audit store
* Redis: In-memory cache for appointment scheduling clash checks
* Caffeine Cache & Embedded RocksDB: Transient local state cache for offline resilience
* OpenTelemetry: Distributed tracing for latency isolation
* Kubernetes: Container orchestration across hybrid deployment nodes

## Rationale
This architecture uses an asynchronous AOP audit interceptor and local caching to achieve sub-second EMR screen loads (<1s P95) without compromising strict HIPAA/GDPR compliance. The hybrid Kubernetes deployment with embedded RocksDB guarantees 99.99% availability and offline resilience during network partitions.