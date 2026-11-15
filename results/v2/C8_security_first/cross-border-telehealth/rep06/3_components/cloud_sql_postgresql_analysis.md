## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability even over unstable connections.

## Key Elements
- Patients (EU/US) & Licensed Clinicians
- API Gateway & BFF (Go, Envoy Proxy)
- Video Consultation Container (WebRTC SFU, MediaSoup)
- E-Prescription Integration Container (Node.js, Express)
- AI Symptom Checker Container (Python, FastAPI)
- Cloud SQL (PostgreSQL 15+) with PgBouncer
- Google Cloud Storage (WORM enabled)

## Relationships
- `API Gateway & BFF` -> `Cloud SQL (PostgreSQL)`: Relational queries for user profiles and consent management [PostgreSQL Protocol over TLS 1.3]
- `E-Prescription Integration Container` -> `Cloud SQL (PostgreSQL)`: Persists structured e-prescription data [PostgreSQL Protocol over TLS 1.3]
- `AI Symptom Checker Container` -> `Cloud SQL (PostgreSQL)`: Persists symptom logs and model version metadata [PostgreSQL Protocol over TLS 1.3]

## Technology Stack
- **Google Cloud Platform (GCP):** Deployed in `europe-west3` and `us-central1` to enforce strict data residency.
- **Cloud SQL (PostgreSQL 15+):** Relational storage with PgBouncer connection pooling and multi-zone HA failover.
- **Cloud KMS:** Customer-Managed Encryption Keys (CMEK) with 90-day rotation for regional compliance.
- **Google Cloud Storage:** WORM-enabled buckets for immutable audit logs and AI model version traceability.
- **Terraform & ArgoCD:** GitOps-driven deployment and automated zero-downtime schema migrations.

## Rationale
Physical regional database segregation in GCP satisfies GDPR and HIPAA mandates while avoiding complex logical partitioning. Combining IAM authentication, PostgreSQL Row-Level Security, and TLS 1.3 guarantees data privacy, strict isolation of AI and prescription data, and full auditability.