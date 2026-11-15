## Overview
[The Clinic Management System is a hybrid cloud clinical IT platform designed to manage patient admissions, EMRs, scheduling, and billing. It provides high availability, stringent security, and interoperability for medium-sized hospitals and clinics.]

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists
- External Systems: Identity Provider (IdP), Lab & Imaging Systems, Insurance Clearinghouse
- API Gateway (Kong/Envoy, Rust/Go)
- Patient Portal Container (Node.js/NestJS, Go)
- EMR Core Service (Java/Spring Boot, .NET 8)
- Billing Integration Service (Java/Spring Boot)
- Audit & Compliance Daemon (Go)
- Data Tier (PostgreSQL with Citus/Multi-Master)
- Message Broker (NATS JetStream / Kafka)
- Target Infrastructure: Hybrid (`on-prem-k8s` and `eu-central-1`)

## Relationships
- Clients to API Gateway via HTTPS (REST/JSON)
- Internal microservices intercommunication via gRPC over mTLS with SPIFFE/SPIRE
- EMR Core and Billing Services to PostgreSQL via SQL over encrypted connections
- Billing Integration Service to Insurance Clearinghouse via secure APIs
- EMR Core to Lab & Imaging Systems via HL7 FHIR APIs

## Technology Stack
- Kong/Envoy (Rust/Go): API Gateway for rate-limiting, OAuth2/OIDC validation, and routing
- Java/Spring Boot / .NET 8: High-performance EMR Core and transactional Billing services
- PostgreSQL (Citus/Multi-Master): Relational storage with active-active/read replica support
- NATS JetStream / Kafka: Durable message broker for reliable asynchronous processing and transactional outbox patterns
- OpenTelemetry & Prometheus/Grafana: Distributed tracing and observability SLO monitoring
- WORM Storage: Cryptographically hashed immutable audit logging

## Rationale
[The hybrid architecture leverages local on-prem Kubernetes for low-latency clinical operations and `eu-central-1` for scalable cloud capabilities while meeting 99.99% uptime. Strict mTLS, automated outbox patterns, and isolated containers ensure HIPAA/GDPR compliance and zero data loss for billing without compromising sub-second EMR performance.]