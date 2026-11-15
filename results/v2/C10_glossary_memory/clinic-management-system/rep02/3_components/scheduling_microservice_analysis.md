## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It provides secure, high-availability clinical IT infrastructure adhering to HIPAA and GDPR standards across a hybrid cloud environment.

## Key Elements
- Unified API Gateway (API Gateway, TLS 1.3)
- Scheduling Microservice (Spring Boot)
- Appointment Controller [Component, Spring MVC]
- Scheduling Engine [Component, Spring Service]
- Calendar Resource Manager [Component, Spring Service]
- Slot Reservation Manager [Component, Spring Service]
- Scheduling Data Access Repository [Component, Spring Data JPA]
- Distributed Cache (Redis Enterprise) (Redis Enterprise)
- Cloud-Native Distributed SQL Database (CockroachDB)
- Patient Portal / Mobile App [externalSystem, container]

## Relationships
- Unified API Gateway -> Appointment Controller [HTTP / REST via mTLS]
- Appointment Controller -> Scheduling Engine [In-process Java Method Call]
- Scheduling Engine -> Calendar Resource Manager [In-process Java Method Call]
- Scheduling Engine -> Slot Reservation Manager [In-process Java Method Call]
- Slot Reservation Manager -> Distributed Cache (Redis Enterprise) [Redis Protocol / TLS]
- Scheduling Engine -> Scheduling Data Access Repository [In-process Java Method Call]
- Scheduling Data Access Repository -> Cloud-Native Distributed SQL Database [SQL / TLS with serializable isolation]

## Technology Stack
- Spring Boot: Framework for building the Scheduling Microservice and its internal Java components.
- Spring MVC: Powers the Appointment Controller for exposing REST endpoints.
- Spring Data JPA: Manages database persistence and transaction boundaries.
- Redis Enterprise: Provides distributed cache storage for ephemeral slot reservation timeouts using TLS and opaque UUIDs.
- CockroachDB: Acts as the Cloud-Native Distributed SQL Database to guarantee ACID compliance, serializable isolation for R-02, and 10-year data retention.
- Kubernetes: Orchestrates containers across hybrid regions (`on-prem-k8s` and `eu-central-1`) with Pod Disruption Budgets.

## Rationale
This architecture uses granular internal components and distributed locking with Redis and CockroachDB to strictly enforce appointment clash prevention (R-02) without sacrificing concurrency. Zero-trust mTLS, RBAC/ABAC token validation, and encrypted caching fulfill HIPAA compliance and security mandates while maintaining 99.99% availability.