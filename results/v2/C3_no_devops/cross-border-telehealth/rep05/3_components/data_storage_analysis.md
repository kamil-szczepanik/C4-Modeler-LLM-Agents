## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system enforces strict regional data residency and medical compliance while supporting rural users with unstable internet connections.

## Key Elements
*   **Client Apps:** Flutter and Web application with SQLite (SQLCipher) for offline-first caching and sync.
*   **API Gateway:** Google Cloud API Gateway with Envoy managing routing and mTLS.
*   **Core Services:** Core Telehealth Service, Patient Consent Service (Node.js/Go), and AI Symptom Checker Container (Python/FastAPI).
*   **Data Storage:** Google Cloud SQL (PostgreSQL with FHIR extensions and Read Replicas) deployed in `europe-west3` (EU) and `us-central1` (US).
*   **Caching & Logging:** Google Memorystore for Redis (regional caching tier) and GCP Cloud Storage with Object Versioning (WORM audit logs).
*   **Infrastructure:** GCP Cloud SQL Auth Proxy, Cloud KMS (CMEK), and VPC Service Controls.

## Relationships
*   Client Apps -> API Gateway: Secure client requests [HTTPS / WSS, TLS 1.3]
*   Core Telehealth Service & Patient Consent Service -> Google Cloud SQL: Reads and writes clinical/consent data [Encrypted SQL connections via Cloud SQL Auth Proxy]
*   Core Telehealth Service & Patient Consent Service -> Google Memorystore for Redis: Caches session and consent states [RESP protocol, TLS]
*   AI Symptom Checker -> GCP Cloud Storage: Writes immutable audit logs of inputs and model versions [gRPC / HTTPS]

## Technology Stack
*   **Google Cloud SQL (PostgreSQL):** Regional isolated databases with FHIR extensions to ensure HIPAA/GDPR compliance and regional data residency.
*   **Google Memorystore for Redis:** In-memory caching tier for low-latency session and consent retrieval during consultations.
*   **Google Cloud KMS:** Customer-Managed Encryption Keys (CMEK) ensuring regional key isolation without cross-border transit.
*   **SQLite with SQLCipher:** Client-side local database providing disk encryption for offline-first rural access.
*   **GCP VPC Service Controls:** Logical and cryptographic perimeter enforcement preventing cross-region data exfiltration.

## Rationale
This architecture guarantees strict regional data compliance (GDPR/HIPAA) through isolated GCP regions, CMEK keys, and VPC boundaries. Additionally, it ensures high availability and low-latency clinical access for rural users via client-side caching, read replicas, and secure in-memory Redis layers.