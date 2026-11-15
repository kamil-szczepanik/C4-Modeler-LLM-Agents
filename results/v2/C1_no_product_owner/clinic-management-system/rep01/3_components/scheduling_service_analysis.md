## Overview
The Scheduling Service is a core container within the Clinic Management System responsible for managing hospital staff and patient appointments. It provides robust, secure, and highly available appointment workflows with strict resource clash checks.

## Key Elements
- Appointment Controller (Spring MVC REST Controller)
- Security Interceptor (Spring Security filter)
- Audit Logging Component (Regulatory audit trail recorder)
- Scheduling Engine (Core domain logic)
- Resource Clash Checker (Availability and conflict detection)
- Distributed Lock Manager (Redisson-based concurrency control)
- Notification Publisher (Spring Kafka event emitter)
- Scheduling Repository (Spring Data JPA data access layer)

## Relationships
- API Gateway & Edge Router -> Appointment Controller: Forwards API requests via mTLS and Istio/Linkerd service mesh
- Security Interceptor -> Appointment Controller: Validates local JWT claims and enforces RBAC
- Scheduling Engine -> Distributed Lock Manager: Acquires cluster-aware locks via TLS-secured Redis
- Resource Clash Checker -> Scheduling Repository: Queries availability via TLS-secured JDBC
- Notification Publisher -> Message Broker Container: Publishes domain events via TLS/mTLS and SCRAM-SHA-512

## Technology Stack
- Spring Boot & Spring MVC: Provides modular stereotypes for clean separation of concerns and testability
- Redis with Redisson Client: Enables distributed locking for atomic slot reservation and concurrent clash prevention
- PostgreSQL: Provides persistent storage for appointment records with TLS-secured JDBC
- Spring Kafka: Emits asynchronous domain events with TLS-secured message broker integration
- HashiCorp Vault & Kubernetes Secrets: Injects secure credentials without hardcoding

## Rationale
This architecture ensures 99.99% availability and high concurrency performance while meeting strict HIPAA and GDPR compliance requirements. Distributed locking and fail-closed resilience patterns prevent booking conflicts and data leakage.