## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and high availability for rural users.

## Key Elements
* Patients (EU/US) and Licensed Clinicians
* Web Application & Mobile App (Flutter / React)
* API Gateway (Google Cloud API Gateway / Envoy)
* Core Telehealth Service (Go / Spring Boot)
* AI Symptom Checker Orchestrator (Python / FastAPI)
* E-Prescription Integration Service (Node.js / Java)
* Media Relay & Signaling Service (WebRTC / LiveKit)
* Cloud SQL PostgreSQL (PostgreSQL Relational Engine, Audit & Logging Schema)
* Memorystore Redis (Redis)
* Cloud Key Management Service (Cloud KMS)

## Relationships
* Core Telehealth Service -> PostgreSQL Relational Engine: Relational queries and transactions via `pgx` [TLS 1.3, SQL]
* AI Symptom Checker Orchestrator -> Audit & Logging Schema: Batched inserts via SQLAlchemy/Psycopg [TLS 1.3, SQL]
* Cloud SQL PostgreSQL -> Cloud KMS: Fetches regional envelope encryption keys [Internal VPC, gRPC]
* Patients -> Web/Mobile App: Accesses telehealth services [HTTPS, WSS]
* Media Relay -> Patients: Handles degraded video consultations [WebRTC, SRTP]

## Technology Stack
* GCP (`europe-west3`, `us-central1`): Deploys regional architecture for data residency (R-05).
* Cloud SQL PostgreSQL: Regional instances with declarative partitioning and append-only audit tables for traceability (R-07).
* Cloud KMS: Provides Customer-Managed Encryption Keys (CMEK) for region-specific encryption at rest.
* WebRTC / LiveKit: Enables video consultations with degraded mode support under 300 kbit/s (R-06).
* HL7 FHIR & National e-Prescription Standards: Ensures interoperability in US and EU (R-08).

## Rationale
This architecture enforces strict regional data isolation to satisfy GDPR and HIPAA mandates while utilizing Cloud KMS and append-only audit schemas for complete medical traceability. The technology stack guarantees reliable cross-border telehealth delivery even across unstable rural network connections.