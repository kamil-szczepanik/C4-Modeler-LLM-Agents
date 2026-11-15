## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The E-Prescription & Interoperability Service manages prescription lifecycles, regional format translations, and secure pharmacy dispatch.]

## Key Elements
- Prescription Orchestrator Component
- US FHIR Adapter Component
- EU National Gateway Adapter Component
- Prescription Status & Audit Component
- Google Cloud Pub/Sub
- Cloud SQL PostgreSQL
- GCP KMS & Cloud Storage WORM

## Relationships
- API Gateway -> Prescription Orchestrator: Invokes prescription creation [gRPC]
- Prescription Orchestrator -> US FHIR Adapter / EU Gateway Adapter: Delegates payload transformation [Internal Java Interfaces]
- US FHIR Adapter / EU Gateway Adapters -> External Pharmacies: Dispatches messages [HTTPS, REST, HL7 FHIR over mTLS]
- US FHIR Adapter / EU Gateway Adapters -> Prescription Status & Audit: Publishes delivery status updates [Google Cloud Pub/Sub]
- Prescription Status & Audit -> Data Storage Layer: Persists audit logs and status changes [SSL-enforced TCP, PostgreSQL]

## Technology Stack
- Java / Spring Boot: Enterprise integration and robust ecosystem support for adapters
- Resilience4j: Circuit breakers for handling external pharmacy downtime
- Google Cloud Pub/Sub: At-least-once asynchronous event delivery with partition ordering
- GCP KMS: Envelope encryption for secure data-at-rest and event payload protection
- Cloud Storage WORM: Tamper-resistant immutable audit logging

## Rationale
[This modular, event-driven architecture guarantees region-specific data residency (EU/US) while ensuring zero prescription loss through Dead Letter Queues and durable messaging. Pluggable regional adapters and strict mTLS integration provide the necessary compliance, security, and interoperability required for cross-border healthcare delivery.]