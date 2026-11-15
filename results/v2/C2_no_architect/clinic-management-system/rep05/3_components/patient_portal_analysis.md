## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability (99.99%) and HIPAA/GDPR compliance while streamlining clinical workflows.

## Key Elements
- Patients & Clinical/Administrative Staff (Users)
- Patient Portal Container (React, Web)
- API Gateway (Istio Service Mesh, Envoy)
- EMR & Billing Containers (Java, Spring Boot, PostgreSQL, PgBouncer)
- Patient Notification Microservice (Node.js)
- External Lab & Imaging Systems

## Relationships
- Patient Portal -> API Gateway: Routes client requests [HTTPS / mTLS via Istio]
- API Gateway -> EMR & Billing Containers: Forwards authenticated transactions [gRPC / HTTPS]
- EMR & Billing Containers -> External Lab & Imaging Systems: Interoperates via HL7 FHIR APIs [HTTPS]

## Technology Stack
- Frontend: React (WCAG 2.1 AA compliant, deployed via CDN with CSP)
- Security & Gateway: Istio Service Mesh, Envoy, OAuth 2.0 / OIDC, HttpOnly cookies (MFA mandated)
- Backend & Storage: Java, Spring Boot, PostgreSQL with PgBouncer, Redis (AES-256 encrypted session drafts)
- Infrastructure & Observability: Kubernetes (`on-prem-k8s`, `eu-central-1`), OpenTelemetry, Prometheus, Datadog

## Rationale
The hybrid architecture utilizes a Backend-for-Frontend (BFF) pattern and encrypted server-side session persistence to secure sensitive PHI while preventing client-side data loss. Active-active deployments across Kubernetes and Istio service mesh ensure the 99.99% uptime and low-latency performance required for critical healthcare operations.