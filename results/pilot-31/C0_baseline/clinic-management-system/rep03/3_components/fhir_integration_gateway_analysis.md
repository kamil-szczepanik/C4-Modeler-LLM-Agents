## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage patient records, scheduling, and billing while ensuring HIPAA/GDPR compliance. It utilizes a high-availability architecture to facilitate secure, bi-directional clinical data exchange with external diagnostic systems.

## Key Elements
*   **FHIR Integration Gateway:** HAPI FHIR-based proxy for external diagnostic interoperability.
*   **Transformation Engine:** Rule-based (JOLT/Liquid) engine for mapping internal models to HL7 FHIR R4.
*   **Metadata Registry:** Centralized store for versioned, cryptographically signed FHIR profiles and templates.
*   **Audit & Reconciliation Service:** Monitors clinical data integrity and manages "soft failure" exceptions.
*   **Partner Configuration Portal:** UI for non-technical staff to manage diagnostic partner connections.
*   **Queue Manager:** NATS JetStream-based messaging for asynchronous data flow.

## Relationships
*   **External Diagnostic Systems <-> FHIR Integration Gateway:** Bi-directional exchange via HL7 FHIR R4 over mTLS.
*   **Gateway <-> Metadata Registry:** Runtime retrieval of signed transformation templates.
*   **Gateway <-> Audit & Reconciliation Service:** Event-based ingestion of payloads for clinical integrity monitoring.
*   **Partner Configuration Portal -> Metadata Registry:** Management of partner-specific onboarding configurations.

## Technology Stack
*   **HAPI FHIR:** Core framework for FHIR R4 compliance and interoperability.
*   **JOLT/Liquid:** Rule-based transformation engine for decoupled mapping logic.
*   **NATS JetStream:** High-throughput, resilient messaging for asynchronous integration.
*   **Redis:** Caching layer for FHIR Capability Statements and schema profiles.
*   **Cloud KMS/HSM:** Secure management of cryptographic keys for template signing.
*   **Sidecar Proxy:** Handles mTLS termination and circuit breaking for network resilience.

## Rationale
This architecture uses a decoupled, configuration-driven approach to enable rapid partner onboarding while maintaining 99.99% uptime through stateless execution and circuit breakers. The separation of metadata from the runtime engine ensures clinical data integrity and auditability required for strict healthcare compliance.