## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely handle patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures high availability, strict regulatory compliance, and rapid clinical workflows.

## Key Elements
- API Gateway (Istio Service Mesh, Envoy)
- EMR & Billing Containers (Java, Spring Boot, PostgreSQL, PgBouncer)
- Analytics & Audit Reporting Container (Python, OpenTelemetry, Datadog/Prometheus)
- Lab and Imaging Systems (External Systems)
- Clinical Staff and Administrative Staff (Users)

## Relationships
- API Gateway -> EMR & Billing Containers: Routes EMR and billing transactions via gRPC / HTTPS with mTLS
- EMR & Billing Containers -> Lab and Imaging Systems: Integrates clinical data exchange via HL7 FHIR APIs over mTLS
- EMR & Billing Containers -> PostgreSQL: Manages persistent patient and billing records via TLS connections with connection pooling

## Technology Stack
- Java & Spring Boot: Provides robust transactional integrity and enterprise security features for EMR and billing workflows.
- PostgreSQL & PgBouncer: Ensures ACID compliance and optimized database connection pooling for high-frequency clinical transactions.
- Istio Service Mesh & Envoy: Manages secure zero-trust service-to-service communication via mTLS and canary deployments.
- OpenTelemetry & Prometheus/Datadog: Delivers end-to-end tracing and system observability while preventing PHI leakage.
- Patroni: Automates active-passive PostgreSQL failover to meet high availability targets.

## Rationale
This architecture uses an active-passive PostgreSQL topology with PgBouncer and JVM tuning to meet strict 99.99% availability and sub-second P95 latency requirements. Zero-trust security controls, including column-level encryption, PostgreSQL Row-Level Security, and Istio mTLS, ensure full HIPAA and GDPR compliance across hybrid boundaries.