## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability across unstable rural networks.

## Key Elements
- Patients and Clinicians (Users)
- External Pharmacy Systems, AI Model Provider, National Identity Providers, National Health Registries (External Systems)
- Web/Mobile Client SPA/PWA (Flutter/React)
- Google Cloud API Gateway (GCP API Gateway)
- Data Residency & Consent Router (Go)
- Core Services Backend (Go/Spring Boot)
- AI Symptom Checker Service (Python/FastAPI)
- Video Streaming Server (LiveKit WebRTC SFU on GKE)
- Interoperability Adapter (Node.js/TypeScript)
- Cloud SQL PostgreSQL (PostgreSQL 15), containing:
  - Regional Database Instances (`europe-west3` and `us-central1`)
  - Database Schema & Partitioning Layer (PostgreSQL Row-Level Security)
  - Audit Logging Extension (`pgAudit`)
  - Connection Pooling & Encryption Component (Cloud SQL Auth Proxy & GCP Cloud KMS)

## Relationships
- Core Services Backend -> Connection Pooling & Encryption Component: Routes queries via [TCP/PostgreSQL over IAM-authenticated Unix sockets / TLS 1.3]
- Connection Pooling & Encryption Component -> Regional Database Instances: Forwards authenticated queries to regional databases
- Core Services Backend -> Cloud SQL PostgreSQL: Persists and queries regional transactional health data via [TCP/SQL, TLS 1.3]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider across `europe-west3` and `us-central1` regions for data residency compliance
- PostgreSQL 15 & Cloud SQL: Relational data storage with Row-Level Security (RLS) for tenant isolation
- `pgAudit`: Database extension for comprehensive logging to satisfy AI traceability and accountability (R-07)
- Cloud SQL Auth Proxy & GCP Cloud KMS: Secure connection management and Customer-Managed Encryption Keys (CMEK) for data privacy

## Rationale
This architecture enforces strict regional data isolation to comply with GDPR and HIPAA mandates. The component-level database design guarantees auditability, encryption, and secure routing for cross-border healthcare data.