## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency and compliance via GDPR and HIPAA standards.

## Key Elements
*   Patients & Clinicians: Primary users conducting video consultations and managing health data.
*   Compliance Officers / Auditors: Secondary users querying system logs for regulatory audits.
*   API Gateway: Cloud Endpoints / Apigee managing incoming traffic.
*   Regional Application Services: Google Kubernetes Engine (GKE) clusters in *europe-west3* and *us-central1*.
*   Policy & Consent Engine: Open Policy Agent (OPA) with Consent Sync Worker and Consent Audit Transformer components.
*   Data & Audit Tier: BigQuery, WORM Cloud Storage, and regional Cloud SQL.

## Relationships
*   Patients / Clinicians -> API Gateway: HTTPS/REST and WebRTC for consultations and portal access.
*   Regional GKE Services -> Policy & Consent Engine: Local OPA policy evaluation via gRPC.
*   Consent Sync Worker -> GCP Pub/Sub: Asynchronous cross-region consent propagation.
*   Consent Audit Transformer -> BigQuery: Regional log querying for human-readable audit trails.

## Technology Stack
*   Cloud Provider: Google Cloud Platform (GCP) across *europe-west3* and *us-central1* for data residency isolation.
*   Authorization: Open Policy Agent (OPA) for distributed, localized policy evaluation.
*   Event Streaming & Messaging: GCP Pub/Sub with regional topics for asynchronous consent state synchronization.
*   Security & Encryption: Istio/Cloud Service Mesh (mTLS), Cloud KMS (CMEK), and WORM Cloud Storage for immutable audit logs.
*   Runtime: Google Kubernetes Engine (GKE) running regional microservices.

## Rationale
This architecture guarantees strict regional data isolation between the EU and US to satisfy GDPR and HIPAA mandates. Distributed OPA sidecars combined with a fail-closed network partition strategy ensure compliance without sacrificing local availability.