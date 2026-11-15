## Overview
The Clinic Management System is a hybrid clinical IT platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures 99.99% availability, strict HIPAA/GDPR compliance, and sub-second EMR performance.

## Key Elements
- **API Gateway / Reverse Proxy** (Envoy / NGINX): Perimeter proxy featuring TLS Termination & WAF Module, Authentication & Claims Filter, Dynamic Routing & Rate Limiting Engine, and Resilience & Fault Injection Module.
- **Client Applications**: Patient Portal App (React SPA / Node.js / CDN) and administrative front-ends.
- **Microservices**: Clinical Core Service (Java / Spring Boot), Billing & Integration Service (Go / Temporal.io), Administrative & Analytics Service (Python / FastAPI + Celery), Notification & Messaging Service (Node.js / Python), and FHIR Integration Adapter.
- **Data & Identity**: Clinical Core Database (Encrypted SQL) and external Identity Provider (IdP) (OIDC / OAuth2).

## Relationships
- Patient / Clinician / Receptionist -> API Gateway / Reverse Proxy: HTTPS (TLS 1.3) via WAF with risk-based adaptive MFA.
- API Gateway / Reverse Proxy -> Patient Portal App: Routes static assets and SPA traffic via HTTPS.
- API Gateway / Reverse Proxy -> Clinical Core Service, Billing & Integration Service, Administrative & Analytics Service, Notification & Messaging Service, FHIR Integration Adapter: Routes API traffic via HTTPS / mTLS.
- API Gateway / Reverse Proxy -> Identity Provider (IdP): Validates session tokens via OpenID Connect (OIDC) / OAuth2 over HTTPS.
- Administrative & Analytics Service -> Clinical Core Database: Accesses read-only replicas via encrypted SQL over mTLS.

## Technology Stack
- **Envoy / NGINX**: Selected for high-performance edge routing, WAF capabilities, and active-active hybrid cluster deployment.
- **Java / Spring Boot**: Powers the Clinical Core Service for robust enterprise EMR transactions.
- **Go / Temporal.io**: Drives the Billing & Integration Service for resilient insurance claims and retries.
- **PostgreSQL / SQL with Encryption**: Provides AES-256 data at rest for the Clinical Core Database.
- **OpenID Connect (OIDC) / OAuth2**: Secures authentication across all user personas and services.

## Rationale
This architecture uses an active-active hybrid topology fronted by an Envoy/NGINX API Gateway to achieve 99.99% availability and sub-second EMR performance. Decoupled microservices ensure HIPAA/GDPR compliance through strict mTLS isolation, tenant-aware rate limiting, and centralized JWT validation.