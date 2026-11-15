## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability over unstable connections.

## Key Elements
- Patients and Licensed Clinicians (Users)
- API Gateway (Google Cloud Platform, HTTPS/WSS)
- Media Gateway / Edge Proxy (WebRTC)
- AI Symptom Checker Container (gRPC)
- E-Prescription Service (Cloud SQL / Cloud Spanner)
- OpenTelemetry Collector sidecars (Asynchronous log shipping)
- GCP Cloud Storage (Regional WORM storage with CMEK)
- Regional Pharmacies and National Standards APIs (External Systems)

## Relationships
- Patients/Clinicians -> API Gateway via HTTPS/WSS for routing requests
- API Gateway -> Media Gateway / Edge Proxy via WebRTC for video consultations
- API Gateway -> AI Symptom Checker via gRPC for urgency recommendations
- OpenTelemetry Collector -> GCP Cloud Storage via HTTPS for asynchronous log shipping

## Technology Stack
- Google Cloud Platform (europe-west3, us-central1): Target cloud enforcing strict regional data residency.
- OpenTelemetry Collector: Handles asynchronous log shipping, local disk buffering, and schema validation.
- GCP Cloud Storage with Cloud KMS: Implements WORM retention policies, Object Retention Locks, and Customer-Managed Encryption Keys.
- WebRTC: Enables low-bandwidth video consultations under degraded network conditions.

## Rationale
This architecture uses GCP regions and regional CMEK encryption to satisfy rigorous GDPR and HIPAA data residency constraints. Asynchronous OpenTelemetry logging with local buffering ensures uncompromised availability and accountability even during rural network instability.