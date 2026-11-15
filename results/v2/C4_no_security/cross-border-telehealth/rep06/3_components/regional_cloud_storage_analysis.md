## Overview
[Regional Cloud Storage provides region-locked, immutable, and secure audit logging for AI symptom-checker outputs to satisfy EU MDR, GDPR, and HIPAA compliance mandates.]

## Key Elements
- GCP Cloud Storage (Regional Storage Buckets in europe-west3 and us-central1)
- AI Symptom Service (Python / FastAPI)
- GCP Cloud KMS (Key Management Service)
- Cloud Monitoring & Logging

## Relationships
- AI Symptom Service -> GCP Cloud Storage: Writes versioned audit logs and custom metadata [HTTPS / Storage API]
- GCP Cloud Storage -> GCP Cloud KMS: Encrypts audit logs using Customer-Managed Encryption Keys [Internal GCP API]
- Cloud Monitoring -> GCP Cloud Storage: Monitors bucket metrics, errors, and IAM denials [Cloud Monitoring API]

## Technology Stack
- GCP Cloud Storage: Region-locked buckets with Object Versioning and Bucket Lock (Compliance Mode) for immutability and regulatory compliance.
- GCP Cloud KMS: Customer-Managed Encryption Keys (CMEK) with regional key rings for strict data protection.
- Terraform: Infrastructure as Code for automated deployments and drift detection.
- GCP Object Lifecycle Management: Automated tiering to Nearline/Coldline storage after 30 days for cost-efficiency.

## Rationale
[The architecture enforces strict regional data residency and immutability via GCP Cloud Storage and CMEK to comply with GDPR, HIPAA, and EU MDR. Automated lifecycle rules and structured metadata ensure long-term operational cost-efficiency and rapid audit readiness.]