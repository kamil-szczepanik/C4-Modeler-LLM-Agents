## Overview
The Clinic Management System is a hybrid cloud platform managing patient registrations, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability clinical workflows while ensuring strict HIPAA and GDPR compliance.

## Key Elements
* Front Desk Administrators, Clinicians, Billing Specialists, and Patients
* Web Client & Patient Portal (SPA/Mobile)
* API Gateway with OAuth 2.0/OIDC and mTLS
* Core Microservices (Patient Registration, Scheduling Engine, EMR, Billing & Claims)
* External Lab & Imaging Systems via HL7 FHIR APIs
* Data Storage Tier (Immutable WORM storage, AES-256 encrypted databases)

## Relationships
* Users interact with Web Client via HTTPS (TLS 1.3)
* Web Client communicates with API Gateway via REST/GraphQL over HTTPS
* API Gateway routes requests to Core Microservices using gRPC/REST over mTLS
* Core Microservices interact with database tier via encrypted SQL/NoSQL protocols
* System integrates with External Lab Systems via HL7 FHIR APIs over mTLS

## Technology Stack
* Kubernetes (on-prem-k8s and AWS eu-central-1): Active-active hybrid deployment supporting 99.99% uptime
* OAuth 2.0 / OpenID Connect (OIDC): Secures patient portal authentication and role-based access control
* HL7 FHIR: Standardizes interoperability with external lab and imaging systems
* AES-256 & HSM: Secures data at rest and ephemeral caches with customer-managed keys
* WORM (Write-Once-Read-Many) Storage: Satisfies 10-year regulatory data retention mandates

## Rationale
The active-active hybrid Kubernetes architecture guarantees 99.99% availability and local survivability during WAN outages. Comprehensive encryption, mTLS, and WORM storage fulfill rigorous HIPAA and GDPR security and compliance requirements.