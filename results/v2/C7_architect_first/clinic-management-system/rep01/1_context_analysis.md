## Overview
[The Clinic Management System (CMS) manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability, HIPAA- and GDPR-compliant clinical IT operations across a hybrid cloud infrastructure.]

## Key Elements
- Patients & Clinical Staff (Doctors, Nurses, Receptionists)
- System Administrators
- Clinic Management System (CMS) core
- External Lab & Imaging Systems
- Payment Gateway & Insurance Clearinghouse
- External Identity Provider (IdP)

## Relationships
- Patients & Clinical Staff to CMS via HTTPS/TLS 1.3 (Web/Mobile)
- CMS to External Lab & Imaging Systems via HL7 FHIR (REST over HTTPS)
- CMS to Payment Gateway & Insurance Clearinghouse via secure REST APIs
- CMS to External IdP via OIDC/OAuth2 for authentication and MFA
- Inter-environment and service-to-service communication secured via mTLS (TLS 1.3)

## Technology Stack
- Hybrid Cloud (On-premise Kubernetes clusters and AWS eu-central-1) for high availability
- API Gateway & Web Application Firewall (WAF) for traffic security and threat mitigation
- Distributed database layer with synchronous/asynchronous replication for active-active data management
- ArgoCD for GitOps-based infrastructure management
- AES-256 encryption at rest with regional KMS for data sovereignty

## Rationale
[This hybrid architecture guarantees 99.99% active-active uptime and sub-second EMR performance while strictly enforcing EU data residency and HIPAA/GDPR compliance. Split ingress channels and dedicated security gateways isolate patient and clinical workflows, protecting sensitive health records and revenue cycles.]