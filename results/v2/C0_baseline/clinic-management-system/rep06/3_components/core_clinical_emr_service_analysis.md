## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers. It is architected for high availability, strict regulatory compliance, and high-performance clinical workflows.

## Key Elements
- **EMR Orchestrator Component**: Java/Spring MVC service managing REST requests and clinical workflow coordination.
- **CDR Access Component**: Spring Data JPA layer interacting with PostgreSQL via PgBouncer.
- **Audit Interceptor Component**: AspectJ / Spring AOP service emitting asynchronous gRPC audit events.
- **Security Enforcement Component**: Spring Security module handling ABAC/RBAC and dynamic HashiCorp Vault tokenization.
- **PostgreSQL Databases**: Primary datastore featuring column-level encryption and active-passive replication.
- **Audit & Compliance Service**: External Go/Spring Boot service receiving audit logs.

## Relationships
- **API Gateway -> EMR Orchestrator Component**: Routes incoming EMR REST requests [OAuth2/OIDC, mTLS]
- **CDR Access Component -> PostgreSQL Databases**: Executes optimized queries and reads [PostgreSQL Protocol, mTLS]
- **Audit Interceptor Component -> Audit & Compliance Service**: Emits cryptographic audit events [gRPC, mTLS]
- **Security Enforcement Component -> HashiCorp Vault**: Retrieves dynamic, short-lived database credentials and encryption keys [HTTPS/REST, mTLS]

## Technology Stack
- **Java Spring Boot / Spring MVC**: Chosen for robust enterprise framework support and rapid development of core clinical services.
- **Spring Data JPA & PgBouncer**: Selected for efficient database interaction and connection pooling to meet sub-second latency requirements.
- **Spring AOP & gRPC**: Utilized for asynchronous, zero-blocking audit event emission.
- **PostgreSQL with Column-Level Encryption**: Implemented for secure, relational PHI storage meeting HIPAA/GDPR constraints.
- **HashiCorp Vault**: Deployed for dynamic secret injection, ephemeral credentials, and key management.

## Rationale
This architecture achieves sub-second P95 EMR load times by decoupling asynchronous auditing and optimizing database read paths. It guarantees HIPAA and GDPR compliance through context-aware security controls, immutable audit trails, and robust hybrid-cloud encryption.