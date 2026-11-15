## Overview
[The AI Symptom Checker Container processes patient symptom inputs to deliver care-urgency recommendations while strictly enforcing regional data residency and EU MDR traceability.]

## Key Elements
- API Router / Triage Controller (FastAPI)
- Deterministic Validation Layer
- Inference Engine (PyTorch / ONNX Runtime)
- Traceability & Audit Interceptor
- Localized AI Model Registries
- Cloud Storage (WORM enabled)

## Relationships
- API Router -> Deterministic Validation Layer [In-process Python call]
- Deterministic Validation Layer -> Inference Engine [In-process Python call]
- Inference Engine -> Localized AI Model Registries [HTTPS / gRPC]
- Inference Engine -> Traceability & Audit Interceptor [In-process hook]
- Traceability & Audit Interceptor -> Cloud Storage (WORM enabled) [Cloud Storage APIs]

## Technology Stack
- Python with FastAPI: Provides lightweight, high-performance API endpoints for rapid request handling.
- PyTorch / ONNX Runtime: Executes localized AI models efficiently for fast inference.
- Cryptographic HSM-Backed Keys: Ensures secure, tamper-proof signing of audit logs for regulatory compliance.

## Rationale
[This architecture ensures strict regional data isolation and cryptographic traceability required for EU MDR and HIPAA compliance. It also guarantees high availability and low-latency triage through modular components and clinical safety guardrails.]