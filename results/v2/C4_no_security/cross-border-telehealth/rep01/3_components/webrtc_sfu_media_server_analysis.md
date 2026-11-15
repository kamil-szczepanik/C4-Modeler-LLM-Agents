## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict data residency, regulatory compliance, and high availability in low-bandwidth rural environments.

## Key Elements
- Patients (EU and US) and Licensed Clinicians
- Patient Portal (React, Flutter, IndexedDB)
- API Gateway / Region Router (Cloud Endpoints, Envoy)
- Core Telehealth Service & AI Gateway (GKE, Node.js, Go, Python)
- WebRTC SFU Media Server (LiveKit, Janus)
- Data Layer (Cloud SQL PostgreSQL, Firestore, Cloud Storage)
- External Systems: AI Symptom Checker Engine, EU National E-Prescription Gateways, US Pharmacy Networks

## Relationships
- Patient Portal -> API Gateway / Region Router: HTTPS / REST / GraphQL
- Core Telehealth Service -> WebRTC SFU Media Server: gRPC / WebRTC
- Patients / Clinicians -> WebRTC SFU Media Server: WebRTC (ICE, STUN, TURN over UDP/TCP)
- Core Telehealth Service -> AI Gateway: gRPC / REST
- Interoperability Adapter -> EU/US Pharmacy Networks: HL7 FHIR (US), National Standards (EU)

## Technology Stack
- **Compute & Orchestration:** Google Kubernetes Engine (GKE) and GCP Compute Engine for scalable microservices.
- **Media Streaming:** LiveKit / Janus (WebRTC, WHIP/WHEP) for real-time video with dynamic bandwidth scaling.
- **Data Persistence:** Cloud SQL PostgreSQL and Firestore for transactional and state data.
- **Networking & Security:** GCP Cloud Endpoints, Envoy, and Coturn for regional routing and NAT traversal.

## Rationale
This architecture segregates data regionally across `europe-west3` and `us-central1` to strictly satisfy GDPR and HIPAA mandates. LiveKit's dynamic adaptive bitrate controllers ensure continuous consultations for rural patients operating below 300 kbit/s.