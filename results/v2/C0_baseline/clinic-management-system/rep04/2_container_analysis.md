## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA/GDPR compliance, high availability (99.99%), and a 10-year data retention policy via a secure hybrid cloud architecture.

## Key Elements
- **Users:** Patients, Clinic Staff/Receptionists, Clinicians/Doctors, Billing Specialists, and Hospital Administrators.
- **External Systems:** Identity Provider (IdP), External Lab & Imaging Systems, External Payment Gateway & Insurance Clearinghouse.
- **Containers:** Kong/Envoy API Gateway, React SPA Web Application, Node.js/Spring Boot Patient Portal BFF, Java (Spring Boot) Core Services, Billing Service, Apache Camel/MuleSoft Integration Engine, and Apache Kafka Event Stream.
- **Data & Infrastructure:** PostgreSQL clusters, Redis Enterprise caching layer, and WORM object storage.

## Relationships
- Patients & Staff interact with the React Web App and Patient Portal BFF via HTTPS/TLS 1.3 through the Kong/Envoy API Gateway.
- API Gateway communicates with Core Services and Billing Service using gRPC/REST over mTLS enforced by Istio service mesh.
- Core Services query PostgreSQL and Redis Enterprise using encrypted database protocols.
- Integration Engine connects to External Lab & Imaging Systems via HL7 FHIR APIs over TLS.
- Billing Service communicates with External Payment Gateway via HTTPS.

## Technology Stack
- **Frontend:** React served via Nginx containers for clinic staff UI.
- **Backend Services:** Java (Spring Boot) and Node.js for modular core, billing, and BFF containers.
- **Data & Caching:** PostgreSQL with AES-256 encryption at rest for ACID compliance; Redis Enterprise for low-latency session and reference data caching.
- **Integration & Messaging:** Apache Camel/MuleSoft for HL7 FHIR translation; Apache Kafka for local event-driven telemetry.
- **Infrastructure & Security:** Hybrid Kubernetes (on-prem-k8s and AWS eu-central-1), Istio for mTLS service mesh, and OAuth2/OIDC via external IdP.

## Rationale
The hybrid Active-Passive architecture prevents split-brain scenarios and guarantees 99.99% availability while isolating sensitive Protected Health Information (PHI). Containerized microservices, local caching, and strict mTLS security boundaries fulfill sub-second EMR performance and rigorous healthcare compliance mandates.