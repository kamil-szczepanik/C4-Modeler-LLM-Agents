## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. The system enforces strict regional data residency, HIPAA/GDPR compliance, and high availability for rural connections.

## Key Elements
* **Users & Actors**: Urban Patients, Rural Patients, Licensed Clinicians, Pharmacists, and Compliance Officers.
* **API Gateway**: Cloud Endpoints / Apigee handling TLS termination, JWT validation, and request routing.
* **Regional Application Services**: Google Kubernetes Engine (GKE) clusters in `europe-west3` and `us-central1`.
* **Video Consultation Service**: Twilio / WebRTC Media Server with adaptive bitrate streaming.
* **AI Symptom Checker**: Isolated inference container via Vertex AI endpoints.
* **Policy & Consent Engine**: Open Policy Agent (OPA) deployed locally on regional GKE clusters.
* **Interoperability Adapter**: GKE microservice for external health systems and pharmacy integration.
* **Data & Audit Tier**: Region-isolated Cloud SQL / Cloud Spanner databases and WORM Cloud Storage buckets.

## Relationships
* **Patients/Clinicians to API Gateway**: HTTPS and WSS via TLS 1.3.
* **API Gateway to GKE Clusters**: gRPC over Istio mTLS service mesh with Workload Identity.
* **GKE Application Services to Regional Databases**: Region-isolated SQL connections with no cross-border replication.
* **Interoperability Adapter to External Pharmacies**: OAuth 2.0 mTLS and signed payloads (SMART on FHIR).
* **AI Symptom Checker to Audit Tier**: Asynchronous event streams to WORM Cloud Storage and BigQuery.

## Technology Stack
* **Cloud Provider**: GCP (`europe-west3` and `us-central1`) for guaranteed regional data isolation.
* **Orchestration**: Google Kubernetes Engine (GKE) for regional container execution.
* **Security & Policy**: Istio (mTLS), Open Policy Agent (OPA), and Cloud KMS (CMEK) for localized authorization and data protection.
* **Observability**: OpenTelemetry and Google Cloud Operations Suite for distributed tracing and SLO monitoring.
* **Interoperability**: HL7 FHIR and national e-prescription protocols.

## Rationale
Regional GKE deployment combined with complete database isolation satisfies strict GDPR and HIPAA data residency mandates. Furthermore, OPA enforcement and adaptive WebRTC streaming ensure localized compliance and reliable video consultations for rural users.