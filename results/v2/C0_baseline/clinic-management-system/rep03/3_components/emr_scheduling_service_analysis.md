## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It provides high-availability, secure, and interoperable clinical IT infrastructure across hybrid cloud environments.

## Key Elements
- Front Desk Staff, Clinicians, Billing Officers, Patients, Regulatory Auditors
- React Single-Page Application (SPA) / React Native Mobile Client
- Envoy API Gateway / Edge Proxy
- EMR & Scheduling Service (Node.js / Java) containing Patient Registry, Scheduling Engine, EMR Core, Access Control & Policy Enforcer (OPA), and Audit Interceptor
- Billing & Claims Service (Java / Spring Boot)
- FHIR Interoperability Service (HAPI FHIR)
- Region-local PostgreSQL databases with Row-Level Security
- Redis Cache for in-memory session and slot caching
- Apache Kafka / RabbitMQ message brokers
- AWS S3 / on-prem WORM Object Storage
- HashiCorp Vault for secret management
- Centralized SIEM & Observability Platform

## Relationships
- React SPA/Mobile Client -> Envoy API Gateway: Submits user requests [HTTPS / WSS]
- Envoy API Gateway -> EMR & Scheduling Service: Routes internal requests securely [Internal mTLS via Istio/Linkerd]
- Access Control & Policy Enforcer (OPA) -> EMR Core / Patient Registry: Forwards authorized requests with cryptographic context [Internal gRPC]
- Scheduling Engine -> Redis Cache: Executes sub-100ms resource clash checks [Redis Protocol]
- EMR & Scheduling Service -> Region-local PostgreSQL: Reads/writes operational data with optimistic locking [Encrypted TCP]
- EMR & Scheduling Service -> Apache Kafka/RabbitMQ: Publishes asynchronous events [Kafka/AMQP protocol]
- EMR & Scheduling Service -> AWS S3 WORM Storage: Archives immutable audit records [HTTPS / S3 API]
- EMR & Scheduling Service -> HashiCorp Vault: Retrieves dynamic database credentials [HTTPS / Vault API]
- Audit & Compliance Interceptor -> Centralized SIEM: Streams PHI-masked telemetry [Secure syslog/OTLP]

## Technology Stack
- React / React Native: Powers cross-platform client interfaces with responsive UI for <1s EMR load requirements.
- Node.js & Java / Spring Boot: Provides robust microservice execution for business logic and scheduling engines.
- Open Policy Agent (OPA): Enforces fine-grained ABAC/RBAC and break-glass auditing via local sidecars.
- PostgreSQL: Manages structured clinical data utilizing Row-Level Security (RLS) for multi-tenant isolation.
- Redis: Delivers low-latency in-memory caching for active records and scheduling slot validation.
- Apache Kafka / RabbitMQ: Enables decoupled asynchronous event-driven messaging.
- AWS S3 & on-prem WORM: Ensures immutable, retention-compliant long-term data storage.
- HashiCorp Vault: Secures dynamic credentials and short-lived internal JWT tokens.
- Istio/Linkerd: Secures service mesh communication via strict SPIFFE/SPIRE mTLS.

## Rationale
This architecture ensures strict HIPAA and GDPR compliance through embedded OPA policy enforcement, PHI masking, and WORM storage audit trails. The hybrid deployment with local read-replicas, Redis caching, and active-active components guarantees 99.99% availability and sub-second EMR performance.