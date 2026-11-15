## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It enforces strict HIPAA/GDPR compliance and 99.99% availability via an active-active architecture.

## Key Elements
- **Users:** Receptionist/Front Desk, Clinician/Doctor, Billing Specialist, Patient
- **External Systems:** External Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP)
- **API Gateway Containers:** Kong / Envoy, WAF / Coraza, Redis, Fluentbit sidecar
- **Core Containers:** EMR & Scheduling Service (Java / Spring Boot, Encrypted PostgreSQL), Billing & Claims Service (Node.js / TypeScript, Redis, RabbitMQ), Interoperability Service (.NET Core / Apache Camel), Audit Logger Sidecar

## Relationships
- Users -> API Gateway: Authenticate and request routing [HTTPS / OAuth 2.0 / OIDC / REST / GraphQL]
- API Gateway -> EMR & Scheduling Service: Route requests via service mesh [gRPC over mTLS]
- API Gateway -> Billing & Claims Service: Route billing requests [gRPC over mTLS]
- API Gateway -> IdP: Fetch JWKS public keys [HTTPS]
- API Gateway -> Metering Collector: Async batch telemetry push [gRPC]

## Technology Stack
- **API Gateway:** Kong / Envoy with ModSecurity/Coraza WAF for payload inspection and threat mitigation.
- **Security:** TLS 1.3 externally, mTLS internally with SPIFFE/SPIRE certificate rotation, and JWT validation with OIDC.
- **Backend Services:** Java / Spring Boot for EMR, Node.js / TypeScript for Billing, .NET Core / Apache Camel for Interoperability.
- **Databases & Messaging:** Encrypted PostgreSQL (AES-256 at rest), Redis for token-bucket rate limiting, RabbitMQ for async messaging.
- **Observability & Logging:** Prometheus, W3C Trace Context, and Fluentbit sidecar with HMAC-SHA256 log sanitization.

## Rationale
This hybrid architecture uses an active-active Kubernetes and cloud deployment with mTLS and gRPC to meet stringent 99.99% availability and low-latency performance targets. Centralized security enforcement at the API Gateway satisfies HIPAA and GDPR data protection mandates.