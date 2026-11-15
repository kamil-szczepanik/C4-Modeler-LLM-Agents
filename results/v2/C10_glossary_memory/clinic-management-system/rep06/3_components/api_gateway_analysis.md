## Overview
The Clinic Management System is a hybrid-cloud healthcare platform providing patient admissions, electronic medical records, scheduling, and billing. It ensures HIPAA/GDPR compliance, high availability (99.99%), and sub-second EMR performance.

## Key Elements
- Patients, Receptionists/Admins, Clinicians/Doctors, Billing Specialists, Compliance/Security Officers, Hospital/Clinic Management
- External Identity Provider (IdP), External Lab & Imaging Systems, Insurance Clearinghouse
- Patient Portal (React / TypeScript, Nginx)
- Internal Staff Application (React / TypeScript, Nginx)
- API Gateway (Kong / Envoy) with Routing Engine, Authentication & Authorization Filter (Lua / WASM), and Rate Limiting & Throttling Module
- Patient Admission Service (Go / Node.js)
- Scheduling Service (Go / Node.js)
- EMR Service (Go / Node.js)
- Billing Service (Java Spring Boot)
- Integration Engine (Go / Node.js)
- Data Store (PostgreSQL, WORM Object Storage, Distributed Cache / Redis)

## Relationships
- Patient Portal -> API Gateway: Sends API requests [HTTPS (mTLS/OIDC)]
- Internal Staff Application -> API Gateway: Sends API requests [HTTPS (mTLS/OIDC)]
- API Gateway -> Patient Admission Service / Scheduling Service / EMR Service / Billing Service / Integration Engine: Routes requests [gRPC / REST over internal mesh]
- Authentication & Authorization Filter -> External Identity Provider (IdP): Validates tokens and fetches JWKS [HTTPS]
- Rate Limiting & Throttling Module -> Distributed Cache: Evaluates rate limits [Redis Protocol]
- Patient Admission Service / Scheduling Service / EMR Service / Billing Service -> Data Store: Persists data [PostgreSQL protocol with AES-256]
- Integration Engine -> External Lab & Imaging Systems: Exchanges health data [HL7 FHIR over HTTPS with mTLS]
- Integration Engine -> Insurance Clearinghouse: Submits claims [EDI over SFTP / HTTPS]

## Technology Stack
- React / TypeScript & Nginx: Frontend delivery for patient and internal portals
- Kong / Envoy: Edge API Gateway for routing, mTLS, and token validation
- Lua / WASM: Extensible filtering for OIDC token validation and RBAC/ABAC enforcement
- Redis: Distributed cache backing the rate-limiting module with fail-open availability
- Go / Node.js & Java Spring Boot: High-performance microservices backend
- PostgreSQL & WORM Object Storage: Core relational persistence and 10-year audit retention with AES-256 encryption
- HashiCorp Vault: Secret management for mTLS keys and signing secrets

## Rationale
The hybrid-cloud architecture isolates sensitive workloads while leveraging scalable Kubernetes clusters on-prem and in `eu-central-1`. Strict edge security via Kong/Envoy and robust microservices separation satisfy stringent HIPAA/GDPR compliance and 99.99% availability targets.