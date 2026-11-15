## Overview
The AI Symptom Checker Service provides traceable, region-locked symptom analysis and clinical handoffs for patients in the EU and US. It ensures GDPR, HIPAA, and EU MDR compliance while supporting unstable network conditions.

## Key Elements
- Patients and Licensed Clinicians (Primary Users)
- AI Symptom Checker Service (FastAPI / Python Container)
- Symptom Analysis API Controller (FastAPI Router)
- Consent & Resilience Middleware
- Inference Orchestrator
- Audit & Traceability Logger
- Clinical Handoff Formatter
- External AI Inference Provider and Core Telehealth Service

## Relationships
- Web & Mobile Client Apps -> Symptom Analysis API Controller via gRPC with mTLS over GCP Service Mesh
- Consent & Resilience Middleware -> Data & Security Layer for consent token validation
- Inference Orchestrator -> External AI Inference Provider via regional routing (`europe-west3` / `us-central1`)
- Audit & Traceability Logger -> Cloud SQL (PostgreSQL) via SQLAlchemy using GCP Cloud KMS (CMEK)
- Clinical Handoff Formatter -> Core Telehealth Service via gRPC

## Technology Stack
- FastAPI / Python: Selected for efficient AI model integration and high-performance asynchronous request handling.
- gRPC / Protobuf: Used for low-latency, strongly typed inter-service communication.
- GCP Cloud KMS & CMEK: Ensures regional data encryption at rest for GDPR/HIPAA compliance.
- SQLAlchemy: Provides database ORM mapping for audit logs.
- GCP Service Mesh (Istio): Enforces strict mTLS across all service-to-service communication.

## Rationale
This component architecture enforces strict regional data residency and purpose-specific consent validation required by GDPR and HIPAA. Furthermore, it guarantees traceability for EU MDR compliance and incorporates resilience patterns for unstable rural connections.