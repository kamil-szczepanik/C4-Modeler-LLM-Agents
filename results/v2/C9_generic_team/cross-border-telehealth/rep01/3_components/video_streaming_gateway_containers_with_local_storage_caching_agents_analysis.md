## Overview
Cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across EU and US regions. Enforces strict regional data residency, GDPR/HIPAA compliance, and resilient streaming for unstable rural connections.

## Key Elements
* Patients and Clinicians (End Users)
* Global Traffic Director / API Gateway (GCP Ingress / Envoy)
* Stateless Core Application Containers & Video Streaming Gateway Containers with Local Storage/Caching Agents (GCP)
* AI Inference & Audit Proxy Containers (Python / gRPC)
* FHIR Translation Adapter (US) and National E-Prescription Adapter (EU)
* Regional Audit and Compliance Logging Subsystem

## Relationships
* Patients and Clinicians -> Global Traffic Director: HTTPS / WebRTC
* Video Streaming Gateway -> Regional Object Storage: Encrypted Store-and-Forward chunk flushing [HTTPS / GCP Persistent Disk]
* AI Inference & Audit Proxy -> Regional Audit Subsystem: Structured Correlation ID logging [gRPC]

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Target cloud provider ensuring regional data isolation
* WebRTC & TURN/STUN: Real-time video consultation protocols
* Python / gRPC: AI symptom checker and microservices communication
* HL7 FHIR & National APIs: Interoperability standards for US and EU prescriptions
* GCP Persistent Disk Encryption: Secures local caching volumes for PHI/PII compliance

## Rationale
Containerized edge architectures with Store-and-Forward patterns maintain consultation availability under unstable 300 kbit/s connections. Strict encryption, localized processing, and decoupled isolation patterns ensure full GDPR/HIPAA compliance across multi-region deployments.