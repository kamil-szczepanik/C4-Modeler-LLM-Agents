## Overview
The Regional Data Stores container manages partitioned patient health data across GCP regions to guarantee strict regulatory compliance for cross-border telehealth. It enforces data residency, consent management, and audit traceability for both EU and US operations.

## Key Elements
- EU Data Store Instance: PostgreSQL database on GCP Cloud SQL in `europe-west3`
- US Data Store Instance: PostgreSQL database on GCP Cloud SQL in `us-central1` with FHIR schema
- Audit & Traceability Logger: Append-only schema component within each instance
- Consent Enforcement Proxy: Access control middleware protecting both database instances

## Relationships
- Core Telehealth Service -> Consent Enforcement Proxy: Validates patient consent scopes via [gRPC]
- Consent Enforcement Proxy -> EU/US Data Store Instances: Executes scoped database queries via [SQL over TLS 1.3]
- Audit & Traceability Logger -> Cloud Logging (GCP): Streams compliance and consent logs asynchronously via [gRPC]

## Technology Stack
- GCP Cloud SQL (PostgreSQL): Chosen for managed regional scaling, reliability, and isolation.
- gRPC: Selected for low-latency, high-performance internal service communication.
- TLS 1.3: Implemented for encrypted, secure data transmission.

## Rationale
This architecture enforces strict regional data residency to satisfy GDPR and HIPAA mandates while ensuring transparent, traceable access. Isolating data streams with consent proxies and append-only logging guarantees regulatory compliance and audit accountability.