## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The Cloud Logging & BigQuery component ensures strict regional data residency, immutable audit trails for medical AI compliance, and secure analytics.

## Key Elements
- Log Ingestion & Routing Engine (Google Cloud Logging Sinks)
- Audit & Compliance Data Store (BigQuery Partitioned Datasets)
- Analytics & BI Exporter (BigQuery Authorized Views)
- Clinical Insights Dashboard (Looker Studio Enterprise)
- Security & Infrastructure (Cloud KMS, Cloud Pub/Sub, Cloud Monitoring)

## Relationships
- GKE & Cloud Run Services -> Log Ingestion & Routing Engine: Sends structured logs and telemetry [gRPC/HTTPS, TLS 1.3]
- Log Ingestion & Routing Engine -> Audit & Compliance Data Store: Stores region-segregated, pseudonymized logs [BigQuery SQL, Google Cloud Pub/Sub]
- Audit & Compliance Data Store -> Analytics & BI Exporter: Exposes anonymized metrics [BigQuery Authorized Views, Column-Level Masking]
- Analytics & BI Exporter -> Clinical Insights Dashboard: Feeds aggregated KPIs and clinical metrics [HTTPS, OAuth2/OIDC]

## Technology Stack
- Google Cloud Logging: Centralized log collection with regional routing to enforce data residency constraints.
- BigQuery: Regional data storage and analytics with table partitioning and WORM retention policies for compliance.
- Google Cloud KMS: Customer-Managed Encryption Keys (CMEK) ensuring regional key isolation (`europe-west3` and `us-central1`).
- Looker Studio Enterprise: Secure BI dashboard connected via authorized views for clinical quality monitoring.

## Rationale
This architecture guarantees strict GDPR and HIPAA compliance by enforcing complete regional data isolation and cryptographic separation. Additionally, it fulfills EU MDR traceability requirements for the AI symptom checker while enabling continuous clinical quality improvement via secure analytics.