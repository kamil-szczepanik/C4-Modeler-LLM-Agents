## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces regional data residency and compliance using GCP to segregate health data.

## Key Elements
- Patients (EU/US) & Licensed Clinicians
- External Systems: Local Pharmacies, Vertex AI
- Patient Portal Container (PWA) with regional Redis
- Clinical Workspace Container with LiveKit WebRTC SFU
- Consent & Compliance Container with Istio, OPA sidecars, and regional WORM BigQuery
- Platform Administrators & Compliance Officers

## Relationships
- Patient Portal Container -> Consent & Compliance Container: Validates consent and logs activities via mTLS in GKE and OAuth2
- Clinical Workspace Container -> Consent & Compliance Container: Enforces granular consent and audit logging via mTLS in GKE and OAuth2
- Platform Administrators -> Consent & Compliance Container: Manages audits and credentials via HTTPS and OAuth2 token validation
- Consent & Compliance Container -> Regional WORM BigQuery: Stores immutable audit logs with region-specific CMEK encryption

## Technology Stack
- Google Cloud Platform (GCP): Target cloud utilizing `europe-west3` and `us-central1` regions for data residency
- Istio Service Mesh & Open Policy Agent (OPA): Enforces mTLS and fine-grained access control
- BigQuery (WORM configuration): Ensures immutable, region-isolated audit logs for AI traceability and compliance
- Redis: Provides regional caching with hard TTLs for consent validation
- LiveKit WebRTC SFU: Powers video consultations with degraded mode support

## Rationale
Segregating infrastructure into regional GCP clusters guarantees strict adherence to EU GDPR and US HIPAA data residency boundaries. Integrating immutable WORM storage and policy-driven sidecars ensures regulatory traceability for AI recommendations without compromising availability.