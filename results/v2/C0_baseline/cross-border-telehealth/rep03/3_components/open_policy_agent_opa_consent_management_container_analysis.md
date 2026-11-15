## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It ensures strict regional data residency and compliance using GCP.

## Key Elements
- Patients and Licensed Clinicians
- React / Flutter Web and Mobile Apps
- Google Cloud API Gateway / Region Router
- Go / Spring Boot Core Telehealth Backends
- Open Policy Agent (OPA) Consent Management Container
- LiveKit / WebRTC SFU Video Media Servers
- Python / FastAPI + TensorFlow AI Symptom Checker Container
- Google Cloud SQL, Cloud Storage, and Cloud KMS

## Relationships
- React / Flutter Apps -> Google Cloud API Gateway: HTTPS / WSS
- Google Cloud API Gateway -> Go / Spring Boot Core Backends: gRPC over Istio mTLS mesh
- Go / Spring Boot Core Backends -> Open Policy Agent (OPA) Sidecar: Local loopback gRPC (`localhost:9191`)
- Open Policy Agent (OPA) -> Google Cloud SQL: Read-only SQL queries via Istio mTLS
- OPA Bundle Manager -> Google Cloud Storage: HTTPS via Istio mTLS

## Technology Stack
- Google Cloud Platform (GCP): Multi-region deployment in `europe-west3` and `us-central1` for data residency.
- Open Policy Agent (OPA): Real-time authorization and consent evaluation.
- Go and Spring Boot: High-performance core telehealth microservices.
- LiveKit / WebRTC SFU: Low-latency real-time video streaming.
- TensorFlow & FastAPI: AI symptom checker infrastructure.
- Google Cloud KMS: Customer-managed encryption keys (CMEK) for data at rest.

## Rationale
Co-locating OPA as a local sidecar ensures sub-millisecond evaluation latency to protect real-time video workflows. Regional isolation guarantees compliance with GDPR and HIPAA mandates.