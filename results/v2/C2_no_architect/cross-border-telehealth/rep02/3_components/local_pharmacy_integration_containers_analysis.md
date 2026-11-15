## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and compliance using GCP.

## Key Elements
- Patients and Licensed Clinicians
- Local Pharmacy Networks
- GCP GKE Clusters (`europe-west3`, `us-central1`)
- Local Pharmacy Integration Containers
- GCP Pub/Sub and Dead-Letter Queues
- GCP Secret Manager
- GCP Cloud Storage WORM Buckets
- Open Policy Agent (OPA) and Istio Sidecars

## Relationships
- API Gateway Container -> Local Pharmacy Integration Containers: Routes e-prescription requests [Istio Service Mesh (mTLS)]
- Local Pharmacy Integration Containers -> Local Pharmacy Networks: Transmits e-prescriptions [HL7 FHIR (US) and national EU standards, mutual TLS]
- Local Pharmacy Integration Containers -> GCP Pub/Sub: Publishes state-change events and retries failures via dead-letter queues
- Local Pharmacy Integration Containers -> GCP Cloud Storage WORM Buckets: Immutably logs transmission payloads and ACK/NACK responses [HTTPS]

## Technology Stack
- GCP GKE: Regional container orchestration for data residency in `europe-west3` and `us-central1`
- GCP Pub/Sub: Asynchronous event messaging and retry handling for unreliable external pharmacy networks
- GCP Secret Manager: Securely stores X.509 client certificates for external mutual TLS connections
- Open Policy Agent (OPA): Enforces strict tenant isolation and authorization for cross-border transactions
- GCP Cloud Storage WORM: Immutably logs audit trails for HIPAA and GDPR compliance

## Rationale
This architecture isolates fragmented national e-prescription standards into regional containers while ensuring strict cross-border data residency on GCP. Asynchronous event-driven messaging and immutable WORM logging guarantee high availability during network instability and absolute regulatory compliance.