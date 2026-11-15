## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% uptime, and 10-year data retention.

## Key Elements
- **Users**: Patients, Doctors, Nurses, Clinic Staff, Hospital Administrators, Billing Specialists, Revenue Cycle Managers.
- **External Systems**: Payment Gateway, Insurance Verification Service, External Lab & Imaging Systems, Public Health Registries.
- **API Gateway Containers**: Edge Router Component, Authentication Filter Component, Rate Limiter Component, Local Rate Limit Cache Component, Telemetry & Audit Filter Component.
- **Backend Services**: Identity & Access Management (Keycloak / OAuth2 Proxy), Core Services (Spring Boot / Java), Integration Service (Node.js / Apache Camel).
- **Infrastructure**: Message Broker (Kafka / RabbitMQ), Data Tier (PostgreSQL), Storage (WORM Object Storage), Kubernetes (`on-prem-k8s`, `eu-central-1`).

## Relationships
- Patients, Doctors, Nurses, and Administrators -> API Gateway: Access workflows via HTTPS / gRPC over TLS.
- API Gateway -> Identity & Access Management: Authenticates users and validates tokens via OAuth2 / OpenID Connect.
- API Gateway -> Core Services: Routes internal API requests via gRPC over mTLS.
- API Gateway -> Integration Service: Routes integration requests via gRPC over mTLS.
- Integration Service -> External Lab & Imaging Systems: Interoperates using HL7 FHIR APIs.

## Technology Stack
- **API Gateway**: Envoy (provides dynamic routing, native tracing, and strict mTLS).
- **Security**: OAuth2 / OpenID Connect, JSON Web Tokens (JWT), SPIFFE IDs.
- **Backend**: Spring Boot / Java for Core Services; Node.js / Apache Camel for Integration.
- **Data & Storage**: PostgreSQL (Relational Data); WORM Object Storage (10-year retention).
- **Orchestration**: Kubernetes with Istio service mesh across `on-prem-k8s` and `eu-central-1`.

## Rationale
This hybrid architecture satisfies HIPAA and GDPR mandates through strict mTLS, AES-256 encryption, and PHI-sanitized audit logging. Envoy-based localized rate-limiting caches and active-active multi-replica deployments ensure 99.99% availability without compromising clinical safety.