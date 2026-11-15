## Overview
[Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients while strictly enforcing regional data residency and compliance.]

## Key Elements
- Patients (EU/US) and Clinicians
- React Web App and React Native Mobile App
- GCP Cloud Endpoints / Envoy API Gateway
- Core Services Container (Node.js / NestJS)
- AI Symptom Checker Container (Python / FastAPI)
- Video Media Server (LiveKit / WebRTC SFU)
- Cloud SQL (PostgreSQL, PgBouncer)
- BigQuery Container (GCP BigQuery) with regional datasets (`eu_audit_logs`, `us_audit_logs`)
- Internal BigQuery Components: Log Ingestion Service, Compliance Analytics View Layer, Partition & Retention Manager

## Relationships
- Core Services Container & AI Symptom Checker Container -> BigQuery (Log Ingestion Service): Streams audit trails via gRPC / BigQuery Storage Write API
- BigQuery (Log Ingestion Service) -> BigQuery (Partition & Retention Manager): Writes streaming data via BigQuery Internal Storage Engine
- Compliance Users -> BigQuery (Compliance Analytics View Layer): Queries audit data via BigQuery SQL Views

## Technology Stack
- GCP BigQuery & BigQuery Storage Write API: High-throughput audit log ingestion
- GCP Cloud KMS: Customer-Managed Encryption Keys (CMEK) with region-specific key rings (`eu-keyring`, `us-keyring`)
- Terraform: Infrastructure as Code for regional dataset and IAM deployment
- GCP Pub/Sub: Dead-letter queues for transient outage resilience
- GCP VPC Service Controls: Prevents data exfiltration and secures per-region perimeters

## Rationale
[Regional dataset isolation in `europe-west3` and `us-central1` combined with CMEK encryption satisfies strict GDPR and HIPAA data residency mandates. Automated partitioning, fine-grained access control, and immutable streaming ensure compliance and traceability for medical AI outputs.]