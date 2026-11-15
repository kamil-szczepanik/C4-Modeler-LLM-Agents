## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients while ensuring strict regional data residency and regulatory compliance.]

## Key Elements
* Patients (EU & US) and Licensed Clinicians
* Compliance & Regulatory Officers
* External Pharmacies (EU/US)
* API Gateway (Istio Service Mesh / Envoy)
* Frontend Container (Web / Distroless Container)
* WebRTC SFU (Mediasoup / coturn)
* AI Symptom Checker Container (Python / TensorFlow / Distroless)
* WORM Cloud Storage (Google Cloud Storage (WORM)) with Cloud Pub/Sub buffer
* Audit Sidecar (Sidecar Container)
* Regional GKE Clusters in `europe-west3` and `us-central1`
* Google Cloud WAF and Google Cloud KMS

## Relationships
* AI Symptom Checker Container -> WORM Cloud Storage: Streams immutable audit logs [gRPC/HTTPS via Istio mTLS]
* Compliance & Regulatory Officers -> BigQuery: Queries masked audit data and compliance metrics [HTTPS]
* API Gateway -> Frontend Container: Routes client traffic [HTTPS]
* Frontend Container -> WebRTC SFU: Manages video consultations [WebRTCP/UDP]

## Technology Stack
* Google Cloud Platform (GCP): Target cloud provider for `europe-west3` and `us-central1` regions to enforce data residency.
* Google Cloud Storage (WORM): Implemented with Bucket Lock in compliance mode for hardware-enforced immutability.
* Istio Service Mesh / Envoy: Enforces strict mTLS and network perimeter security.
* Google Cloud KMS: Provides Customer-Managed Encryption Keys (CMEK) with regional key rings.
* BigQuery: Provides secure, regional analytics and querying with column-level masking for compliance reporting.

## Rationale
[This architecture enforces stringent GDPR and HIPAA compliance by isolating regional health data and locking immutable audit logs with hardware-enforced retention policies. Additionally, resilient local redundancy and cryptographic log integrity ensure high availability and absolute traceability for AI medical outputs.]