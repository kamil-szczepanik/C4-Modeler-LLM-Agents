## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage clinical workflows, patient records, and billing. It ensures high availability and regulatory compliance for healthcare providers while supporting patient engagement and administrative analytics.

## Key Elements
*   **Users:** Clinical Staff, Patients, Hospital Administrators.
*   **Core Systems:** EMR Core (On-premise), Patient Portal, Admin Analytics Dashboard.
*   **Infrastructure:** Centralized API Gateway, Data Synchronization Service, Asynchronous Data Warehouse.
*   **External Dependencies:** Identity Provider (IdP), Secure Payment Gateway, External Diagnostic Systems (Lab/Imaging).
*   **Security Components:** WAF, KMS/HSM, Immutable Storage.

## Relationships
*   **API Gateway:** Manages ingress from all actors using mTLS and ABAC.
*   **EMR Core ↔ Diagnostic Systems:** HL7 FHIR protocol for interoperability.
*   **EMR Core ↔ Data Warehouse:** ETL process with data masking for reporting.
*   **On-premise ↔ Cloud:** Data Synchronization Service with automated failover and circuit breakers.

## Technology Stack
*   **Kubernetes (K8s):** Orchestration for hybrid deployment (on-prem/cloud).
*   **HL7 FHIR:** Standard for clinical data exchange.
*   **AES-256:** Mandatory encryption at rest for PHI/PII.
*   **mTLS:** Required for all traffic traversing the synchronization service.
*   **ABAC:** Attribute-Based Access Control for granular security.
*   **WAF:** Edge protection against OWASP Top 10.
*   **KMS/HSM:** Key management for compliance and encryption.

## Rationale
The hybrid architecture ensures 99.99% availability by allowing autonomous on-premise operation during network partitions. Decoupling the EMR core from analytics and patient portals via an asynchronous data warehouse and API gateway preserves P95 performance while maintaining strict HIPAA/GDPR compliance.