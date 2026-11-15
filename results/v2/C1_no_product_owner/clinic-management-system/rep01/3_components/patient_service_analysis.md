## Overview
The Clinic Management System manages patient admissions, Electronic Medical Records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It ensures 99.99% availability, strict HIPAA/GDPR compliance, and 10-year data retention across a hybrid cloud infrastructure.

## Key Elements
- **Patient API Controller (`@RestController`, Spring MVC):** Exposes RESTful endpoints for registration, demographics, and JSR-303 input validation.
- **Patient Security Filter (`@Component`, Spring Security):** Intercepts requests for OAuth2/JWT token validation and RBAC scoping.
- **Patient Domain Manager (`@Service`):** Enforces clinical rules and propagates security context for asynchronous events.
- **Audit Interceptor (`@Component` / AOP):** Captures immutable access and modification events for HIPAA/GDPR compliance.
- **Audit Event Buffer (`@Component`):** Provides a local encrypted SQLite file/durable volume buffer for audit resilience.
- **Patient Repository (`@Repository`, Spring Data JPA):** Manages data access with HikariCP connection pooling and HSM-managed AES-256 column encryption.

## Relationships
- **Patient API Controller** -> **Patient Security Filter**: Intercepts requests [Spring Security Filter Chain]
- **Patient API Controller** -> **Patient Domain Manager**: Delegates requests [Java Method Call]
- **Patient Domain Manager** -> **Patient Repository**: Queries and persists entity data [TLS-secured JDBC/JPA]
- **Patient Domain Manager** -> **Audit Interceptor**: Triggers audit logging events [Spring AOP/Event]
- **Audit Interceptor** -> **Audit Event Buffer**: Writes to local durable fallback storage on broker failure [Local File Buffer]
- **Audit Interceptor** -> **Message Broker Container**: Forwards audit events asynchronously [TLS/mTLS and SCRAM-SHA-512 via Apache Kafka]

## Technology Stack
- **Java Spring Boot / Spring MVC / Spring Security:** Provides the core framework for secure, enterprise-grade component architecture.
- **Spring Data JPA & HikariCP:** Ensures optimized, bounded database connection pooling for high-concurrency performance.
- **SQLite / Kubernetes Durable Volumes:** Implements a reliable local write-ahead buffer for zero-loss audit resilience during network outages.
- **HashiCorp Vault / Kubernetes Secrets:** Injects runtime database credentials and HSM encryption keys securely without hardcoding.

## Rationale
This component architecture enforces strict HIPAA and GDPR compliance through automated audit interception, local buffer resilience, and field-level encryption. The decoupled Spring Boot design combined with Kubernetes autoscaling and connection pooling guarantees high availability and rapid P95 performance during peak clinical hours.