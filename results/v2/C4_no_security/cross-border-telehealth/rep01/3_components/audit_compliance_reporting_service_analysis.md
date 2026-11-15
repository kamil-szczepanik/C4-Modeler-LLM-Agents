## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, HIPAA and GDPR compliance, and EU MDR traceability.

## Key Elements
- Compliance Officers and Support Users
- Compliance Dashboard UI (React)
- Log Ingestion Engine (Go)
- Jurisdictional Storage Router (Go)
- Report Generation & Query API (Node.js/GraphQL)
- Compliance & Export Orchestrator (Node.js)
- Cloud Storage WORM Buckets & Cloud SQL PostgreSQL
- Cloud Pub/Sub
- Prometheus & Grafana

## Relationships
- API Gateway -> Log Ingestion Engine via gRPC over internal VPC
- Log Ingestion Engine -> Jurisdictional Storage Router via in-process calls
- Jurisdictional Storage Router -> GCS WORM Buckets & Cloud SQL via HTTPS (CMEK-secured)
- Compliance & Export Orchestrator -> Cloud Pub/Sub via gRPC
- Report Generation & Query API -> Compliance Dashboard UI via HTTPS/GraphQL

## Technology Stack
- GCP (europe-west3, us-central1): Enforces geographic separation for data residency.
- Go & Node.js: Powers microservices for high throughput and rapid API development.
- GCS WORM Buckets & Cloud SQL: Ensures immutable audit retention for HIPAA/GDPR.
- Cloud Pub/Sub: Manages asynchronous report generation without timeouts.
- Prometheus & Grafana: Provides regional pipeline monitoring and alerting.

## Rationale
The architecture strictly segregates regional data to satisfy EU and US privacy laws while using WORM storage and asynchronous queues to guarantee tamper-proof audit trails and system availability.