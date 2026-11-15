## Overview
The Patient Portal is a secure, self-service container within the Clinic Management System that enables patients to manage appointments, view Electronic Medical Records, and settle bills. It ensures HIPAA and GDPR compliance while driving patient engagement and reducing front-desk overhead.

## Key Elements
- Patients (End-users)
- Patient Portal Container (Node.js / TypeScript)
- Authentication & Session Component (Passport.js / Auth0 SDK)
- Appointment & Scheduling UI/Controller
- Payment Orchestration Component (Stripe Elements / tokenized iFrames)
- Patient Dashboard & EMR Viewer
- Audit Logging Interceptor (Winston / Pino)
- API Gateway / BFF (Kong / Envoy)

## Relationships
- Patients -> Patient Portal Container: Accesses self-service features via HTTPS/REST [TLS 1.3]
- Patient Portal Container -> API Gateway / BFF: Communicates via mTLS and HTTPS/REST with scoped OAuth2 access tokens
- Authentication & Session Component -> API Gateway / BFF: Validates MFA status via OpenID Connect (OIDC)
- Patient Dashboard & EMR Viewer -> API Gateway / BFF: Fetches patient-scoped records via HTTPS/REST with JWT propagation
- Audit Logging Interceptor -> Apache Kafka: Emits audit events for PHI access attempts

## Technology Stack
- Node.js / TypeScript: Chosen for strict type safety and high-performance asynchronous I/O across portal components.
- Passport.js / Auth0 SDK: Powers multi-factor authentication and OAuth2/OIDC session management.
- Zod / Joi: Enforces rigorous schema validation on inbound payloads to prevent injection attacks.
- Winston / Pino: Captures structured audit logs for compliance tracking.
- Stripe Elements: Isolates financial data handling via tokenized payment frames to minimize PCI-DSS scope.

## Rationale
This architecture isolates the Patient Portal to enforce strict multi-factor authentication, attribute-based access control, and AES-256 encryption at the edge. By utilizing tokenized payment frames and asynchronous audit logging, the system achieves HIPAA and GDPR compliance without compromising user experience or performance.