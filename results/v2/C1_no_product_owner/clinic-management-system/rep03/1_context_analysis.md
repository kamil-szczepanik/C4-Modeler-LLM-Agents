## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely manage patient admissions, electronic medical records, scheduling, and billing. It provides high availability, stringent compliance, and robust interoperability for healthcare operations.

## Key Elements
* **Actors:** Patient, Clinician, Receptionist, Billing Specialist
* **Core System:** Clinic Management System (CMS) deployed across hybrid infrastructure (`on-prem-k8s` and AWS `eu-central-1`)
* **Perimeter Services:** API Gateway / Edge Proxy (on-prem and AWS perimeters)
* **External Systems:** Third-Party Payment Gateway, External Lab & Imaging Systems, Insurance Clearinghouse, Enterprise IdP
* **Data & Storage:** AES-256 encrypted databases, WORM storage tier with HSM-backed Customer-Managed Keys (CMKs)

## Relationships
* **Actors to API Gateway:** Patients, Clinicians, Receptionists, and Billing Specialists connect via HTTPS/REST using OAuth2/OIDC with MFA.
* **External Systems to API Gateway:** External Lab & Imaging Systems integrate via HL7 FHIR over HTTPS; Payment Gateway and Insurance Clearinghouse connect via REST/SFTP.
* **Internal Routing:** API Gateways route validated traffic to internal CMS services across the hybrid boundary using mTLS over TLS 1.3.

## Technology Stack
* **Orchestration & Infrastructure:** Kubernetes (`on-prem-k8s`, AWS `eu-central-1`) for active-active multi-region scalability.
* **Security & Auth:** OAuth2/OIDC, mTLS (TLS 1.3), HSM-backed CMKs, AES-256 for data at rest.
* **Interoperability:** HL7 FHIR APIs for lab and imaging systems.
* **Data & Retention:** WORM cloud storage tiers for immutable 10-year data retention compliance.

## Rationale
The hybrid architecture balances data residency requirements on-premises with cloud scalability in AWS to achieve 99.99% availability. Strict zero-knowledge encryption, mTLS, and immutable WORM storage ensure full compliance with HIPAA and GDPR regulations.