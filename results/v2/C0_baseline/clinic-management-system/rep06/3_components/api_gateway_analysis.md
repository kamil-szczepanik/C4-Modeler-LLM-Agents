## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It provides secure, high-availability clinical workflows and regulatory compliance.

## Key Elements
- **Users**: Front-Desk Receptionist, Clinician/Doctor, Billing Specialist, Patient, Hospital Administrator, Compliance Officer.
- **External Systems**: External Lab & Imaging Systems, Third-Party Payment & Insurance Gateway, Identity Provider (IdP).
- **Containers**: API Gateway (Kong/NGINX/Envoy), Patient Portal Frontend (React), Staff Web Application (React), Core Clinical & EMR Service (Java Spring Boot), Scheduling Service (Node.js/Python), Billing & Claims Service (Java Spring Boot), FHIR Interoperability Adapter (HAPI FHIR), Audit & Compliance Service, PostgreSQL databases, AWS S3, HashiCorp Vault.
- **API Gateway Components**: Edge TLS Termination & WAF Proxy, Authentication & JWT Validation Filter, Routing & Rate-Limiting Engine, API Developer Portal & Consumer Registry, Dynamic Service Discovery & Upstream Resolver.

## Relationships
- Patient Portal Frontend -> API Gateway: Makes API requests [HTTPS/REST]
- Staff Web Application -> API Gateway: Makes API requests [HTTPS/REST]
- API Gateway -> Core Clinical & EMR Service: Routes EMR requests [OAuth2/OIDC, mTLS]
- API Gateway -> Scheduling Service: Routes scheduling requests [OAuth2/OIDC, mTLS]
- API Gateway -> Billing & Claims Service: Routes billing requests [OAuth2/OIDC, mTLS]
- API Gateway -> FHIR Interoperability Adapter: Routes lab/imaging requests [OAuth2/OIDC, mTLS]
- API Gateway -> Identity Provider: Token introspection/validation [HTTPS/OIDC]

## Technology Stack
- **API Gateway**: Kong/NGINX/Envoy for edge routing, WAF, and tenant-aware rate limiting.
- **Frontend**: React for Patient Portal and Staff Web Application.
- **Backend Services**: Java Spring Boot (Core Clinical & EMR, Billing & Claims), Node.js/Python (Scheduling), Go/Spring Boot (Audit).
- **Interoperability**: HAPI FHIR for HL7 FHIR APIs.
- **Security & Infrastructure**: TLS 1.3, mTLS, OAuth2/OIDC, AES-256 at rest, HashiCorp Vault for cert lifecycle management, AWS S3 Object Lock for data retention.
- **Deployment**: Hybrid Kubernetes (`on-prem-k8s` and `eu-central-1`) with active-active routing.

## Rationale
This architecture ensures 99.99% high availability through active-active hybrid cloud deployments and resilient routing. It strictly enforces HIPAA and GDPR compliance via end-to-end mTLS, AES-256 encryption, edge PHI scrubbing, and immutable audit logging.