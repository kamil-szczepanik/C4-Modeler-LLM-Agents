## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. It ensures strict data residency, regulatory compliance, and traceability.

## Key Elements
- GCP Global HTTPS Load Balancer with Geo-routing
- EU Telehealth System (GCP `europe-west3`)
- US Telehealth System (GCP `us-central1`)
- Regional Pharmacy Networks and Health Information Exchanges (HIEs)
- AI Model Provider / Inference Service
- WebRTC/SFU Media Relay (LiveKit / Mediasoup)
- Regional GCP Cloud Storage with Object Retention (WORM) containing:
  - Bucket Manager / Retention Policy Enforcer
  - Access Control & Encryption Router
  - Audit Log Verifier / Integrity Checker
  - Audit & Access Logger

## Relationships
- AI Symptom Checker Service -> Access Control & Encryption Router: Streams immutable audit logs [HTTPS / GCP IAM]
- Access Control & Encryption Router -> Cloud KMS (Regional): Executes envelope encryption [gRPC]
- Bucket Manager -> Audit Log Verifier: Triggers integrity validation events [Cloud Pub/Sub]
- Audit & Access Logger -> GCP Cloud Logging / BigQuery: Exports security telemetry [Cloud Logging API]

## Technology Stack
- GCP (`europe-west3`, `us-central1`): Ensures regional data residency for EU and US compliance.
- GCP Cloud Storage: Provides immutable object storage with Bucket Lock in compliance mode.
- Cloud KMS: Manages regional customer-managed encryption keys (CMEK) for data isolation.
- Cloud Pub/Sub: Asynchronously triggers object integrity verification events.
- Cloud Logging & BigQuery: Captures non-repudiation security telemetry and audit trails.

## Rationale
This regionally isolated architecture strictly enforces GDPR and HIPAA by ensuring health and audit data remains within its source jurisdiction. Furthermore, immutable WORM storage and comprehensive logging satisfy strict EU MDR traceability mandates for AI outputs.