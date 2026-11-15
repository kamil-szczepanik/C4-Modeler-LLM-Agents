## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. The architecture enforces strict regional data residency and compliance using isolated GCP infrastructure in `europe-west3` and `us-central1`.

## Key Elements
*   Patients (EU/US) & Licensed Clinicians
*   Regional Storage & Messaging Container
*   GCP Cloud SQL (PostgreSQL)
*   GCP Cloud Pub/Sub with Dead-Letter Queues (DLQ)
*   GCP Cloud KMS (Customer-Managed Encryption Keys)
*   Cloud Monitoring & Cloud Functions

## Relationships
*   Core Telehealth Service -> GCP Cloud SQL: Reads and writes consultation data via PostgreSQL native wire protocol [TLS 1.3]
*   E-Prescription Integrator -> GCP Pub/Sub: Publishes and consumes prescription events via gRPC APIs [TLS 1.3]
*   GCP Cloud SQL -> GCP Cloud KMS: Encrypts regional data using region-specific keys
*   GCP Pub/Sub -> GCP Cloud Functions: Triggers alerting payloads on DLQ threshold breaches

## Technology Stack
*   GCP Cloud SQL (PostgreSQL): Provides isolated regional relational storage with row-level security and append-only audit tables.
*   GCP Cloud Pub/Sub: Handles asynchronous event streaming and offline queuing with 7-to-14-day retention for rural resilience.
*   GCP Cloud KMS: Enforces regional compliance via Customer-Managed Encryption Keys (`europe-west3` and `us-central1`).
*   Cloud Monitoring & Cloud Functions: Automates operational alerts and DLQ monitoring for system reliability.

## Rationale
This architecture guarantees strict GDPR and HIPAA data residency compliance by isolating all storage and messaging within dedicated EU and US cloud regions. Additionally, it ensures high availability and rural accessibility through robust Pub/Sub offline queuing and automated database replication.