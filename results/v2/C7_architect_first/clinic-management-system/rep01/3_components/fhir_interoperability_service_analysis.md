## Overview
The FHIR Interoperability Service handles secure healthcare data exchange for the Clinic Management System using open standards. It operates in a hybrid Kubernetes environment (`on-prem-k8s` and `eu-central-1`) to ensure HIPAA/GDPR compliance and high availability.

## Key Elements
- **FHIR REST Controller (Java/Spring MVC):** Exposes FHIR R4/R5 endpoints and validates OAuth 2.0 / SMART-on-FHIR scopes.
- **Resource Mapping Engine (HAPI FHIR / Java):** Translates internal EMR models to FHIR JSON/XML, prioritizing patient-facing reads.
- **Audit & Compliance Interceptor (Java):** Captures transactions and enforces redacted, HIPAA-compliant access logs.
- **FHIR Message Queue Broker (NATS JetStream):** Buffers asynchronous FHIR bundles with AES-256 encrypted persistent volumes.
- **External Integration Client (Apache HttpClient/WebClient):** Manages outbound communication with external lab and imaging systems.

## Relationships
- **FHIR REST Controller -> Resource Mapping Engine:** Delegates payload transformation [In-memory Java Method Calls]
- **Resource Mapping Engine -> Audit & Compliance Interceptor:** Emits transaction audit events [Spring Application Events]
- **FHIR REST Controller -> FHIR Message Queue Broker:** Offloads asynchronous FHIR ingestion [AMQP/NATS]
- **FHIR Message Queue Broker -> External Integration Client:** Feeds queued outbound transactions [AMQP/NATS]
- **External Integration Client -> External Lab & Imaging Systems:** Exchanges clinical data [HTTPS / mTLS with client certificate pinning]

## Technology Stack
- **Java / Spring Boot / HAPI FHIR:** Chosen for robust, standardized healthcare interoperability and enterprise maturity.
- **NATS JetStream:** Selected as a lightweight, Kubernetes-native message broker to handle async buffering across hybrid clouds without heavy operational overhead.
- **HashiCorp Vault / AWS KMS:** Used for managing AES-256 keys to secure data at rest and persistent volumes.
- **OAuth 2.0 / OIDC & SMART-on-FHIR:** Implemented for fine-grained, role- and attribute-based access control.

## Rationale
This architecture decouples heavy interoperability workloads from the core EMR to maintain <1s P95 UI response times. Asynchronous message queuing and robust security controls ensure compliance, resilience during vendor outages, and patient safety.