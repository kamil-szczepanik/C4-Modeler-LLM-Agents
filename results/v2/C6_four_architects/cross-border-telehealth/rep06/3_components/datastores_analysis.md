## Overview
The Cross-Border Telehealth Platform is a secure telemedicine system providing video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability under unstable network conditions.

## Key Elements
- Patients and Clinicians (Web & Mobile Apps)
- Regulatory and Compliance Auditors
- External Pharmacy Networks, National Identity Providers, Payment & Insurance Providers
- Google Cloud API Gateway with Open Policy Agent (OPA)
- Core Telehealth Service (Go)
- AI Symptom Checker Service (Python / FastAPI)
- Video Streaming Service (mediasoup SFU on GCP Compute Engine, TURN/STUN relay)
- Integration Service (Node.js)
- Datastores Container components: Regional Transactional DB (Cloud SQL PostgreSQL), Caching Layer (Memorystore Redis), Audit & Analytics Store (Google Cloud BigQuery), Document Store / FHIR Repository (Google Cloud Storage), Encryption Key Management Component (Google Cloud KMS), CDC & Event Ingestion Pipeline (Google Cloud Pub/Sub & Dataflow), Data Masking & Tokenization Component, Database Connection Pooling (PgBouncer)

## Relationships
- Web & Mobile Apps -> Google Cloud API Gateway: API requests and video streaming [HTTPS and WebRTC over UDP/TCP]
- Core Telehealth Service -> Regional Transactional DB & Caching Layer via Database Connection Pooling: Relational reads/writes and session management [PostgreSQL and Redis protocols over TLS]
- AI Symptom Checker Service -> Audit & Analytics Store: Immutable AI traceability logging [HTTPS / BigQuery insert APIs]
- Integration Service -> Document Store & Regional Transactional DB: FHIR resources and e-prescriptions [HTTPS and PostgreSQL protocol]
- Regional Transactional DB, Document Store, & Audit Store -> Encryption Key Management Component: Data-at-rest encryption [gRPC over TLS with IAM]
- Regional Transactional DB -> CDC & Event Ingestion Pipeline: Change data capture streams [Google Cloud Pub/Sub native protocol over TLS]
- Integration Service & CDC Pipeline -> Data Masking & Tokenization Component: PHI/PII sanitization [Internal gRPC]
- Audit Store -> Regulatory Auditors: Compliance reporting [BigQuery SQL via IAM-secured HTTPS]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing regions europe-west3 and us-central1 for regional isolation.
- Cloud SQL PostgreSQL with PgBouncer: Relational database and connection pooling for transactional data and resilience against network flapping.
- Memorystore Redis: In-memory cache for low-latency session management and temporary state.
- Google Cloud BigQuery & Cloud Storage: Analytics, immutable audit logging, and FHIR document storage.
- Google Cloud KMS: Customer-managed encryption keys for strict cryptographic data isolation.
- Google Cloud Pub/Sub & Dataflow: Asynchronous event ingestion pipeline for zero-loss telemetry logging.

## Rationale
This architecture enforces strict regional isolation between europe-west3 and us-central1 to guarantee GDPR and HIPAA compliance while keeping EU health data strictly within the EU. Furthermore, it incorporates robust connection pooling, encrypted key management, and decoupled audit logging to meet high availability, security, and EU MDR traceability mandates.