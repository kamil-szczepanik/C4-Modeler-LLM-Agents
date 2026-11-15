## Overview
[A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, compliance, and resilience for rural connectivity.]

## Key Elements
* Patients, Licensed Clinicians, Platform Administrators, Compliance Auditors
* External Pharmacies, National Health Authorities, WORM Audit Logs
* Regional GKE Clusters (`europe-west3`, `us-central1`)
* API Gateway Container with Consent Management and ABAC
* WebRTC SFU Media Servers for video consultations
* AI Symptom Checker Container with signed execution manifests
* GCP Cloud Armor and Cloud CDN
* Google Cloud Logging and Monitoring with region-bound log sinks

## Relationships
* Patients and Clinicians interact via HTTPS (TLS 1.3) and WebRTC for video consultations.
* API Gateway routes traffic using Istio mTLS and enforces OAuth2/OIDC JWT authentication and consent policies.
* AI Symptom Checker logs inputs and model versions to regional Cloud Logging using OpenTelemetry.
* External Pharmacies connect via national e-prescription standards (EU) and HL7 FHIR (US).

## Technology Stack
* Google Cloud Platform (GCP): Target cloud provider for regional isolation and infrastructure.
* Google Kubernetes Engine (GKE): Container orchestration with Binary Authorization.
* Istio Service Mesh: Enforces mTLS and zero-trust networking.
* GCP Cloud Armor & Cloud CDN: Edge security, WAF inspection, and asset caching.
* Google Cloud Logging & Monitoring: Centralized regional telemetry and immutable audit logs.
* OpenTelemetry: Standardized tracing for AI symptom checker traceability.

## Rationale
[Regional GKE isolation in `europe-west3` and `us-central1` strictly enforces GDPR and HIPAA data residency requirements. Istio mTLS, API Gateway consent enforcement, and OpenTelemetry logging guarantee security, privacy, and EU MDR traceability.]