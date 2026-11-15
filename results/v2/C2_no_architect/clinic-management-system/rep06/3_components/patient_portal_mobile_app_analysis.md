## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing securely. It ensures high availability (99.99%), strict regulatory compliance (HIPAA/GDPR), and seamless interoperability.

## Key Elements
* **Patient Portal / Mobile App**: Mobile and web interface for patient self-registration, appointment booking, and EMR access.
* **API Gateway**: Entry point handling OAuth2/OIDC, ABAC, TLS termination, and request routing.
* **Backend Services**: EMR Service and Billing / Claims Service deployed on Kubernetes.
* **Security & Observability**: HashiCorp Vault, OpenTelemetry sidecars, and WORM audit logging.
* **External Systems**: Insurance/Payer Systems and Lab & Imaging Systems via HL7 FHIR.

## Relationships
* Patient -> Patient Portal / Mobile App: Accesses portal and mobile application [HTTPS/TLS via API Gateway]
* Patient Portal / Mobile App -> API Gateway: Routes authenticated requests [HTTPS/TLS with W3C Trace Context headers]
* API Gateway -> EMR Service: Directs internal clinical traffic [gRPC/REST over mTLS, SPIFFE/SPIRE]
* Backend Services -> HashiCorp Vault: Fetches dynamic secrets [Encrypted API]

## Technology Stack
* **Client Apps**: React Native / Flutter with local SQLite encrypted via iOS Keychain/Android EncryptedSharedPreferences (AES-256).
* **Gateway & Auth**: OAuth2/OIDC with PKCE, API Gateway with WAF and rate limiting.
* **Orchestration**: Kubernetes (on-prem-k8s and AWS eu-central-1).
* **Observability**: OpenTelemetry with W3C Trace Context propagation and RUM.
* **Interoperability**: HL7 FHIR APIs for external lab/imaging integration.

## Rationale
This architecture uses a hybrid cloud model to balance data residency constraints with elastic scalability for high availability. Rigorous security protocols (mTLS, AES-256, secure enclaves) ensure strict HIPAA/GDPR compliance without compromising sub-second performance.