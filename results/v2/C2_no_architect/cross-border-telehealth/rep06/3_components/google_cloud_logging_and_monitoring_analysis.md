## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, HIPAA/GDPR compliance, and traceable medical AI outputs.

## Key Elements
- Patients and Licensed Clinicians (End Users)
- Compliance Auditors and Platform Administrators (Internal Users)
- Regional GKE Clusters (`europe-west3`, `us-central1`)
- AI Symptom Checker Container
- WebRTC SFU Media Servers
- Google Cloud Logging and Monitoring
- External Pharmacies and National Health Authorities

## Relationships
- AI Symptom Checker Container -> Google Cloud Logging and Monitoring: Sends immutable structured logs and OpenTelemetry traces [mTLS, OpenTelemetry]
- Patients -> Regional GKE Clusters: Accesses video consultations and AI symptom checker [HTTPS, WebRTC]
- Regional GKE Clusters -> Google Cloud Logging and Monitoring: Exports sanitized operational metrics and region-bound audit trails [Cloud DLP, Pub/Sub, mTLS]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for regional isolation (`europe-west3`, `us-central1`)
- Google Kubernetes Engine (GKE): Container orchestration for regional workloads
- Istio Service Mesh: Manages microservice communication and enforces strict mTLS for OpenTelemetry exporters
- Google Cloud Logging and Monitoring: Centralized telemetry enforcing region-bound log sinks, CMEK encryption, and WORM immutability
- Cloud DLP API: Asynchronously scans and sanitizes log streams to prevent PHI/PII leakage

## Rationale
This architecture guarantees strict compliance with EU and US healthcare regulations by isolating data regionally while enabling unified, non-PII operational monitoring. It ensures traceability for AI medical devices and maintains high availability for unstable rural connections.