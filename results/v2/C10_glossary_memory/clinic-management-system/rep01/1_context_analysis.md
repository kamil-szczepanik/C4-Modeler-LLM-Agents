## Overview
The Clinic Management System (CMS) manages patient admissions, EMRs, scheduling, and billing for healthcare facilities while ensuring strict HIPAA/GDPR compliance and 99.99% availability. It utilizes a hybrid cloud architecture spanning on-premises Kubernetes and AWS (`eu-central-1`).

## Key Elements
* **Users:** Patients, Clinicians / Medical Staff, Administrative / Billing Staff
* **Core System:** Clinic Management System (CMS) Software System
* **External Systems:** External Labs/Imaging, Insurance Payment Gateways, Identity Provider (IdP)
* **Infrastructure:** API Gateway, Hardware Security Module (HSM), WORM Audit Logging Service

## Relationships
* **Human Users to CMS:** HTTPS (TLS 1.3), OAuth 2.0 / OIDC, enforcing MFA
* **External Labs/Imaging to CMS:** HL7 FHIR RESTful APIs over HTTPS
* **Insurance Payment Gateways to CMS:** Secure API webhooks / REST
* **CMS to Infrastructure:** mTLS (Mutual TLS 1.3), Zero Trust Network Access (ZTNA)

## Technology Stack
* **Container Orchestration:** Kubernetes (`on-prem-k8s`) and AWS (`eu-central-1`) for hybrid active-active scaling
* **Security & Encryption:** FIPS 140-2 validated Hardware Security Module (HSM) and AES-256 for data at rest and in transit
* **Identity & Access Management:** OAuth 2.0 / OpenID Connect (OIDC) via IdP for federation and step-up MFA
* **Interoperability:** HL7 FHIR RESTful APIs for clinical system integration

## Rationale
* The hybrid active-active architecture with strict RTO/RPO targets ensures the required 99.99% availability and disaster recovery resilience.
* Asynchronous WORM auditing, hardware cryptographic acceleration, and decoupled security controls protect sensitive PHI while preserving sub-second EMR performance (<1s P95).