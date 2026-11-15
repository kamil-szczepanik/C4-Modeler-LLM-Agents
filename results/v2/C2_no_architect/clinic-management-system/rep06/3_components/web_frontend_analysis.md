## Overview
The Clinic Management System is a clinical IT platform that manages patient admissions, EMR, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and 10-year data retention across hybrid environments.

## Key Elements
- Patients, Clinicians, Receptionists, Billing Specialists, Compliance Officers
- Web Frontend (BFF & Static Assets)
- API Gateway (OAuth2/OIDC, ABAC)
- EMR Service, Billing / Claims Service
- OpenTelemetry & Audit Logging sidecars
- HashiCorp Vault, Redis Token Blacklist
- on-prem-k8s cluster, AWS (eu-central-1)

## Relationships
- Users -> Web Frontend: Access via browser [HTTPS/TLS via API Gateway]
- Web Frontend -> API Gateway: Routes requests [HTTPS/TLS]
- Internal Microservices -> Internal Services: Inter-service communication [gRPC/REST over mTLS, SPIFFE/SPIRE]

## Technology Stack
- Frontend/BFF: Kubernetes-backed SSR/BFF with CDN caching for <1s P95 EMR rendering and WCAG 2.1 AA compliance
- Security: OAuth2/OIDC with `HttpOnly`, `Secure`, `SameSite=Strict` cookies, DOMPurify, and TLS 1.3
- Infrastructure: Hybrid deployment on `on-prem-k8s` and AWS `eu-central-1` for active-active 99.99% uptime
- Observability: OpenTelemetry and Real User Monitoring (RUM) for performance tracking

## Rationale
This hybrid architecture combines active-active regional redundancy with strict zero-trust security controls to meet 99.99% availability and stringent healthcare compliance mandates. The BFF pattern ensures fast client-side rendering while centralizing security token handling.