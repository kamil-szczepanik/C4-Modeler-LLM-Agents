## Overview
- Secure and compliant Clinic Management System designed for medium-sized hospitals and clinics.
- Manages patient registration, EMR, scheduling, and billing while ensuring strict regulatory compliance.

## Key Elements
- **Users**: Front-Desk Receptionist, Clinician/Doctor, Billing Specialist, Patient, Hospital Administrator, Compliance Officer.
- **External Systems**: External Lab & Imaging Systems, Third-Party Payment & Insurance Gateway, Identity Provider (IdP).
- **Frontend Containers**: Patient Portal Frontend (React), Staff Web Application (React).
- **Backend Containers**: API Gateway (Kong/NGINX Envoy), Core Clinical & EMR Service (Java Spring Boot), Scheduling Service (Node.js/Python), Billing & Claims Service (Java Spring Boot), FHIR Interoperability Adapter (HAPI FHIR), Audit & Compliance Service (Go/Spring Boot).
- **Storage & Security Containers**: PostgreSQL databases, AWS S3 Object Lock (Bucket Policy Manager, Retention Mode Engine, Legal Hold Controller, Lifecycle Transition Manager), HashiCorp Vault.

## Relationships
- **Client to Gateway**: HTTPS/TLS 1.3 traffic from React frontends to API Gateway.
- **Service-to-Service**: gRPC and REST over internal service mesh.
- **Storage Access**: Core Clinical & EMR Service and Audit & Compliance Service communicate with AWS S3 Object Lock via AWS SDK using HTTPS/TLS 1.3 and AWS PrivateLink (VPC Endpoints).
- **Interoperability**: FHIR Interoperability Adapter connects with external lab and imaging systems using HL7 FHIR APIs over HTTPS.
- **Authentication**: OAuth 2.0 / OpenID Connect (OIDC) via external IdP and HashiCorp Vault.

## Technology Stack
- **Languages & Frameworks**: Java Spring Boot, Node.js, Python, Go, React, HAPI FHIR.
- **Infrastructure & Orchestration**: Kubernetes (on-prem-k8s and AWS eu-central-1), Terraform, AWS S3 Object Lock, AWS KMS, AWS PrivateLink.
- **Databases & Storage**: PostgreSQL, AWS S3 Glacier Flexible/Deep Archive.
- **Security**: OAuth 2.0/OIDC, mTLS, AES-256 at rest, AWS IAM Roles for Service Accounts (IRSA), AWS SCPs.

## Rationale
- Hybrid cloud architecture using Kubernetes and AWS provides high availability (99.99%) and active-active scaling across on-premises and cloud regions.
- Strict security controls (AES-256, mTLS, AWS S3 Object Lock WORM storage) satisfy HIPAA, GDPR, and the 10-year data retention mandate.