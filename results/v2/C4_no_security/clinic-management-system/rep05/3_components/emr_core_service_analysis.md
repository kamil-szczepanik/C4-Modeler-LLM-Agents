## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures high availability (99.99%), strict HIPAA/GDPR compliance, and sub-second clinical performance.

## Key Elements
- SPA Frontend (React, TypeScript, Nginx)
- EMR Core Service (Spring Boot, Java)
- Internal Components: Clinical Data Controller, EMR Business Logic Engine, Audit Interceptor, Data Access Repository, Clinical Notification Dispatcher, FHIR Mapping & Interoperability Component
- Billing & Claims Service, Audit & Compliance Service (Spring Boot, Java)
- Integration Gateway (Apache Camel, Spring Cloud Gateway)
- Data Stores: PostgreSQL with Patroni, Redis Cluster, Apache Kafka

## Relationships
- SPA Frontend -> EMR Core Service: Requests EMR data and operations [HTTPS / WSS]
- EMR Core Service -> Billing & Claims Service / Audit & Compliance Service: Internal workflows and audit events [gRPC over mTLS with eBPF routing]
- Data Access Repository -> PostgreSQL / Redis Cluster: Relational storage and caching [TCP with AES-256 encryption at rest]
- Clinical Notification Dispatcher / FHIR Mapping Component -> Apache Kafka: Event streaming and lab/imaging handoffs [TCP event streaming]

## Technology Stack
- Spring Boot (Java): Core backend container framework
- PostgreSQL with Patroni & Redis Cluster: Primary relational storage and read-through caching for <1s P95 latency
- Apache Kafka: Real-time clinical event streaming and notifications
- OpenTelemetry & eBPF: Distributed tracing and secure service mesh telemetry
- Resilience4j: Circuit breaking and fault tolerance for data repositories

## Rationale
This architecture uses asynchronous non-blocking gRPC and Kafka event streaming to protect sub-second EMR performance under high loads. Hybrid Kubernetes deployment combined with Patroni replication and Redis caching ensures 99.99% availability and HIPAA/GDPR compliance.