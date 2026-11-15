## Overview
The FHIR Integration Service acts as a high-availability, secure bridge between the internal EMR and external lab/imaging systems. It ensures HIPAA/GDPR-compliant interoperability through standardized HL7 FHIR messaging and robust vendor-specific contract management.

## Key Elements
*   **FHIR Facade Controller:** Handles request validation and routing.
*   **Transformation Engine:** Maps internal schemas to FHIR resources using HAPI FHIR libraries.
*   **Outbox/Message Queue:** Decouples processing using Kafka for asynchronous delivery.
*   **Integration Configuration Manager:** Manages vendor-specific metadata via HashiCorp Consul.
*   **Schema Registry:** Enforces versioned FHIR profile validation (R4/R5).
*   **Sidecar Proxies:** Manages mTLS, logging, and HIPAA audit trails.

## Relationships
*   **EMR Service to Integration Service:** RESTful FHIR APIs for data exchange.
*   **Integration Service to External Systems:** RESTful APIs with mTLS/certificate pinning.
*   **Transformation Engine to Schema Registry:** Validates payloads against versioned HL7 FHIR profiles.
*   **Configuration Manager to Transformation Engine:** Provides dynamic routing and vendor-specific connection secrets.

## Technology Stack
*   **Java/HAPI FHIR:** Core engine for standards-compliant resource mapping.
*   **Kafka:** Asynchronous message backbone with Outbox pattern for data consistency.
*   **HashiCorp Consul:** Centralized KV store for dynamic vendor configuration.
*   **Istio:** Service mesh for mTLS, circuit breaking, and cross-cluster observability.
*   **Prometheus/Grafana:** Integration health monitoring and vendor-specific metrics.
*   **HSM (FIPS 140-2):** Encryption for sensitive vendor credentials and connection metadata.

## Rationale
This architecture ensures 99.99% availability and data integrity by decoupling external dependencies through the Outbox pattern and circuit breakers. The modular design supports heterogeneous vendor maturity levels while maintaining strict security boundaries via mTLS and resource-level authorization.