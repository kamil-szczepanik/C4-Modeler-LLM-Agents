## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and long-term data retention.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists, and Clinic Administrators (Users)
- External Lab & Imaging Systems, Payment Gateways, Insurance Clearinghouses, and Identity Provider (External Systems)
- React SPA & Node.js Patient Portal BFF (Client/Frontend)
- Kong API Gateway & Istio Service Mesh (Networking/Security)
- Spring Boot Core Services, Apache Camel Integration Service, Go Audit Logging Container, Apache Superset Reporting Container (Containers)
- PostgreSQL (Primary & Read-Replica), Redis, HashiCorp Vault (Data & Security)

## Relationships
- Patients & Staff interact with the React SPA and Patient Portal BFF via HTTPS/REST.
- API Gateway routes and validates traffic using JWT, enforcing mTLS via Istio service mesh across hybrid clusters.
- Core Services communicate with PostgreSQL via JDBC and Redis via TCP.
- Integration Service connects to external Lab, Imaging, and Payment systems using HL7 FHIR and HTTPS protocols.

## Technology Stack
- React & Node.js/NestJS: Frontend and Backend-for-Frontend for responsive client interfaces.
- Spring Boot (Java) & Go: Core business logic and high-throughput write-optimized audit logging.
- Kong & Istio: API routing, rate limiting, and zero-trust mTLS encryption.
- PostgreSQL & Redis: ACID-compliant transactional persistence, read-replicas for CQRS, and distributed caching.
- HashiCorp Vault & ArgoCD: Centralized secret management and GitOps hybrid cluster synchronization.

## Rationale
The hybrid container architecture uses CQRS and database read-replicas to maintain sub-second EMR performance while executing heavy analytics. Furthermore, zero-trust mTLS boundaries, immutable audit logging, and strict data partitioning ensure 99.99% availability and full HIPAA/GDPR compliance.