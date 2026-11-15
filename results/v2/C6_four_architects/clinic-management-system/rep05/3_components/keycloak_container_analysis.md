## Overview
The Clinic Management System is a hybrid-cloud clinical IT platform providing patient admissions, EMR, scheduling, and billing while ensuring HIPAA and GDPR compliance with 99.99% availability. It utilizes a containerized microservices architecture deployed across on-premises Kubernetes and AWS eu-central-1.

## Key Elements
- Patients, Clinicians/Staff, Billing Administrators
- API Gateway (Kong / Nginx)
- Keycloak Container (Docker / Keycloak) with 7 internal components: Authentication SPI, User Federation Provider, Token Service, Session Cache Manager (Infinispan), Admin REST API / Theme Engine, Audit Event SPI, Identity Brokering & Federation Engine
- Patient & Scheduling Service, EMR Service, Billing Service, FHIR Interoperability Service (Java/Python)
- Primary Database (PostgreSQL) with PgBouncer
- Message Broker (Apache Kafka) and Distributed Cache (Redis Enterprise)
- External Systems (Identity Provider, Insurance Gateway, External Lab & Imaging Systems, National Health Registry)

## Relationships
- API Gateway -> Keycloak Container: Token validation and IAM requests [HTTPS / OIDC]
- Authentication SPI & Token Service -> Primary Database: Persists credentials and config [JDBC / TLS via PgBouncer]
- Session Cache Manager -> Session Cache Manager (Remote): Synchronizes user sessions [Infinispan / TCP]
- Audit Event SPI -> Observability Agent: Exports security logs [Syslog / HTTPS]
- FHIR Interoperability Service -> External Lab & Imaging Systems: HL7 FHIR data exchange [HTTPS / REST]

## Technology Stack
- Keycloak / Quarkus: Core IAM runtime for high-performance authentication and tokens
- PostgreSQL with PgBouncer: Relational persistence with connection pooling for ACID compliance
- Apache Kafka: Event-driven streaming for decoupled microservices communication
- Redis Enterprise: Distributed caching for session management and rate limiting
- Istio / Envoy: Service mesh ensuring zero-trust mTLS service-to-service communication
- AWS S3 / On-Prem Object Storage: Long-term encrypted data retention (≥ 10 years)

## Rationale
The hybrid architecture leverages local Kubernetes for low-latency clinical operations and cloud regions for scalability, meeting 99.99% uptime. Strict separation of services via an API gateway and robust IAM guarantees HIPAA and GDPR data privacy mandates.