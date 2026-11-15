## Overview
Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance (GDPR, HIPAA, EU MDR), and auditability through regionally isolated infrastructure.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- Dedicated Audit & Logging Container (deployed in `europe-west3` and `us-central1`)
- Log Collector (Fluent Bit)
- Audit & Compliance Engine (OpenTelemetry Collector)
- Compliance Archival Manager (Go-based cron)
- Log Access Proxy
- Regional Cloud Storage (Immutable Buckets with Object Lock)

## Relationships
- Core Telehealth Backend / AI Symptom Checker -> Log Collector [gRPC]
- Log Collector -> Audit & Compliance Engine [In-memory / IPC]
- Audit & Compliance Engine -> Compliance Archival Manager [Internal gRPC]
- Compliance Archival Manager -> Regional Cloud Storage [HTTPS / Storage API with CMEK and Object Lock]
- External Compliance Auditors -> Log Access Proxy [HTTPS / mTLS]
- Log Access Proxy -> Regional Cloud Storage [HTTPS / IAM]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for managed infrastructure and regional isolation (`europe-west3`, `us-central1`).
- Fluent Bit: Lightweight log ingestion and PHI stripping at the edge.
- OpenTelemetry Collector: Normalization and structured schema tagging for AI traceability (R-07).
- Go: Language for the Compliance Archival Manager component.
- Google Cloud Storage with Object Lock & CMEK: WORM-compliant regional storage for immutable audit logs.

## Rationale
The architecture enforces strict geographic isolation by deploying independent logging pipelines per region to satisfy EU and US data residency mandates. Immutable WORM storage and OpenTelemetry tracing ensure rigorous compliance with HIPAA, GDPR, and EU MDR auditability requirements.