## Overview
The React SPA is a high-performance frontend application designed for clinical, administrative, and billing staff within the Clinic Management System. It delivers secure, low-latency access to patient admissions, EMRs, scheduling, and billing while enforcing strict healthcare compliance.

## Key Elements
- React SPA (React Frontend)
- Auth & Session Manager
- Routing & RBAC Guard
- API Client (OpenAPI/Fetch)
- Feature Modules (Patient Registration UI, Appointment Scheduler, EMR Viewer & Editor, Billing Console)
- Telemetry & RUM Agent
- External: API Gateway (Nginx / Kong), Identity Provider (IdP), AWS CloudFront CDN

## Relationships
- React SPA $\rightarrow$ API Gateway: HTTPS / JSON (REST via OpenAPI) and WSS for real-time updates
- Auth & Session Manager $\rightarrow$ Identity Provider (IdP): HTTPS (OAuth2 / OIDC with PKCE)
- React SPA $\rightarrow$ AWS CloudFront CDN: HTTPS for static asset delivery

## Technology Stack
- React: Component-based UI framework for rapid, maintainable interface development
- SessionStorage & Local Caching: Used for form-state persistence and optimizing EMR load times below P95 targets
- Sentry / RUM: Client-side error tracking and Real User Monitoring to ensure high availability and performance

## Rationale
This architecture ensures sub-second EMR interactions and high availability across hospital workstations through optimized local caching, resilient state persistence, and robust telemetry. Strict RBAC enforcement and OIDC authentication maintain HIPAA and GDPR compliance for sensitive clinical data.