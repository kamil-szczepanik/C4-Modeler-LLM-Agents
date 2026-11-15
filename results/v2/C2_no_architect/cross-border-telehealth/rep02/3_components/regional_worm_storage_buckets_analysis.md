## Overview
[A secure, multi-region cross-border telehealth platform delivering video consultations, e-prescriptions, and AI symptom checking for EU and US patients. It guarantees strict regulatory compliance, regional data residency, and verifiable medical traceability.]

## Key Elements
* Patients and Licensed Clinicians (End Users)
* Regional Health Authorities and Auditors (Compliance Actors)
* API Gateway Container (GCP GKE, Istio, OPA)
* Consent & Identity Management Container (GCP GKE)
* Video Streaming Container (GCP GKE, WebRTC)
* AI Symptom Checker Container (GCP GKE, Cloud KMS)
* Local Pharmacy Integration Containers (GCP GKE, HL7 FHIR)
* Regional WORM Storage Buckets (GCP Cloud Storage WORM)
* Automated Dispute-Extraction Pipelines (GCP Cloud Run, Cloud KMS)

## Relationships
* AI Symptom Checker Container -> Regional WORM Storage Buckets: Persists immutable AI outputs and audit trails [HTTPS (TLS 1.3)]
* Consent & Identity Management Container -> Regional WORM Storage Buckets: Manages consent-backed audit events [HTTPS (TLS 1.3)]
* Automated Dispute-Extraction Pipelines -> Regional WORM Storage Buckets: Extracts scoped compliance reports via multi-party authorization [HTTPS (TLS 1.3)]
* API Gateway Container -> Local Pharmacy Integration Containers: Dispatches e-prescriptions using HL7 FHIR and national EU standards [HTTPS (TLS 1.3)]
* Patients -> Video Streaming Container: Conducts real-time video consultations in degraded bandwidth modes [WebRTC, SRTP]

## Technology Stack
* Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` for strict regional isolation.
* GCP GKE & Istio: Container orchestration and service mesh securing inter-service traffic.
* GCP Cloud Storage WORM: Immutable object storage with Object Lock in compliance mode for audit retention.
* GCP Cloud KMS: Customer-Managed Encryption Keys (CMEK) and Multi-Party Authorization (MPA) for data residency and decryption control.
* WebRTC: Real-time communication protocol supporting low-bandwidth degraded video modes.
* HL7 FHIR: Interoperability standard for US prescription integration.

## Rationale
[This architecture enforces regional data residency and privacy mandates (GDPR/HIPAA) through isolated GCP regions and WORM storage. Automated extraction pipelines and immutable logging ensure EU MDR traceability and zero-trust security without compromising data integrity.]