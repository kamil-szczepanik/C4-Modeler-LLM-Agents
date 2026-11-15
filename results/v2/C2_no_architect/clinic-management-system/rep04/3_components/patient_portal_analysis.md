## Overview
The Patient Portal is a secure web interface enabling patients to manage appointments, view electronic medical records (EMR), and handle billing. It drives patient engagement while enforcing strict healthcare compliance standards.

## Key Elements
- Patients (Primary external users)
- Patient Portal (React SPA / UI Container)
- API Gateway (Istio Service Mesh with WAF)
- Identity Provider (OIDC/OAuth2 with MFA)
- Clinical Core (EMR, Scheduling, and Billing services on Kubernetes)
- Edge CDN (Content Delivery Network for static assets)

## Relationships
- Patients -> Patient Portal: Accesses via HTTPS / TLS 1.3 with OAuth2/MFA
- Patient Portal -> API Gateway: Routes requests via mTLS with Istio
- API Gateway -> Clinical Core: Forwards authenticated API calls
- Patient Portal -> Edge CDN: Loads static UI assets

## Technology Stack
- React SPA: Powers the frontend UI with WCAG 2.1 AA accessibility and multi-language support.
- Istio Service Mesh & WAF: Manages traffic routing, mTLS, rate-limiting, and DDoS protection at the edge.
- OAuth2/OIDC & JWT: Provides short-lived access tokens (15 min) and secure session management via HTTP-only cookies.
- Kubernetes & Hybrid Cloud: Ensures active-active high availability (99.99%) across on-prem and AWS (`eu-central-1`).

## Rationale
This architecture uses a secure, decoupled frontend served via a CDN combined with an Istio-managed API gateway to protect sensitive PHI. Active-active hybrid deployments and robust JWT/MFA security mechanisms ensure compliance with HIPAA/GDPR while meeting strict 99.99% availability requirements.