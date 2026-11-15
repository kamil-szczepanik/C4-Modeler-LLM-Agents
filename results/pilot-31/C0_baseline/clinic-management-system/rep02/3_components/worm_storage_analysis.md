## Overview
The Clinic Management System is a hybrid-cloud platform designed for clinical operations, ensuring HIPAA/GDPR compliance and high availability. It provides secure patient registration, scheduling, EMR management, and billing with a 10-year immutable audit trail.

## Key Elements
*   **Users:** Clinical Staff, Patients, Auditors, Legal Counsel.
*   **Gateways:** Clinical API Gateway (Go), Patient-Facing API Gateway (Node.js).
*   **Services:** EMR/Scheduling Service, Reporting & Compliance Service, Audit Logging Sidecar.
*   **Storage/Infrastructure:** WORM Storage (Object Lock), PostgreSQL/Patroni, Redis, NATS/Kafka.
*   **WORM Components:** Ingestion Gateway, Verification Engine, Retention Manager.

## Relationships
*   **Audit Logging Sidecar -> WORM Storage:** mTLS-encrypted stream using cryptographic manifests.
*   **Ingestion Gateway -> Verification Engine:** Internal asynchronous processing via local disk-backed queue.
*   **Retention Manager -> S3 Object Lock API:** Orchestrates lifecycle policies and Legal Hold states.
*   **External Systems:** HL7 FHIR Integration Engine (interoperability), Clearinghouse Gateway (billing).

## Technology Stack
*   **WORM Storage:** AWS S3 with Object Lock (Compliance Mode) and Glacier Deep Archive for tiered retention.
*   **Security:** AES-256 at rest with CMK via FIPS 140-2 Level 3 HSM; mTLS for service communication.
*   **Integrity:** Digital Signature Service for cryptographic manifest generation and background drift detection.
*   **Orchestration:** Kubernetes (on-prem) and AWS (eu-central-1) with M-of-N multi-party authorization for Legal Holds.

## Rationale
The architecture utilizes hardware-level immutability and cryptographic verification to satisfy strict non-repudiation and 10-year retention mandates. Decoupling the ingestion, verification, and retention logic ensures high performance while maintaining a robust, tamper-proof "Chain of Custody" for clinical records.