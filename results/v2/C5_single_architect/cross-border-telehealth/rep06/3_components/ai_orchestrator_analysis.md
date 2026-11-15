## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability in rural areas.

## Key Elements
- **Patients & Clinicians**: End-users accessing the telehealth platform.
- **Global Load Balancer with Cloud Armor**: Google Cloud Global Load Balancer & Cloud Armor.
- **API Gateway / BFF**: Go, gRPC/REST.
- **AI Orchestrator**: Python, FastAPI container with internal components: Prompt Router, Model Gateway, and Traceability Logger.
- **Video Consultation Service**: Golang, WebRTC SFU (LiveKit).
- **E-Prescription Integrator**: Java, Spring Boot.
- **Data Storage**: Cloud SQL (PostgreSQL), Cloud Storage, Cloud Bigtable.
- **External Systems**: National Pharmacy Networks (EU), US Pharmacy Systems, AI Model Provider / LLM API, Third-Party Identity Providers & Payment Gateways.

## Relationships
- **API Gateway / BFF** -> **AI Orchestrator**: Sends requests for AI symptom analysis [gRPC over mTLS via Istio].
- **Prompt Router** -> **Model Gateway**: Passes sanitized, region-validated payloads [In-process async function calls].
- **Model Gateway** -> **AI Model Provider / LLM API**: Executes external inference requests [HTTPS/REST with TLS 1.3].
- **Model Gateway** -> **Traceability Logger**: Emits immutable audit events [In-process Python Queue].
- **Traceability Logger** -> **Data Storage (Cloud Bigtable)**: Persists audit logs to region-locked tables [Region-pinned gRPC over VPC Service Controls].

## Technology Stack
- **Google Cloud Platform (GCP)**: Target cloud (`europe-west3`, `us-central1`) for regional isolation.
- **Python (FastAPI)**: Chosen for the AI Orchestrator due to its AI/ML ecosystem and asynchronous request handling.
- **Cloud Bigtable**: Used for immutable, high-throughput traceability logging.
- **WebRTC SFU (LiveKit)**: Powers video consultations under degraded network conditions.
- **HL7 FHIR / National Standards**: Ensures interoperability for US and EU pharmacies.

## Rationale
This architecture enforces GDPR and HIPAA by pinning regional health data to `europe-west3` and `us-central1` using GCP controls and region-pinned gRPC. It guarantees EU MDR compliance via traceable AI logging and maintains resilience for rural users via WebRTC.