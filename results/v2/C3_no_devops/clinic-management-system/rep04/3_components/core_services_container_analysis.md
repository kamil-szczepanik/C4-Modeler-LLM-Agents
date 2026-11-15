## Overview
The Core Services Container manages patient admissions, scheduling, and billing workflows for the Clinic Management System. It ensures high-availability clinical operations while maintaining strict HIPAA and GDPR compliance.

## Key Elements
- Core Services Container (Spring Boot Java)
- PatientManagementModule (Demographics capture)
- SchedulingModule (Appointment scheduling and resource clash checks)
- BillingModule (Billing and insurance claim submission)
- Redis Cache (In-memory cache for scheduling locks)
- PostgreSQL Database (Persistent state storage)
- Integration Service Container (External system integration)

## Relationships
- API Gateway -> Core Services Container: Routes requests [gRPC/REST over Istio mTLS]
- Core Services Container -> Integration Service Container: Copay & eligibility verification [gRPC over Istio mTLS]
- Core Services Container -> PostgreSQL Database: Reads and writes core data [JDBC over TLS with HikariCP]
- SchedulingModule -> Redis Cache: Fast resource clash validation [Redis Protocol over TLS with AUTH]
- Core Services Container -> Apache Kafka: Streams audit events [Kafka Producer API, TLS + SASL]

## Technology Stack
- Spring Boot (Java): Selected for robust enterprise transactional integrity and maturity
- Spring Data JPA: Standardizes persistence management
- Spring Security: Enforces fine-grained RBAC/ABAC and JWT scope verification
- Redis: Provides low-latency caching for scheduling availability locks
- PostgreSQL: Ensures ACID compliance for clinical records

## Rationale
Standardizing on Spring Boot modules satisfies strict HIPAA security and transactional requirements while isolating financial data. The architecture achieves 99.99% availability and sub-second performance through internal caching and resilient database connections.