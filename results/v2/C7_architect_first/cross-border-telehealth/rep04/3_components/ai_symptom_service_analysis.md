## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, EU MDR traceability, and HIPAA/GDPR compliance across GCP regions.

## Key Elements
- AI Symptom Service container (Python / FastAPI)
- API Controller component
- Symptom Inference Engine component
- Traceability & Audit Logger component
- Data Residency Filter component
- Resilience & Fallback Handler component
- Google Cloud Pub/Sub with DLQs
- Google Cloud BigQuery
- Google Cloud Run

## Relationships
- API Gateway -> API Controller: Routes requests via gRPC over VPC
- API Controller -> Symptom Inference Engine: Evaluates inputs in-process
- Symptom Inference Engine -> Traceability & Audit Logger: Delegates audit payloads in-process
- Traceability & Audit Logger -> Google Cloud Pub/Sub: Publishes audit events via gRPC
- Google Cloud Pub/Sub -> Google Cloud BigQuery: Stores compliance logs via BigQuery API

## Technology Stack
- Python / FastAPI: Core framework for AI Symptom Service components for fast async handling
- Google Cloud Run: Regional container deployment ensuring multi-zone redundancy and infrastructure-as-code parity
- Google Cloud Pub/Sub: Asynchronous messaging with DLQs to prevent I/O blocking during inference
- Google Cloud BigQuery: Secure storage for pseudonymized EU MDR audit logs
- OpenTelemetry: Distributed tracing across the API Gateway and FastAPI service for latency SLAs

## Rationale
This architecture isolates data regionally in `europe-west3` and `us-central1` using GCP project segregation and VPC Service Controls to satisfy strict GDPR and HIPAA mandates. Asynchronous Pub/Sub logging and resilience handlers maintain availability and traceability for unstable rural connections.