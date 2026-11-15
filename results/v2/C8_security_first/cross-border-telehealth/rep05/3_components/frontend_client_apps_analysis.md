## Overview
Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, HIPAA/GDPR compliance, and high availability over unstable connections.

## Key Elements
* Patients (EU & US) & Licensed Clinicians
* Frontend Client Apps (Flutter)
* API Gateway / BFF (Envoy / gRPC-Web)
* Video Consultation Service (WebRTC / Mediasoup SFU)
* AI Symptom Checker Container (Python / FastAPI)
* E-Prescription Integration Service (Node.js / Express)
* Consent & Policy Engine (Opa / Go)
* Data Layer (PostgreSQL / Cloud SQL)

## Relationships
* Patients & Clinicians -> Frontend Client Apps: Interacts via HTTPS and WebRTC [HTTPS, WebRTC]
* Frontend Client Apps -> API Gateway / BFF: Communicates via gRPC-Web and HTTPS [gRPC-Web, HTTPS]
* API Gateway / BFF -> Consent & Policy Engine: Validates access via internal gRPC [gRPC]
* Video Consultation Service -> Mediasoup SFU: Manages video streams via WebRTC [WebRTC]
* Backend Services -> Data Layer: Persists data via SQL/TLS [TLS 1.3]

## Technology Stack
* Flutter: Cross-platform web and mobile client support with certificate pinning and root detection.
* Envoy & gRPC-Web: High-performance binary protocol for client-to-BFF communication.
* WebRTC & Mediasoup: Real-time video/audio streaming with bandwidth degradation fallback.
* Python / FastAPI: AI symptom checker container ensuring traceable diagnostic recommendations.
* PostgreSQL (Cloud SQL): Relational data storage partitioned across GCP regions (`europe-west3` and `us-central1`).
* Google Cloud CDN: Edge asset delivery with geo-routing for regional data residency enforcement.

## Rationale
The architecture enforces regional data segregation between `europe-west3` and `us-central1` to meet strict GDPR and HIPAA mandates. The Flutter client with WebRTC and gRPC-Web guarantees resilient performance for rural patients with unstable connections while preserving traceability.