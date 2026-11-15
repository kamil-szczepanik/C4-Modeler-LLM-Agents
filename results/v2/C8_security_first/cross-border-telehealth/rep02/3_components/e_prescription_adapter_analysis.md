## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and resilient cross-border integrations.

## Key Elements
* Patients & Licensed Clinicians (Users)
* Local Pharmacies, Identity Providers (IdP), AI Triage Engine (External Systems)
* Istio Service Mesh & API Gateway (Istio)
* Backend-for-Frontend (BFF) (Node.js, GraphQL)
* Mediasoup SFU (Mediasoup WebRTC)
* AI Triage Service & Consent Manager (Containerized Services)
* E-Prescription Adapter (Containerized Service containing Prescription Router, Outbox Processor, Gateway Client, Status Notification, and Audit Logging components)
* Regional WORM Storage (GCP Storage)

## Relationships
* Backend-for-Frontend (BFF) -> E-Prescription Adapter: Transmits prescription requests [gRPC over mTLS via Istio]
* Prescription Router -> Outbox Processor: Enqueues messages [Internal Async]
* Outbox Processor -> Gateway Client: Dispatches queued payloads [Internal Event]
* Gateway Client -> Local Pharmacies: Transmits signed payloads [TLS 1.3, HL7 FHIR/REST/SOAP]
* Outbox Processor -> Status Notification: Dispatches delivery state changes [Internal Event]
* Status Notification -> BFF: Pushes status receipts and error codes [gRPC Stream]
* Outbox Processor -> Audit Logging: Forwards immutable event logs [Internal Async]
* Audit Logging -> Regional WORM Storage: Writes compliance logs [GCP Storage API, TLS 1.3]

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Target cloud provider for regional data isolation and compliance.
* Istio Service Mesh: Manages secure internal service-to-service communication via mTLS.
* Node.js / TypeScript: Core runtime for microservices and the E-Prescription Adapter.
* HL7 FHIR & REST/SOAP: Interoperability protocols for US and EU national pharmacy networks.
* GCP Cloud KMS with CMEK: Enforces regional encryption-at-rest key segregation.

## Rationale
This architecture guarantees strict regional data residency and compliance using isolated GCP regions and regional CMEK keys. It ensures fault-tolerant, reliable cross-border e-prescription delivery to unstable pharmacy endpoints via the Transactional Outbox pattern and Dead-Letter Queues.