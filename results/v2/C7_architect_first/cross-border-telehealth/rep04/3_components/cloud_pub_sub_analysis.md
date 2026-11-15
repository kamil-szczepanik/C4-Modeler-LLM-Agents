## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, GDPR/HIPAA compliance, and regional interoperability standards.

## Key Elements
* **Users:** Patients (EU/US), Licensed Clinicians, Compliance/Audit Authorities
* **External Systems:** EU National E-Prescription Gateways, US Pharmacy Systems, Identity Providers (OAuth2/OIDC)
* **Containers:** API Gateway (Cloud Run / Envoy), Core Telehealth Backend (Node.js / NestJS), AI Symptom Service (Python / FastAPI), Video Media Server (LiveKit / WebRTC), Interoperability Worker (Go), Cloud SQL (PostgreSQL), Google Cloud BigQuery, Google Cloud Pub/Sub
* **Components (Cloud Pub/Sub):** Topic Router, Schema Registry, Retry & Backoff Controller, DLQ Handler, Audit Logger

## Relationships
* Core Telehealth Backend -> Schema Registry: Submits raw event payloads for validation [gRPC]
* Schema Registry -> Topic Router: Forwards validated events [Internal Buffer]
* Topic Router -> Regional Topics (europe-west3, us-central1): Routes messages [Cloud Pub/Sub API]
* Core Telehealth Backend -> Cloud Pub/Sub: Publishes e-prescription tasks asynchronously [Cloud Pub/Sub API]
* Interoperability Worker -> Cloud Pub/Sub: Consumes e-prescription tasks [Cloud Pub/Sub API]
* DLQ Handler -> Interoperability Worker: Triggers redelivery or alerts [gRPC]

## Technology Stack
* **Cloud Provider:** Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for strict regional data residency.
* **Messaging:** Google Cloud Pub/Sub with Dead Letter Queues (DLQs) for asynchronous, reliable e-prescription delivery.
* **Storage & Analytics:** Cloud SQL (PostgreSQL) for transactional PHI; Google Cloud BigQuery for audit logging and traceability.
* **Security:** Cloud KMS (Customer-Managed Encryption Keys), TLS 1.3, and IAM Workload Identity.
* **Interoperability:** HL7 FHIR for the US; national e-prescription standards for the EU.

## Rationale
The architecture guarantees strict regional data isolation to comply with GDPR and HIPAA mandates. Asynchronous messaging via GCP Pub/Sub with robust retry policies ensures reliable e-prescription delivery despite unstable rural internet connections.