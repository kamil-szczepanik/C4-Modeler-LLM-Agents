## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It provides high availability, stringent compliance, and seamless interoperability across hybrid cloud environments.

## Key Elements
- **Front Desk Receptionist, Clinician/Doctor, Billing Specialist, Patient, Compliance Officer** (System Users)
- **Patient & Scheduling Service** (Spring Boot / Node.js container)
- **Patient Management Component** (Spring Webflux / Spring MVC)
- **Scheduling Engine** (Java domain-driven service)
- **Notification Orchestrator** (Spring Cloud Stream / Spring Integration)
- **PostgreSQL Clusters** & **Redis Enterprise** (Data persistence and caching)
- **External Lab & Imaging Systems, Insurance Clearinghouse, IdP, SMS/Email Gateway** (External Systems)

## Relationships
- **API Gateway -> Patient & Scheduling Service**: Routes requests via gRPC over Istio mTLS
- **Patient Management Component -> Identity Provider**: Authenticates via OAuth2/OIDC over HTTPS
- **Scheduling Engine -> PostgreSQL Clusters**: Executes transactions using SERIALIZABLE isolation and AES-256 encryption
- **Scheduling Engine -> Redis Enterprise**: Manages distributed locks via encrypted internal connections
- **Notification Orchestrator -> SMS/Email Notification Gateway**: Dispatches alerts via HTTPS using Resilience4j circuit breakers

## Technology Stack
- **Spring Boot / Node.js**: Core container runtime for business logic execution
- **PostgreSQL Clusters with PgBouncer**: Relational storage enforcing AES-256 encryption and ACID compliance
- **Redis Enterprise**: Distributed caching and locking with strict TTLs
- **Resilience4j**: Circuit breaker implementation for fault tolerance
- **Istio / Linkerd**: Service mesh handling mTLS and traffic splitting
- **OpenTelemetry**: Distributed tracing for SLA monitoring

## Rationale
This hybrid architecture isolates critical scheduling logic from I/O-bound notifications to guarantee 99.99% availability and strict data consistency. Robust transactional controls and distributed caching ensure high performance and strict HIPAA/GDPR compliance.