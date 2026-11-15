## Overview
[Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict regional data residency, GDPR and HIPAA compliance, and reliable care delivery.]

## Key Elements
- Patients (EU / US)
- Licensed Clinicians
- Regional Cloud Spanner (GCP Cloud Spanner instances in europe-west3 and us-central1)
- Transactional Data Store (Spanner SQL tables with row-level security)
- Audit Log Table (Append-only table for consent tracking)
- Spanner Data Access Layer (Client libraries)
- Change Streams Processor (Spanner Change Streams with Pub/Sub)

## Relationships
- Consultation Service -> Regional Cloud Spanner: Reads and writes transactional data via gRPC over TLS 1.3
- Consent Management Service -> Regional Cloud Spanner: Persists consent tokens and immutable audit logs via gRPC over TLS 1.3
- Prescription & Interoperability Service -> Regional Cloud Spanner: Stores and reads prescription records via gRPC over TLS 1.3
- Change Streams Processor -> Microservices / Pub/Sub: Streams asynchronous data changes via gRPC and HTTPS

## Technology Stack
- GCP Cloud Spanner: Provides regional transactional data storage with data residency enforcement
- Google Cloud Spanner Native Go/Java Client Libraries: Enables low-latency transactional read/writes via gRPC over TLS 1.3
- Google Cloud KMS: Provides Customer-Managed Encryption Keys (CMEK) with regional isolation
- Spanner Change Streams: Captures real-time, row-level data changes asynchronously for downstream integration

## Rationale
[This architecture enforces strict regional data residency and security controls (GDPR and HIPAA compliance) by isolating data within europe-west3 and us-central1 using CMEK and fine-grained access. It ensures high availability, transactional integrity, and verifiable auditability for healthcare operations.]