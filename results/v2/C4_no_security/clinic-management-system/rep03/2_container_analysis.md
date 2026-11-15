## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals to handle patient admissions, scheduling, electronic medical records (EMR), and billing securely. It guarantees high availability (99.99%), strict regulatory compliance (HIPAA/GDPR), and 10-year data retention.

## Key Elements
- **Users**: Patient, Clinician/Doctor, Receptionist/Admin, Billing Specialist, Compliance/IT Auditor, Hospital Executive.
- **Frontend Container**: Single Page Application (TypeScript / React).
- **Edge Container**: API Gateway (Kong / Envoy) with mTLS.
- **Backend Containers**: Clinical Service (Go), Scheduling Service (Node.js), Billing Service (Java / Spring Boot), Audit & Compliance Log Service (Go), Integration Service / FHIR Facade (Go).
- **Infrastructure Containers**: Event Bus (Apache Kafka / RabbitMQ), Databases (PostgreSQL, MongoDB, Redis), Object Storage (encrypted S3-compatible).
- **External Systems**: External Lab & Imaging Systems, Payment Gateway & Insurance Clearinghouse, Identity Provider (IdP), Business Analytics / Reporting Service.

## Relationships
- **SPA to API Gateway**: HTTPS / JSON.
- **API Gateway to Backend Services**: Internal gRPC and REST over mTLS.
- **Backend Services to Event Bus**: Asynchronous domain event publishing (Kafka/RabbitMQ).
- **Integration Service to External Systems**: HL7 FHIR APIs for lab and imaging interoperability.
- **Backend Services to Data Stores**: TLS-encrypted connections to PostgreSQL, MongoDB, and Redis.

## Technology Stack
- **Frontend**: TypeScript, React, Nginx/CDN for rapid client-side rendering.
- **Gateway & Routing**: Kong / Envoy for rate limiting, mTLS, and circuit breaking.
- **Backend Languages**: Go (high-performance clinical and audit services), Node.js (scheduling), Java / Spring Boot (robust transactional billing).
- **Databases**: PostgreSQL (transactional clinical/scheduling data), MongoDB (immutable audit logs), Redis (caching).
- **Messaging & Infrastructure**: Apache Kafka / RabbitMQ for event-driven decoupling; Kubernetes (on-prem-k8s and AWS eu-central-1) managed via ArgoCD.

## Rationale
Isolating clinical, scheduling, and billing microservices via an Event Bus ensures that third-party payment or lab outages never block critical patient care workflows. Polyglot persistence, automated tiered archiving to encrypted S3 storage, and strict hybrid Kubernetes deployment patterns collectively satisfy the 99.99% availability, sub-second EMR performance, and 10-year retention mandates.