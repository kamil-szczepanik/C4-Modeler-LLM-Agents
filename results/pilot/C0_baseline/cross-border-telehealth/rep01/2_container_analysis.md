## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data isolation while ensuring regulatory compliance, high availability, and interoperability.

## Key Elements
- **Clients:** Flutter Web and Mobile Applications used by Patients and Licensed Clinicians.
- **Edge Layer:** GCP Cloud Armor, Envoy-based API Gateway, and GCP Traffic Director.
- **Application Containers:** Node.js API Gateway, Go Clinical Workspace Service, Go Consent & Localization Engine.
- **AI & Video Components:** Python/FastAPI AI Symptom Checker container, mediasoup WebRTC Selective Forwarding Unit (SFU).
- **Integration Containers:** US HL7 FHIR adapters and EU national e-prescription formatters.
- **Infrastructure:** Google Cloud Platform (GCP) across `europe-west3` (Frankfurt) and `us-central1` (Iowa), Istio service mesh, ArgoCD.

## Relationships
- **Client to Edge:** HTTPS/TLS 1.3 and WebRTC over UDP/TCP for real-time video streaming.
- **Edge to Services:** Mutual TLS (mTLS) via Istio service mesh and gRPC/REST for inter-container communication.
- **AI to Audit:** Internal gRPC communication with structured payload and model version logging to regional storage.
- **Integration to External:** REST APIs connecting to US HL7 FHIR engines and EU National E-Prescription Gateways.

## Technology Stack
- **Cloud Provider:** Google Cloud Platform (GCP) (`europe-west3`, `us-central1`) for regional data residency isolation.
- **Frontend:** Flutter Web/Mobile for cross-platform patient and clinician UI.
- **Backend Services:** Node.js and Go for lightweight, high-performance API routing and clinical domain logic.
- **AI & Video:** Python/FastAPI for symptom-checking workloads; mediasoup SFU for adaptive, low-bandwidth video streaming.
- **Networking & Security:** Istio service mesh, Envoy, GCP Cloud Armor, and Customer-Managed Encryption Keys (CMEK) for zero-trust compliance.

## Rationale
Mirrored regional container clusters on GCP enforce strict data residency mandates (GDPR/HIPAA) by keeping EU data in `europe-west3` and US data in `us-central1`. Integrating mediasoup SFU and Istio mTLS guarantees high availability over unstable connections while maintaining end-to-end security and MDR traceability.