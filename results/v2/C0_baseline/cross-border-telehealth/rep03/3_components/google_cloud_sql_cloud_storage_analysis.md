## Overview
- **System**: Cross-Border Telehealth Platform
- **Purpose**: Provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients while strictly enforcing regional data residency and healthcare regulations.

## Key Elements
- PostgreSQL 15 Cloud SQL Instance with Row-Level Security
- Google Cloud Storage (Standard Tier) with Cloud KMS / Cloud HSM CMEK
- Google Cloud Audit Logs and Pub/Sub
- Data Export & Erasure Worker (Go, Cloud Tasks)
- PostgreSQL Soft-Delete & Tombstone Manager
- Google Cloud Organization Policies (`constraints/gcp.resourceLocations`)

## Relationships
- Core Telehealth & AI Containers -> PostgreSQL: Relational queries and consent enforcement [SQL / TLS 1.3]
- Core Telehealth -> Cloud Storage: Binary payload persistence [HTTPS / TLS 1.3]
- Core Telehealth Backends -> Data Export Worker: Initiates asynchronous export/erasure jobs [gRPC / TLS 1.3]
- Data Export Worker -> Cloud Storage: Generates localized, time-limited export packages [HTTPS / TLS 1.3]

## Technology Stack
- **PostgreSQL 15**: Provides RLS for multi-tenant data isolation and schema mapping per jurisdiction (`europe-west3` and `us-central1`).
- **Google Cloud Storage**: Stores binary artifacts and export packages with automatic lifecycle management and 24-hour purge rules.
- **Cloud KMS & Cloud HSM**: Secures regional data via CMEK and enables cryptographic erasure.
- **Go & Cloud Tasks**: Powers asynchronous data export and erasure workers without blocking production database IOPS.

## Rationale
- This architecture guarantees GDPR and HIPAA compliance by isolating EU and US health data within their respective regions using PostgreSQL RLS and Cloud Organization Policies. It ensures EU MDR accountability via immutable audit logging and supports patient rights through secure cryptographic erasure and export utilities.