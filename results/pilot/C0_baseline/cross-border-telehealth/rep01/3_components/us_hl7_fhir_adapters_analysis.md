## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and interoperability through regional cloud isolation on GCP.

## Key Elements
* Patients and Licensed Clinicians (Users)
* Flutter Web and Mobile Applications (Containers)
* GCP Cloud Armor, Envoy API Gateway, and Node.js API Gateway (Containers)
* Go Clinical Workspace Service and Go Consent & Localization Engine (Containers)
* mediasoup WebRTC SFU and AI Symptom Checker (Containers)
* US HL7 FHIR Adapters and EU National E-Prescription Formatters (Containers)
* FHIR Resource Mapper, Client Connection Pooler, and Terminology Translator (Components inside US HL7 FHIR Adapters)
* External US HL7 FHIR Engines and National E-Prescription Gateways (External Systems)

## Relationships
* Flutter Applications -> GCP Cloud Armor / Envoy API Gateway: Client requests [HTTPS / WebSockets]
* Go Clinical Workspace Service -> US HL7 FHIR Adapters: Internal payload conversion [gRPC]
* US HL7 FHIR Adapters -> US HL7 FHIR Engines: External health record synchronization [HTTPS / REST / SMART-on-FHIR / mTLS]
* mediasoup SFU -> Patients: Video consultation streaming [WebRTC]

## Technology Stack
* GCP (`us-central1`, `europe-west3`): Cloud provider and regions chosen for strict data residency enforcement.
* Go, Node.js, Python, Rust: Backend services and component languages chosen for high-performance processing and memory safety.
* Flutter: Cross-platform framework for web and mobile client applications.
* mediasoup: WebRTC SFU selected to support video consultations in degraded connection modes (<300 kbit/s).
* HL7 FHIR / SMART-on-FHIR: Interoperability and authorization standards for US healthcare integration.
* GCP Cloud Pub/Sub, Cloud KMS, Cloud Trace: Used for asynchronous queuing, CMEK encryption, and distributed tracing.

## Rationale
The architecture strictly segregates EU and US data within dedicated GCP regions to satisfy GDPR and HIPAA requirements. Isolated container components and resilient integration patterns ensure high availability and auditability across unstable network conditions.