## Overview
The Clinic Management System (CMS) manages patient admissions, EMRs, scheduling, and billing for healthcare clinics. It operates via a hybrid cloud architecture spanning on-premise Kubernetes clusters and AWS (`eu-central-1`).

## Key Elements
* **Actors:** Receptionist / Front Desk, Clinician / Doctor, Billing Specialist, Patient
* **System-of-Interest:** Clinic Management System (CMS)
* **External Systems:** External Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP)
* **Infrastructure:** Global Traffic Manager (GTM), Web Application Firewall (WAF), OpenTelemetry collectors

## Relationships
* **Actors to CMS:** Authenticate via OAuth 2.0 / OIDC and access services exclusively via HTTPS through the Edge WAF.
* **CMS to Lab & Imaging Systems:** Ingest diagnostic results using HL7 FHIR REST APIs over TLS 1.3 with payload signing.
* **CMS to Insurance Clearinghouses:** Submit automated billing claims via secure HTTPS/REST APIs.
* **CMS to IdP:** Validate step-up Multi-Factor Authentication for clinical staff.

## Technology Stack
* **Kubernetes (`on-prem-k8s`):** Local orchestration container for on-premise clinic workloads.
* **AWS (`eu-central-1`):** Cloud region supporting active-active high availability (99.99% uptime).
* **HL7 FHIR & TLS 1.3:** Interoperability standard and transport security for external lab integrations.
* **OAuth 2.0 / OIDC & MFA:** Identity protocols ensuring strict HIPAA/GDPR access compliance.
* **AES-256:** Data-at-rest encryption standard for 10-year data retention compliance.

## Rationale
This hybrid architecture balances strict HIPAA and GDPR data regulations with high availability (99.99% uptime via active-active routing). Standardized HL7 FHIR APIs and secure cloud-edge controls ensure secure, sub-second clinical workflows and interoperability.