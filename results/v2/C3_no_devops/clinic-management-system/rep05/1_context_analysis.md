## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to securely manage patient admissions, electronic medical records, scheduling, and billing. It ensures high availability, strict regulatory compliance, and seamless clinical interoperability.

## Key Elements
* **Users:** Patients, Clinical Staff, Administrative Staff, Compliance Officers
* **External Systems:** Lab & Imaging Systems, Payment Gateway & Insurance Clearinghouse, Regulatory & Auditing System
* **Core System Containers:** Edge API Gateway, Patient Portal, Clinic Core Services, EMR Engine, Billing Service
* **Data Storage:** On-Premises Kubernetes Cluster, AWS (eu-central-1)

## Relationships
* **Patients & Staff -> Edge API Gateway:** HTTPS / TLS 1.3, Multi-Factor Authentication (MFA), JWT
* **Clinic Management System <-> Lab & Imaging Systems:** REST/JSON over HTTPS using HL7 FHIR standards with mTLS
* **Clinic Management System -> Payment Gateway:** Secure API / TLS 1.3
* **Clinic Management System -> Regulatory System:** Encrypted SFTP / Signed HTTPS APIs for audit logs

## Technology Stack
* **Kubernetes (on-prem-k8s) & AWS (eu-central-1):** Hybrid cloud infrastructure ensuring 99.99% active-active availability
* **HL7 FHIR REST APIs:** Standardized protocol for interoperability with diagnostic systems
* **AES-256:** Mandatory encryption at rest across all storage tiers for HIPAA/GDPR compliance
* **JWT (RS256/ES256) & OAuth2:** Edge-terminated authentication and token validation for <1s EMR load performance
* **WORM Storage:** Immutable logging infrastructure meeting the 10-year data retention mandate

## Rationale
This hybrid architecture balances strict HIPAA/GDPR security, encryption, and audit constraints with the ultra-low latency demands of clinical workflows. Offloading security validation to an edge gateway guarantees sub-second EMR performance while maintaining high availability.