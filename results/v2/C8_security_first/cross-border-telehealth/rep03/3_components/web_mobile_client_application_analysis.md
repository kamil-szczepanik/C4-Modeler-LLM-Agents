## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures regional data residency, HIPAA/GDPR compliance, and resilient access for rural users.

## Key Elements
- Patients (EU & US) & Licensed Clinicians
- Web/Mobile Client Application (Flutter / React Native)
- Cloud Load Balancing & Envoy API Gateway (Envoy & GCP Cloud Load Balancing)
- Core Telehealth & Consent Container (Go)
- AI Symptom Checker Container (Python / FastAPI)
- Prescription Integration Container (Go)
- National E-Prescription Networks (EU) & US Pharmacy Systems
- WebRTC SFU Media Relay & Break-Glass Identity Provider (IdP)

## Relationships
- Patients & Clinicians -> Web/Mobile Client Application: Conducts consultations and manages consent [HTTPS / WebRTC]
- Web/Mobile Client Application -> Cloud Load Balancing & Envoy API Gateway: Sends encrypted API requests and streams media [TLS 1.3 / gRPC-Web / SRTP]
- Envoy API Gateway -> Core Telehealth, AI, and Prescription Containers: Routes internal traffic within regional data boundaries [gRPC]
- Core Telehealth Container -> National E-Prescription Networks / US Pharmacy Systems: Transmits e-prescriptions [HL7 FHIR / REST]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Enforces regional data residency constraints
- Flutter / React Native: Powers cross-platform client presentation and accessibility
- Go & Python (FastAPI): Implements high-performance microservices and AI workloads
- Envoy & GCP Cloud Load Balancing: Manages secure API ingress and routing
- SQLCipher & Platform Keychains: Secures offline PHI storage and volatile tokens
- libwebrtc: Handles adaptive media streaming for low-bandwidth connections (<300 kbit/s)

## Rationale
This architecture uses regional GCP deployments to strictly segregate EU and US health data while maintaining global compliance. Edge acceleration, gRPC-Web, and adaptive WebRTC media ensure high availability and low-bandwidth resilience for rural users.