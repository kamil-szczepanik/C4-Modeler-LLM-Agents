## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It utilizes Regional WORM Storage to ensure strict compliance with GDPR, HIPAA, and EU MDR traceability mandates.

## Key Elements
- **Regional WORM Storage Components**: Retention Policy Manager (Go), Audit Query API (Go, gRPC), Encryption & Key Manager (GCP Cloud KMS), Audit Export Bundle Generator (Go)
- **Infrastructure**: GCP Cloud Storage (europe-west3, us-central1) with Bucket Lock in compliance mode
- **Users & Services**: Compliance Auditors / Officers, Consent & Policy Engine, Video Session Service, AI Orchestration Service, FHIR & Prescription Integration Service

## Relationships
- **Consent & Policy Engine -> Regional WORM Storage**: Stores compliance records securely [TLS 1.3, Cloud KMS]
- **Video Session Service -> Regional WORM Storage**: Stores session logs securely [TLS 1.3, Cloud KMS]
- **AI Orchestration Service -> Regional WORM Storage**: Stores audit logs securely [TLS 1.3, Cloud KMS]
- **FHIR & Prescription Integration Service -> Regional WORM Storage**: Stores prescription data securely [TLS 1.3, Cloud KMS]
- **Compliance Auditors -> Audit Query API**: Queries immutable logs [gRPC over TLS 1.3, mTLS with ABAC]
- **Compliance Auditors -> Audit Export Bundle Generator**: Requests regulatory packages [gRPC over TLS 1.3]
- **Retention Policy Manager -> GCP Cloud Storage**: Applies immutable lock and storage tiering [Cloud Storage API]

## Technology Stack
- **GCP Cloud Storage**: Provides WORM storage with Bucket Lock in compliance mode for immutable data archiving.
- **GCP Cloud KMS**: Manages regionally isolated customer-managed encryption keys for data residency.
- **Go**: Implements microservices for high-performance retention policies, queries, and bundle generation.
- **gRPC / TLS 1.3**: Secures internal and external API communications.

## Rationale
This architecture guarantees strict regional data residency by isolating EU and US storage buckets and keys. Compliance requirements are met via immutable WORM storage, automated tiering, and cryptographic audit export verification.