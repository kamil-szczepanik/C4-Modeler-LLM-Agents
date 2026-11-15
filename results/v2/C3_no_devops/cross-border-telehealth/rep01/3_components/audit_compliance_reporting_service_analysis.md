## Overview
[The Audit & Compliance Reporting Service provides immutable audit logging, regional data residency, and real-time anomaly detection to guarantee GDPR, HIPAA, and EU MDR compliance for the cross-border telehealth platform.]

## Key Elements
- Regulatory & Compliance Auditors
- Operations Managers & Clinical Leads
- Audit Event Collector Component (Python / FastAPI)
- Compliance Data Store Component (Google BigQuery)
- Report Generation & Dashboard API Component (Python / FastAPI)
- Compliance Anomaly Detection Component (Python / Cloud Functions)

## Relationships
- Core services to Audit Event Collector via mTLS and gRPC (Protobuf)
- Auditors/Operations to Dashboard API via HTTPS/REST with OAuth2/OIDC
- Anomaly Detection to Operations via Google Cloud Pub/Sub and webhooks with HMAC signatures
- Report Generation to BigQuery via regional SQL queries with CMEK

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing europe-west3 and us-central1 for strict regional data residency.
- Python / FastAPI: Core runtime for ingestion, reporting, and anomaly detection APIs.
- Google BigQuery: Partitioned datasets with WORM policies for tamper-proof audit trails.
- Google Cloud KMS: Customer-Managed Encryption Keys (CMEK) for isolated regional data encryption.
- Google Cloud Pub/Sub: Secure messaging for real-time compliance anomaly alerting.

## Rationale
[This component-based architecture strictly separates telemetry ingestion, storage, reporting, and anomaly detection to enforce regional data isolation per GDPR and HIPAA. It ensures compliance traceability for AI medical devices while empowering stakeholders with proactive risk mitigation.]