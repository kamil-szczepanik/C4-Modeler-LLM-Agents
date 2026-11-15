## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency while ensuring high availability for rural users and compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
* Patients (EU and US) and Licensed Clinicians
* GKE Clusters in `europe-west3` (EU) and `us-central1` (US)
* API Gateway & BFF (Go / Envoy)
* Video Consultation Container (WebRTC SFU / MediaSoup)
* E-Prescription Integration Container (Node.js / Express)
* AI Symptom Checker Container (Python / FastAPI)
* Cloud SQL (PostgreSQL) and Cloud Storage (WORM enabled)
* External Identity Providers (OAuth2/OIDC), National e-Prescription Gateways, and US Pharmacy Networks (HL7 FHIR)

## Relationships
* Patients and Clinicians connect via HTTPS/WebSocket over TLS 1.3 to the regional API Gateway (Envoy).
* API Gateway routes internal traffic using mTLS over gRPC/REST to core services, enforcing OAuth2/OIDC token validation and R-04 purpose-based consent.
* WebRTC media streams utilize DTLS-SRTP terminating at the MediaSoup SFU Container.
* E-Prescription Container connects to US Pharmacy Networks via HL7 FHIR and national gateways in the EU.
* AI Symptom Checker logs inputs, outputs, and signed model versions to regional Cloud Storage.

## Technology Stack
* **Cloud Infrastructure:** GCP (`europe-west3`, `us-central1`), GKE, VPC Service Controls, Cloud KMS for CMEK.
* **API & Gateway:** Go, Envoy Proxy, gRPC, REST, mTLS.
* **Video & Streaming:** WebRTC, MediaSoup SFU (supporting adaptive bitrate down to 150 kbit/s with audio-only fallback).
* **Application Services:** Node.js / Express (E-Prescriptions), Python / FastAPI (AI Symptom Checker).
* **Data & Storage:** Cloud SQL (PostgreSQL), Cloud Storage with WORM policies.
* **Operations & Security:** ArgoCD (GitOps), Argo Rollouts, Cosign (container signing), Prometheus, Grafana, Thanos.

## Rationale
This architecture uses isolated regional GKE deployments governed by VPC Service Controls and GitOps to strictly enforce regional data residency and compliance (GDPR/HIPAA/MDR). It incorporates adaptive WebRTC media routing, cryptographic AI model traceability, and purpose-based consent management to meet both rural accessibility needs and rigorous healthcare regulations.