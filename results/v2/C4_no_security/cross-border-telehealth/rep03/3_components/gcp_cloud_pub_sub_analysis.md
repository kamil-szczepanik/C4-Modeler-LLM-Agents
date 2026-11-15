## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It guarantees regional data residency, strict regulatory compliance (GDPR/HIPAA), and high availability across unstable connections.

## Key Elements
- Patients (Mobile/Web App via Flutter)
- Licensed Clinicians (Clinician Portal via React / Node.js)
- GCP API Gateway (Cloud Endpoints / Envoy)
- Core Telehealth Service & Consent Service (Go / Spring Boot)
- AI Inference Wrapper (Python / FastAPI)
- Pharmacy Integration Gateway (Apache Camel / Spring Integration)
- GCP GKE Regional Clusters (europe-west3, us-central1)
- GCP Cloud Pub/Sub (Regional Topics, Dead Letter Topics, Schema Validator)
- Cloud SQL PostgreSQL Databases

## Relationships
- Patients & Clinicians access services via HTTPS/gRPC through GCP API Gateway.
- Core services publish e-prescriptions and audit logs to GCP Cloud Pub/Sub using gRPC/HTTPS with regional endpoint routing (`europe-west3-pubsub.googleapis.com`).
- Pharmacy Integration Gateway consumes e-prescription events via GCP Cloud Pub/Sub to deliver to national networks (EU) and US pharmacy systems.
- AI Inference Wrapper logs traceability data into regional GCP Cloud Pub/Sub audit topics.

## Technology Stack
- GCP Cloud Pub/Sub: Asynchronous messaging buffer with region-isolated topics for e-prescription reliability and audit logging.
- Avro / Protocol Buffers: Native schema validation at the Pub/Sub ingestion boundary to enforce data contracts.
- Terraform & GCP IAM: Infrastructure as Code and VPC Service Perimeters for security and regional data isolation.
- Cloud SQL PostgreSQL: Relational storage adhering to strict data residency rules per region.

## Rationale
This architecture uses GCP regional services and isolated Pub/Sub endpoints to strictly enforce EU and US data residency mandates. Asynchronous messaging via Pub/Sub ensures reliable prescription delivery for rural patients with unstable connections while maintaining complete audit traceability.