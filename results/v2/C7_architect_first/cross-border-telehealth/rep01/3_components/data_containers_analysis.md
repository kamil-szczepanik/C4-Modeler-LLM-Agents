## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency and compliance using GCP services deployed in separate regions.

## Key Elements
- PostgreSQL Regional Instances (Cloud SQL for PostgreSQL 15 in `europe-west3` and `us-central1`)
- Medical Artifact Buckets (GCP Cloud Storage with Object Lock and CMEK)
- Regional Redis Caches (GCP Memorystore for Redis)
- Core Services GKE Clusters (Google Kubernetes Engine with Istio Service Mesh)
- GCP VPC Service Controls and Cloud KMS

## Relationships
- Core Services GKE Clusters -> PostgreSQL Regional Instances: Reads/writes transactional records, audit logs, and consent states [PostgreSQL wire protocol over TLS 1.3, regional endpoints via Cloud SQL Auth Proxy]
- Core Services GKE Clusters -> Medical Artifact Buckets: Persists and retrieves encrypted medical files and AI trace bundles [HTTPS via Cloud Storage REST API]
- Core Services GKE Clusters -> Regional Redis Caches: Reads/writes session state and fast-path authorization tokens [Redis RESP protocol over TLS 1.3]

## Technology Stack
- GCP Cloud SQL (PostgreSQL): Structured transactional data and AI audit trails with regional isolation
- GCP Cloud Storage: Unsecured/structured medical artifact storage with WORM compliance for EU MDR and HIPAA
- GCP Memorystore for Redis: Ephemeral session caching and rate-limiting to support low-bandwidth resilience
- GCP Cloud KMS & VPC Service Controls: Regional encryption key management and network isolation

## Rationale
This architecture guarantees GDPR and HIPAA compliance by strictly isolating EU and US health data within their respective GCP regions. Furthermore, it ensures high availability, AI traceability, and data minimization while meeting regional regulatory mandates.