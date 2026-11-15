## Overview
- Secure, cross-border telemedicine platform offering video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US.
- Engineered to ensure strict regulatory compliance (GDPR, HIPAA, EU MDR) and high availability over unstable rural internet connections.

## Key Elements
- Patients & Licensed Clinicians
- Web/Mobile Frontend App (`React / Flutter`)
- API Gateway / Core Backend (`Go / Node.js`)
- AI Symptom Checker Container (`Python / FastAPI`), comprising:
  - Triage API Controller (`Python / FastAPI`)
  - Inference Engine (`Python / PyTorch` or `ONNX Runtime`)
  - Clinical Fallback Engine (`Python / Rule-based Logic`)
  - Audit & Cryptographic Signer (`Python / GCP KMS / Cloud HSM Client`)
- External Systems: Global IdP, EU National E-Prescription Gateways, US Pharmacy Networks, Video Relay/Codec Service (WebRTC SFU)

## Relationships
- Web/Mobile Frontend App -> API Gateway / Core Backend: Manages sessions and requests triage [HTTPS / REST]
- API Gateway / Core Backend -> Triage API Controller: Requests AI symptom analysis [mTLS / Internal API]
- Triage API Controller -> Inference Engine: Executes clinical model [In-memory / gRPC]
- Triage API Controller -> Clinical Fallback Engine: Invokes fallback on model failure/timeout [In-memory]
- Triage API Controller -> Audit & Cryptographic Signer: Offloads event logs [Async Message Queue]
- Audit & Cryptographic Signer -> GCP Cloud HSM / KMS: Cryptographically signs audit payload [gRPC / Regional HSM Endpoint]

## Technology Stack
- Google Cloud Platform (`GCP`): Target cloud provider for global infrastructure.
- GKE Autopilot (`europe-west3`, `us-central1`): Regional container orchestration ensuring strict data residency isolation.
- GCP Cloud HSM / KMS: Cryptographically signs audit payloads and secures data at rest via CMEK.
- Python / FastAPI / PyTorch / ONNX Runtime: Powers high-performance, low-latency AI symptom checking and fallback logic.
- WebRTC SFU: Powers video consultations with degraded mode support for low-bandwidth connections.

## Rationale
- Regional GKE deployment with strict network policies ensures health data never crosses international boundaries, satisfying GDPR and HIPAA mandates.
- Asynchronous cryptographic signing and local fallback engines maintain sub-3-second latency and high availability for rural users while guaranteeing EU MDR traceability.