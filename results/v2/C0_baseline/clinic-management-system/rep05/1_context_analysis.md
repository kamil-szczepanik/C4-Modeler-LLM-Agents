## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized clinics and hospitals to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and local-first sub-second performance.

## Key Elements
* **Actors:** Patient, Receptionist / Front Desk, Clinician / Doctor, Billing Specialist
* **Core System:** Clinic Management System (Hybrid Container Architecture)
* **External Systems:** Identity Provider (IdP), External Lab & Imaging Systems, Insurance Clearinghouses, Payment Gateway / Merchant Services
* **Infrastructure & Security:** Secure Hybrid Gateway/VPN Interconnect, SIEM / Observability System, Centralized Vault

## Relationships
* **Patient / Staff -> Clinic Management System:** Accessed via HTTPS, OAuth2/OIDC, and Multi-Factor Authentication (MFA)
* **Clinic Management System -> Identity Provider (IdP):** Manages authentication and IAM via OAuth2/OIDC
* **Clinic Management System -> Lab & Imaging Systems:** Integrates via HL7 FHIR APIs over HTTPS/REST
* **Clinic Management System -> Insurance Clearinghouses & Payment Gateway:** Transmits claims via EDI/HTTPS and processes co-pays via HTTPS/REST
* **On-Prem K8s <-> AWS eu-central-1:** Communicates across the Secure Hybrid Gateway using mTLS/IPsec

## Technology Stack
* **Orchestration:** Kubernetes (deployed on-prem and AWS `eu-central-1`) for active-active 99.99% availability
* **Security:** HashiCorp Vault / AWS Secrets Manager for dynamic secrets; AES-256 at rest and TLS 1.3 in transit
* **Interoperability:** HL7 FHIR and EDI over HTTPS/REST for external system integration
* **Observability:** OpenTelemetry and structured JSON logging feeding into a centralized SIEM for HIPAA-compliant audit trails

## Rationale
This hybrid architecture isolates stateless microservices from stateful data layers to achieve sub-second P95 EMR performance and high availability. Robust security controls, mTLS encryption, and local-first data caching guarantee strict HIPAA and GDPR compliance across regions.