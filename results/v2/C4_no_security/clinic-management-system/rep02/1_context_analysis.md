## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMRs, scheduling, and billing for clinical environments. It ensures HIPAA/GDPR compliance, 99.99% availability, and sub-second EMR performance across distributed deployments.

## Key Elements
* **Actors:** Patients, Clinical Staff, Administrative Staff, Billing & Finance Officers, System/Compliance Administrators.
* **Clients:** Web Browsers, Patient Mobile App.
* **Core System:** Clinic Management System (Hybrid Kubernetes containers across `on-prem-k8s` and `eu-central-1`).
* **External Systems:** External Lab & Imaging Systems, Third-Party Payment Gateway & Insurance Clearinghouse, Identity Provider (IdP), Audit & Compliance SIEM.

## Relationships
* **Clients to Core:** HTTPS/TLS 1.3 for web and mobile interactions.
* **Core to Identity Provider:** OAuth2/OIDC for Multi-Factor Authentication (MFA) and Enterprise SSO.
* **Core to Labs/Imaging:** HL7 FHIR REST APIs over HTTPS.
* **Core to Payment/Insurance:** Secure REST APIs over HTTPS.
* **Core to SIEM:** Secure syslog/HTTPS for immutable log streaming.
* **Inter-Environment:** Dedicated VPN/Direct Connect tunnels between `on-prem-k8s` and `eu-central-1`.

## Technology Stack
* **Orchestration & Cloud:** Hybrid Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) for active-active high availability (99.99% uptime).
* **Security & Auth:** OAuth2/OIDC via external Identity Provider; AES-256 encryption at rest.
* **Interoperability:** HL7 FHIR protocol for clinical data exchange.
* **Routing & Resilience:** Global Anycast DNS with automated health checks for split-brain prevention and failover.

## Rationale
This architecture uses hybrid Kubernetes with dedicated VPN tunnels and Anycast DNS routing to achieve 99.99% availability while keeping latency under 1 second. Offloading authentication to OIDC, logging to an external SIEM, and applying AES-256 encryption ensures strict HIPAA and GDPR compliance.