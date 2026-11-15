## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and compliance via isolated GCP cloud infrastructure.

## Key Elements
* Regional Relational Database (Google Cloud SQL - PostgreSQL 15)
* Ephemeral Session Cache (Google Memorystore - Redis Cluster)
* Medical Document Store (Google Cloud Storage - GCS)
* Connection Pooling (pgBouncer sidecars)
* Security & Infrastructure (GCP KMS, GCP Secret Manager, ArgoCD, Istio Service Mesh, GCP VPC Service Controls)

## Relationships
* Application Services -> Google Cloud SQL: Structured clinical records, e-prescriptions, and consents via TCP over TLS 1.3 with IAM authentication and pgBouncer
* Application Services -> Google Memorystore: Real-time WebRTC session states and fast session tokens via Redis TCP protocol using AUTH and TLS
* AI Symptom Orchestrator & Consultation Service -> Google Cloud Storage: Unstructured artifacts, AI audit logs, and recordings via HTTPS (TLS 1.3) within VPC Service Controls

## Technology Stack
* Google Cloud SQL (PostgreSQL): Regional relational persistence with row-level security for HIPAA and GDPR compliance
* Google Memorystore (Redis): High-availability caching for WebRTC sessions and rapid token lookups
* Google Cloud Storage (GCS): Immutable WORM storage for AI symptom checker traceability and EU MDR compliance
* GCP KMS: Customer-Managed Encryption Keys with strict regional segregation (`europe-west3` and `us-central1`)

## Rationale
This architecture ensures strict regional data isolation between the EU and US to satisfy GDPR and HIPAA mandates. The redundant, high-availability data stores maintain uptime during unstable network connections while preserving immutable audit logs for medical device traceability.