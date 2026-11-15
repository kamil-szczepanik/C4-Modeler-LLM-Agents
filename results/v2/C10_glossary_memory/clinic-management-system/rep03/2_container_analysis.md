## Overview
The Clinic Management System is a hybrid clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high availability and compliance through a decoupled, zero-trust container architecture deployed across on-premises Kubernetes and AWS (`eu-central-1`).

## Key Elements
- **Users:** Patient, Receptionist / Front Desk, Clinician / Doctor, Billing Specialist, Hospital Administrator.
- **API Gateway / Reverse Proxy:** Envoy / NGINX handling TLS 1.3 termination, WAF, and traffic routing.
- **Patient Portal App:** React SPA served via Node.js / CDN.
- **Clinical Core Service:** Java / Spring Boot managing EMR data, scheduling resource checks, and audit trails.
- **Billing & Integration Service:** Go / Temporal.io handling insurance claims and resilient payment retries.
- **Administrative & Analytics Service:** Python / FastAPI + Celery isolating compliance and reporting queries.
- **Notification & Messaging Service:** Node.js / Python managing asynchronous patient alerts via SMS/Email APIs.
- **FHIR Integration Adapter:** Dedicated service decoupling external clinical systems.
- **External Systems:** Payment Gateway, External Lab & Imaging Systems, Identity Provider (IdP).

## Relationships
- **Users -> API Gateway:** HTTPS (TLS 1.3) via WAF with risk-based adaptive MFA.
- **Clinic Management System -> Identity Provider (IdP):** OpenID Connect (OIDC) / OAuth2 over HTTPS.
- **Billing & Integration Service -> Payment Gateway:** Payment REST APIs over encrypted HTTPS.
- **FHIR Integration Adapter -> External Lab & Imaging Systems:** HL7 FHIR APIs over encrypted HTTPS.
- **Clinical Core Service -> Notification & Messaging Service:** AMQP / Kafka over mTLS.
- **Administrative & Analytics Service -> Clinical Core Database:** Read-only replicas via encrypted SQL over mTLS.

## Technology Stack
- **API Gateway:** Envoy / NGINX for edge security and reverse proxying.
- **Backend Services:** Java / Spring Boot (Clinical Core), Go / Temporal.io (Billing), Python / FastAPI (Analytics).
- **Frontend:** React SPA via Node.js / CDN.
- **Messaging / Event Streaming:** AMQP / Kafka for asynchronous event-driven workflows.
- **Security & Secrets:** HashiCorp Vault / AWS Secrets Manager for dynamic secrets; service mesh for mTLS.
- **Infrastructure:** Hybrid Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) managed via ArgoCD.

## Rationale
This architecture guarantees sub-second EMR load performance (P95 < 1s) by isolating heavy analytical queries onto read-only replicas and segregating transaction paths. Furthermore, it ensures HIPAA/GDPR compliance and 99.99% uptime via zero-trust mTLS, WORM audit storage, and active-active hybrid cloud resilience.