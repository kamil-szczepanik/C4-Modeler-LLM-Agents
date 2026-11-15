## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict regulatory compliance, and seamless interoperability with external clinical systems.

## Key Elements
- **Users**: Patient, Clinician/Doctor, Receptionist/Admin, Billing Specialist, Compliance Officer
- **Software System**: Clinic Management System (CMS)
- **External Systems**: Enterprise Identity Provider (IdP), External Labs & Imaging Systems, Insurance Claim Gateways
- **Infrastructure**: Hybrid Kubernetes (on-premise and AWS `eu-central-1`)

## Relationships
- Users interact with CMS via HTTPS (Web/Mobile)
- CMS authenticates with Enterprise IdP via OIDC/SAML
- CMS integrates with External Labs & Imaging Systems via HL7 FHIR / REST over TLS with mTLS
- CMS communicates with Insurance Claim Gateways via HTTPS/REST with asynchronous queuing and circuit breakers
- Hybrid clusters synchronize data via secure IPsec VPN tunnels

## Technology Stack
- **Backend**: C# / .NET Core for core business logic and high-performance EMR processing
- **Orchestration**: Kubernetes for hybrid container deployment across on-prem and AWS `eu-central-1`
- **Security & Mesh**: Istio/Linkerd for container mTLS, HashiCorp Vault for secrets management, OIDC/SAML for enterprise SSO
- **Interoperability**: HL7 FHIR protocols for standardized healthcare data exchange

## Rationale
The hybrid architecture balances strict on-premise data residency requirements with the scalability of AWS `eu-central-1` to achieve 99.99% active-active availability. Robust encryption, mTLS service meshes, and immutable audit logging satisfy stringent HIPAA and GDPR compliance mandates.