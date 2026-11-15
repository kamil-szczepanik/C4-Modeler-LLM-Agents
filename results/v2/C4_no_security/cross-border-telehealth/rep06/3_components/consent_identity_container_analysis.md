## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, privacy regulations (GDPR/HIPAA), and granular consent management.

## Key Elements
- Patients (EU/US) and Licensed Clinicians
- API Gateway (GCP Cloud Endpoints / API Gateway)
- Consent & Identity Container (Independent regional IAM instances)
- Token Service (Keycloak / GCP Identity Platform)
- Consent Engine (Java / Spring Boot)
- Consent Ledger Service (Go / gRPC)
- Federated Identity Broker (Keycloak SPI / OAuth2 Proxy)
- IAM Database (GCP Cloud SQL - PostgreSQL)
- GCP Cloud KMS with Cloud HSM

## Relationships
- API Gateway -> Consent Engine: Evaluates fine-grained consent policies [gRPC]
- Client Apps -> Federated Identity Broker: Authenticates users via external IdPs [REST/HTTPS]
- Client Apps -> Consent Ledger Service: Accesses user audit history [REST/HTTPS]
- Token Service & Consent Ledger -> GCP Cloud KMS: Secures signing and hashing keys [GCP Internal API]

## Technology Stack
- Java / Spring Boot: Chosen for the Consent Engine to provide robust enterprise policy evaluation.
- Go / gRPC: Powers the Consent Ledger Service for high-throughput, low-latency audit logging.
- GCP Cloud SQL (PostgreSQL): Provides isolated regional databases to satisfy data residency (R-05).
- GCP Cloud KMS (Cloud HSM): Secures regional cryptographic keys to ensure tamper-evident audit trails.

## Rationale
This architecture isolates regional data within `europe-west3` and `us-central1` to strictly satisfy GDPR and HIPAA mandates. Micro-components ensure high availability, traceability, and low-latency consent evaluation.