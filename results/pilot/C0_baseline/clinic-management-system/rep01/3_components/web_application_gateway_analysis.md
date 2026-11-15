## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and long-term data retention.

## Key Elements
- Users: Patients, Receptionists, Attending Physicians, Billing Specialists, Clinic Administrators
- External Systems: Identity Provider, Third-Party Payment Gateways/Clearinghouses, External Laboratory & Imaging Systems
- Containers: Web Application Gateway (NGINX), Core API Service (Node.js / NestJS), EMR Engine (Java / Spring Boot), Billing Worker (Python / Celery), Audit Logging Sidecar, PostgreSQL Cluster (with AES-256 and LUKS), Redis, Apache Kafka
- Gateway Components: TLS Termination Module, Reverse Proxy & Routing Engine, Rate Limiter & WAF Module, JWT Validation Filter

## Relationships
- Patients, Receptionists, Attending Physicians, Billing Specialists, Clinic Administrators -> Web Application Gateway: Accesses services and manages workflows [HTTPS/TLS]
- Web Application Gateway -> Core API Service: Routes API requests [gRPC over TLS with mTLS]
- WAF Module -> Audit Logging Sidecar: Forwards security event telemetry [Local IPC]

## Technology Stack
- Web Gateway: NGINX for high-performance edge routing and TLS termination
- Core Services: Node.js / NestJS (Core API) and Java / Spring Boot (EMR Engine) for robust business logic
- Storage & Messaging: PostgreSQL Cluster (with AES-256 and LUKS), Redis for caching, Apache Kafka for event streaming
- Security & Interoperability: OAuth2/JWT via Identity Provider, HL7 FHIR APIs for clinical system integration

## Rationale
This architecture uses a hybrid cloud model with active-active redundancy to satisfy strict 99.99% availability and HIPAA/GDPR compliance requirements. Microservices and event-driven messaging ensure high performance, scalability, and sub-second P95 EMR screen loads.