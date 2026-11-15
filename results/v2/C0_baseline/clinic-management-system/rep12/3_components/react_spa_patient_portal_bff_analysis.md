## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for medium-sized hospitals and clinics. It ensures 99.99% availability, HIPAA/GDPR compliance, and sub-second EMR performance using a hybrid cloud deployment.

## Key Elements
- Patients & Hospital Staff (Users)
- Patient Portal SPA & BFF (React & Node.js/NestJS)
- Clinician/Staff Workspace SPA & BFF (React & Node.js/NestJS)
- Kong API Gateway (Kong)
- Istio Service Mesh (Istio)
- Spring Boot Core Services (Spring Boot / Java)
- Apache Camel Integration Service
- Go Audit Logging Container
- Apache Superset Reporting Container
- PostgreSQL (Primary & Read-Replica) & Redis
- HashiCorp Vault

## Relationships
- Patients & Staff -> Patient Portal & Clinician/Staff Workspaces: Accesses portals via HTTPS/REST
- Patient Portal & Clinician Workspaces -> Kong API Gateway: Forwards requests via HTTPS
- Kong API Gateway -> Istio Service Mesh: Routes internal traffic using mTLS
- Spring Boot Core Services -> PostgreSQL & Redis: Handles persistence and caching
- Apache Camel -> External Lab & Imaging Systems: Integrates via HL7 FHIR APIs

## Technology Stack
- React & Node.js/NestJS: Powers decoupled frontend SPAs and BFFs for optimized user experiences
- Spring Boot (Java): Provides scalable enterprise core services
- PostgreSQL & Redis: Ensures reliable relational storage and fast caching
- Kong & Istio: Manages API routing, rate limiting, and zero-trust service mesh security
- HashiCorp Vault: Secures secrets and AES-256 encryption keys

## Rationale
Separating patient-facing and clinician workflows isolates public threat surfaces from internal hospital operations. This architecture satisfies stringent HIPAA/GDPR security, high availability (99.99%), and sub-second EMR performance constraints.