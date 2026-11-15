## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency and compliance using GCP services while accommodating unstable rural internet connections.

## Key Elements
- Storage Gateway (Go / REST API)
- Upload Session Manager (Go / REST API)
- Encryption Service (Google Cloud KMS)
- Data Residency Auditor (Google Cloud Functions)
- Access Control Enforcer (Go / Open Policy Agent)
- Google Cloud Storage Buckets (Regional EU and US buckets)

## Relationships
- Storage Gateway -> Google Cloud Storage Buckets: Reads/writes encrypted blobs [HTTPS / GCP API]
- Storage Gateway -> Encryption Service: Encrypts/decrypts payloads [gRPC]
- Storage Gateway -> Upload Session Manager: Initiates resumable upload sessions [gRPC]
- Upload Session Manager -> Google Cloud Storage Buckets: Issues signed upload handles [HTTPS]
- Access Control Enforcer -> Encryption Service: Verifies key access rights [gRPC]

## Technology Stack
- Google Cloud Platform (europe-west3, us-central1): Chosen for regional isolation and compliance controls
- Google Cloud KMS: Provides customer-managed encryption keys (CMEK) bound to specific jurisdictions
- Cloud Run: Hosts microservices with multi-zone redundancy behind regional Load Balancers
- Cloud Pub/Sub: Triggers asynchronous malware scanning pipelines for uploaded files

## Rationale
This architecture guarantees GDPR and HIPAA compliance by isolating EU and US health data within their respective regions using CMEK and automated auditing. It also ensures high availability and resilience for rural users via resumable signed-URL uploads and strict security controls.