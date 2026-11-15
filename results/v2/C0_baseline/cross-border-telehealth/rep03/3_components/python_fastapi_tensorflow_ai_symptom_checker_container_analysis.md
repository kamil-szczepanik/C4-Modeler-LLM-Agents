## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency, HIPAA/GDPR compliance, and EU MDR traceability standards on Google Cloud Platform.

## Key Elements
* Patients and Licensed Clinicians (Users)
* React / Flutter Web and Mobile Apps
* Google Cloud API Gateway / Region Router
* Go / Spring Boot Core Telehealth Backends
* LiveKit / WebRTC SFU Video Media Servers
* Python / FastAPI + TensorFlow AI Symptom Checker Container
* Open Policy Agent (OPA) Consent Management Container
* Google Cloud SQL, Cloud Storage, and Google Cloud Pub/Sub
* National E-Prescription Gateways and Surescripts

## Relationships
* React/Flutter Apps -> Google Cloud API Gateway: Routes client traffic [HTTPS / WebSockets]
* Google Cloud API Gateway -> Core Telehealth Backends: Forwards API requests [gRPC / HTTPS]
* Core Telehealth Backends -> AI Symptom Checker Container: Requests AI symptom analysis [gRPC over Istio mTLS mesh]
* AI Symptom Checker Container -> Google Cloud Pub/Sub: Emits asynchronous audit events [gRPC / HTTPS]
* AI Symptom Checker Container -> Google Cloud SQL & Cloud Storage: Stores encrypted state and model artifacts using CMEK [HTTPS]

## Technology Stack
* Google Cloud Platform (GCP): Target cloud provider for regional isolation in `europe-west3` and `us-central1`.
* GKE with KEDA: Orchestrates containers and handles event-driven autoscaling.
* Python / FastAPI & TensorFlow Serving: Powers low-latency, localized AI symptom triage.
* Google Cloud Pub/Sub: Decouples compliance logging from the inference hot path.
* Istio mTLS & OPA: Enforces zero-trust service-to-service encryption and consent management.

## Rationale
This architecture ensures strict geographic data residency by pinning regional workloads to dedicated GCP regions, preventing cross-border data leakage. Decoupling compliance logging via asynchronous event publishing guarantees sub-three-second AI inference latencies while satisfying EU MDR traceability mandates.