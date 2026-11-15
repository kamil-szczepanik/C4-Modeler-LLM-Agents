## Overview
The Clinic Management System is a hybrid, high-availability platform designed to manage clinical workflows, patient records, and billing. It ensures HIPAA/GDPR compliance while providing secure access for clinical staff, patients, and auditors.

## Key Elements
*   **Actors:** Clinical Staff, Patients, Auditors/Compliance Officers.
*   **Internal Containers:** EMR Module, Billing Service, Patient Portal, API Gateway, Local EMR Cache.
*   **External Systems:** Identity Provider (IdP), Clearinghouse Gateway, HL7 FHIR Integration Engine.
*   **Infrastructure:** On-premise Kubernetes, AWS (eu-central-1), WORM storage, KMS.

## Relationships
*   **Clinical Staff/Patients to System:** HTTPS/TLS 1.3 via API Gateway.
*   **System to IdP:** OIDC/SAML for MFA and RBAC.
*   **System to Clearinghouse:** REST/SOAP for financial transactions.
*   **System to FHIR Engine:** HL7 FHIR protocols for clinical data exchange.
*   **Inter-service (Hybrid):** mTLS for all cross-boundary communication.

## Technology Stack
*   **Security:** OAuth2/OIDC, AES-256 (at rest), mTLS (in transit), WORM storage for audit logs.
*   **Observability:** Centralized SIEM, distributed tracing for cross-boundary latency.
*   **Infrastructure:** Kubernetes (on-prem/cloud), IaC with automated policy-as-code.
*   **Data Management:** Tiered storage lifecycle management for 10-year retention.

## Rationale
The hybrid architecture and Zero Trust model satisfy the 99.99% availability and strict HIPAA/GDPR data protection requirements. Decoupling external integrations via specific gateways ensures system maintainability and isolates sensitive PHI from volatile third-party protocols.