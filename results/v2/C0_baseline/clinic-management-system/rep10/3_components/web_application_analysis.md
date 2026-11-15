## Overview
The Clinic Management System is a hybrid cloud healthcare platform providing patient registration, EMR, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and secure clinical workflows.

## Key Elements
- Patients, Clinicians, Administrative Staff, Billing Officers, Auditors
- Web Application (React / TypeScript SPA)
- API Gateway (NGINX / Envoy) with Backend-for-Frontend (BFF) proxy
- EMR Service (Node.js / Go), Billing Service (Java / Spring Boot), Scheduling Service (Node.js / Go), Notification Service (Python / FastAPI), Integration Service (Java / Spring Boot)
- PostgreSQL (AES-256 encrypted at rest), Redis, RabbitMQ
- HashiCorp Vault

## Relationships
- Users -> Web Application: Access portals and clinical workflows via HTTPS
- Web Application -> API Gateway / BFF: Communicates using HTTPS with `HttpOnly`, `SameSite=Strict` cookies
- API Gateway -> Microservices: Routes requests via internal gRPC/HTTPS
- Integration Service -> External Systems: Connects to labs and insurance via HL7 FHIR over HTTPS

## Technology Stack
- React / TypeScript: Chosen for dynamic persona-based UI composition and high-performance EMR rendering (<1s P95)
- NGINX / Envoy & BFF: Implemented for secure session handling, routing, and preventing client-side token exposure
- PostgreSQL with AES-256: Selected to meet strict data retention and HIPAA encryption-at-rest mandates
- Hybrid Cloud (on-prem-k8s & AWS eu-central-1): Deployed across environments to achieve 99.99% active-active availability

## Rationale
This hybrid architecture isolates sensitive Protected Health Information (PHI) server-side while delivering a high-performance, compliant React frontend. It successfully balances rigorous healthcare security standards with high availability and low-latency clinical operations.