## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability across disparate regional networks.

## Key Elements
- **Web/Mobile Client SPA/PWA**: Patient and clinician interface built with Flutter/React supporting degraded network modes.
- **Google Cloud API Gateway**: Entry point containing internal components: API Router & Regional Dispatcher, Authentication & Authorization Filter, Rate Limiting & Resiliency Policy Enforcer, and Audit & Telemetry Logger.
- **Data Residency & Consent Router**: Go service managing regional data boundaries and explicit consent.
- **Video Streaming Server**: LiveKit WebRTC SFU deployed on Google Kubernetes Engine (GKE).
- **AI Symptom Checker Service**: Python/FastAPI service with versioned traceability logging.

## Relationships
- Web/Mobile Client SPA/PWA -> Google Cloud API Gateway: Sends API requests and video streams [HTTPS/WSS]
- API Router & Regional Dispatcher -> Authentication & Authorization Filter: Validates tokens [Internal gRPC]
- API Router & Regional Dispatcher -> Data Residency & Consent Router: Forwards regional payloads [gRPC]
- API Router & Regional Dispatcher -> Audit & Telemetry Logger: Streams request metadata [Cloud Pub/Sub / gRPC]

## Technology Stack
- **Google Cloud Platform (GCP)**: Cloud provider utilizing `europe-west3` and `us-central1` regions for strict data residency.
- **Google Cloud API Gateway**: Manages ingress traffic using Envoy-powered extensions.
- **LiveKit WebRTC SFU**: Powers video consultations on GKE for low-bandwidth environments.
- **PostgreSQL / Cloud SQL**: Regional data storage ensuring separation of EU and US health records.
- **HL7 FHIR & National Standards**: Interoperability protocols for US and EU e-prescriptions.

## Rationale
This architecture enforces GDPR and HIPAA compliance by isolating EU and US health data within designated GCP regions using intelligent API routing. It guarantees high availability and traceability for medical AI outputs even under unstable rural network conditions.