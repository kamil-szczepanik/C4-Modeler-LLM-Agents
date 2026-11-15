## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance (GDPR/HIPAA), and adaptive media streaming for low-bandwidth rural connections.

## Key Elements
* Patients and Clinicians (Users)
* API Gateway / BFF (Envoy / Cloud Endpoints)
* Video Consultation Service container, comprising:
  * Signaling Component (Node.js / WebSockets)
  * SFU Media Router (MediaSoup / C++ / Node.js)
  * Session Management Controller (Node.js / Express)
  * Audit & Metadata Logger Component (Node.js)
* AI Symptom Checker Service (Python / FastAPI)
* Integration & Interoperability Service (REST, HL7 FHIR)
* Consent & Identity Service (Keycloak)
* Regional Relational Database (Google Cloud SQL PostgreSQL)
* Regional Data Warehouse / ETL (BigQuery)
* Google Cloud Storage (Regional Object Storage)

## Relationships
* API Gateway / BFF -> Video Consultation Service: Forwards video consultation traffic [gRPC / REST]
* Signaling Component <> SFU Media Router: Manages RTP/RTCP media routing [Internal UDP/TCP]
* Session Management Controller -> Audit & Metadata Logger Component: Emits session lifecycle events [Internal gRPC]
* Audit & Metadata Logger Component -> Regional Relational Database: Persists compliance audit logs [TLS / SQL]
* SFU Media Router -> Regional Google Cloud Storage: Streams raw media recordings [TLS / HTTPS]
* Video Consultation Service -> Regional Relational Database: Persists consultation metadata [TLS / SQL]

## Technology Stack
* Google Cloud Platform (europe-west3, us-central1): Ensures isolated regional infrastructure for data residency compliance.
* MediaSoup WebRTC SFU (C++ / Node.js): Delivers adaptive bitrate video routing for unstable connections below 300 kbit/s.
* Node.js / Express / WebSockets: Powers signaling and session management controllers.
* Google Cloud SQL PostgreSQL: Stores regional transactional data and compliance audit logs.
* Google Cloud Storage: Secures partitioned regional storage for media recordings.
* Prometheus / Fluentbit: Handles region-isolated telemetry and WebRTC performance monitoring.

## Rationale
This architecture enforces strict regional data isolation between the EU and US to satisfy GDPR and HIPAA mandates. Decomposing the video consultation container ensures low-latency adaptive streaming for rural users while maintaining robust audit trails and regulatory compliance.