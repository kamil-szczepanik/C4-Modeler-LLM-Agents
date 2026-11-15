## Overview
The Clinic Management System is a hybrid healthcare platform designed to manage patient admissions, EMRs, scheduling, and billing for clinics. It ensures high availability, strict HIPAA/GDPR compliance, and interoperability across on-premise Kubernetes and AWS.

## Key Elements
- **Users**: Patients, Receptionists, Attending Physicians, Billing Specialists, Clinic Administrators.
- **Core System**: Clinic Management System (Hybrid: On-premise K8s & AWS eu-central-1).
- **External Systems**: Identity Provider (OAuth2/OIDC), Third-Party Payment Gateways/Clearinghouses, External Laboratory & Imaging Systems.
- **Containers/Services**: Patient Portal, EMR Service, Scheduling Service, Billing Service, API Gateway, Service Mesh.

## Relationships
- **Users to API Gateway**: HTTPS/TLS 1.3, Multi-Factor Authentication (MFA).
- **Core System to Identity Provider**: OAuth2/OIDC for authentication and access control.
- **Core System to External Lab/Imaging**: HL7 FHIR APIs over mutual TLS (mTLS).
- **Core System to Payment Gateways**: REST/HTTPS for insurance claims and billing.
- **Internal Cross-Environment**: Enterprise Service Mesh using mTLS for hybrid traffic routing.

## Technology Stack
- **Infrastructure**: Hybrid Cloud (On-premise Kubernetes and AWS `eu-central-1`) for active-active high availability.
- **Networking & Security**: TLS 1.3, mutual TLS (mTLS), OAuth2/OIDC, RBAC/ABAC authorization.
- **Data & Storage**: AES-256 encryption at rest, hardware-backed KMS, WORM cloud storage for audit logs, local read-replicas.
- **Observability**: OpenTelemetry for distributed tracing.

## Rationale
This hybrid architecture uses local on-premise read-replicas to achieve sub-second EMR performance while leveraging AWS for scalable billing and disaster recovery. Stringent cryptographic controls and WORM storage ensure 10-year immutable audit retention while satisfying HIPAA, GDPR, and 99.99% uptime requirements.