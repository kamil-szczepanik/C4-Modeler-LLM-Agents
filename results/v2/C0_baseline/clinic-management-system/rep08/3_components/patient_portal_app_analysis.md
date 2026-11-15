## Overview
The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA/GDPR compliance, 99.99% availability, and long-term data retention across a hybrid cloud architecture.

## Key Elements
- Patients (Primary User)
- Patient Portal App (React/Node.js Container)
- Presentation Controller (React SPA Component)
- BFF Router (Node.js/Express Component)
- Auth & Session Manager (Node.js/Passport.js Component)
- Appointment & Profile Client (Node.js Component)
- Telemetry & Audit Interceptor (Node.js Middleware Component)
- API Gateway / Reverse Proxy (Envoy/NGINX)

## Relationships
- Presentation Controller -> BFF Router via HTTPS / TLS 1.3
- BFF Router -> Auth & Session Manager via Internal Function Call
- BFF Router -> Appointment & Profile Client via Internal Function Call
- Appointment & Profile Client -> API Gateway / Reverse Proxy via gRPC over TLS 1.3
- Telemetry & Audit Interceptor -> SIEM / Logging Sidecar via Syslog / OTLP

## Technology Stack
- React: Powers the WCAG 2.1 AA accessible, mobile-responsive client-side SPA.
- Node.js & Express: Implements the Backend-for-Frontend (BFF) pattern for secure aggregation and routing.
- Passport.js / OAuth2: Handles multi-factor authentication and token exchange.
- gRPC over TLS 1.3: Ensures high-performance, encrypted communication between internal components and the API Gateway.
- OpenTelemetry (OTLP): Facilitates distributed tracing and HIPAA/GDPR-compliant audit logging.

## Rationale
This architecture isolates sensitive authentication flows and client applications using a secure BFF pattern to prevent token leakage. The component decomposition ensures high availability, strict audit trails, and sub-second performance required for clinical environments.