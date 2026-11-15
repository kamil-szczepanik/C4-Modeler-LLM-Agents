## Overview
[C4 Component Architecture for the E-Prescription & Interoperability Gateway within the Cross-Border Telehealth Platform.]
[Enables secure, compliant, and reliable cross-border e-prescription delivery across EU and US healthcare ecosystems.]

## Key Elements
* Prescription Orchestrator Component (Node.js / TypeScript): Manages internal workflow state and regional dispatch logic.
* EU Translation Adapter Component (Node.js / TypeScript): Translates prescription models into national EU formats.
* US FHIR Adapter Component (Java / Spring Boot): Interoperates with US healthcare systems using HL7 FHIR.
* Audit & Signing Component (Node.js / TypeScript): Cryptographically signs payloads and emits compliance audit events.
* Consent Verification Middleware Component (Node.js / TypeScript): Validates patient consent prior to prescription release.
* Outbound Resilience & Retry Component (Node.js / TypeScript): Implements circuit breaking, backoff, and store-and-forward queueing.

## Relationships
* Prescription Orchestrator -> EU Translation Adapter / US FHIR Adapter: Delegates regional formatting [Internal gRPC]
* Prescription Orchestrator -> Consent Verification Middleware: Validates active patient consent [Internal gRPC]
* Prescription Orchestrator -> Audit & Signing Component: Requests payload digital signature [In-memory function call]
* EU / US Adapters -> Outbound Resilience & Retry Component: Delegates dispatch execution [In-memory async call]
* Consent Verification Middleware -> Consent Management Service: Queries consent tokens [gRPC over mTLS]
* Audit & Signing Component -> Cloud Pub/Sub: Publishes audit events [Cloud Pub/Sub API over TLS]
* Outbound Resilience & Retry Component -> External Pharmacies: Transmits prescriptions [REST / SOAP / XML over TLS 1.3]
* US FHIR Adapter -> National Health Systems: Exchanges FHIR bundles [REST over TLS 1.3]

## Technology Stack
* Node.js / TypeScript: Core language for orchestrators, adapters, and middleware for fast asynchronous I/O.
* Java / Spring Boot: Enterprise framework for US FHIR adapter interoperability.
* Google Cloud Pub/Sub: Asynchronous messaging for audit and compliance event streaming.
* REST / SOAP / XML / HL7 FHIR: Protocols for diverse regional pharmacy and national health integrations.
* TLS 1.3 and mTLS: Secures all internal and external network communication.

## Rationale
[Decomposing the gateway into region-specific adapters and resilient utility components isolates protocol volatility and ensures compliance with EU/US standards.]
[In-memory signing, consent middleware, and store-and-forward queueing guarantee data security, regulatory accountability, and high availability despite unstable rural networks.]