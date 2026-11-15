## Overview
The Clinic Management System is a hybrid clinical IT platform that manages patient admissions, electronic medical records, appointment scheduling, and billing. It provides high availability, stringent compliance, and seamless interoperability for healthcare providers.

## Key Elements
- **Users:** Patients, Clinicians, and Hospital Administrators.
- **External Systems:** Identity Provider (IdP), External Lab & Imaging Systems, and Payment Gateways/Insurance Clearinghouses.
- **Containers:** On-premises Kubernetes clusters for latency-critical EMR workflows, AWS eu-central-1 containers for scalable portal and billing traffic, and a service mesh.

## Relationships
- Users access the system via HTTPS/TLS 1.3 using OAuth2/JWT tokens issued by the IdP.
- The system connects to External Lab & Imaging Systems via RESTful HL7 FHIR over mutual TLS (mTLS).
- On-premises and cloud environments communicate via an encrypted IPsec VPN / AWS Direct Connect hybrid link.

## Technology Stack
- **Orchestration:** Kubernetes (on-prem-k8s and AWS eu-central-1) for container management and GitOps (ArgoCD) for deployment parity.
- **Interoperability:** HL7 FHIR APIs for standardized clinical data exchange.
- **Security:** AES-256 encryption at rest, Istio/Linkerd service mesh for internal mTLS, and HashiCorp Vault / AWS Secrets Manager for runtime secrets.
- **Networking:** AWS Route 53 for active-active global Anycast routing.

## Rationale
The hybrid cloud architecture balances ultra-low latency on-premises for clinical EMR performance with cloud scalability for billing workloads. Strict multi-layer security, WORM storage, and multi-region replication ensure continuous HIPAA/GDPR compliance and 99.99% availability.