## Overview
Cross-Border Telehealth Platform delivering video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict cross-border compliance while supporting unstable rural internet connections.

## Key Elements
- Patients & Clinicians (Users)
- Web & Mobile Frontend Applications (Flutter / React Unified Container)
- UI Router & State Management Component
- Video Consultation Module (WebRTC / Flutter WebRTC)
- AI Symptom Checker UI Component
- Patient Consent Dashboard Component
- API Gateway (Envoy / Google Cloud API Gateway)

## Relationships
- Patients & Clinicians -> Web & Mobile Frontend Applications: Interacts with the platform [HTTPS, WSS]
- Video Consultation Module -> API Gateway: Streams media and signaling [WSS / WebRTC DTLS/SRTP]
- AI Symptom Checker UI -> API Gateway: Submits symptoms and receives traceable model outputs [HTTPS / REST]
- Patient Consent Dashboard -> API Gateway: Submits granular consent preferences [HTTPS / REST]

## Technology Stack
- Flutter / React: Unified codebase for cross-platform web and mobile support without maintaining separate binaries.
- WebRTC / Flutter WebRTC: Handles real-time media streams and adaptive bitrate control for low-bandwidth rural connections.
- OAuth2/OIDC with OIDC Tenant Discovery: Secures authentication and runtime region-locking for session data residency.
- SSL/TLS Certificate Pinning & RASP: Protects mobile clients against MITM attacks and compromised devices.

## Rationale
This architecture uses a unified client codebase with runtime region discovery to maintain user accessibility while strictly enforcing regional data residency. Client-side adaptive video modules and security controls directly satisfy rural availability and medical compliance requirements.