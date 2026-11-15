## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance (GDPR/HIPAA/MDR), and regional isolation.

## Key Elements
* Regional Cloud SQL Instances (PostgreSQL 15 with Row-Level Security)
* Regional Cloud Storage WORM Buckets (Object Versioning and Bucket Lock in COMPLIANCE mode)
* Cloud KMS & Cloud HSM (Customer-Managed Encryption Keys)
* GCP Secret Manager (Credential and secret rotation)
* Core Telehealth Backend, AI Symptom Checker Service, and Interoperability Adapters
* GCP IAM and VPC Private Service Connect

## Relationships
* Core Telehealth Backend, AI Symptom Checker, and Adapters -> Regional Cloud SQL: Read/write transactional data and logs [TCP/PostgreSQL, TLS 1.3, IAM Auth]
* AI Symptom Checker Service -> Cloud Storage WORM Buckets: Writes immutable decision traces and audit logs [HTTPS/REST, CMEK]
* Backend Services -> GCP Secret Manager: Fetches rotated database credentials and API secrets [Internal gRPC/HTTPS, IAM]

## Technology Stack
* PostgreSQL 15: Regional transactional persistence with Row-Level Security for multi-tenant data isolation
* GCP Cloud Storage: Immutable object storage with COMPLIANCE mode bucket locks for regulatory audit trails
* Cloud KMS / Cloud HSM: Regional hardware-backed encryption keys ensuring strict cross-border data segregation
* GCP IAM & Private Service Connect: Secure zero-trust network paths and token-based database authentication without public IPs

## Rationale
This architecture uses isolated regional GCP resources (`europe-west3` and `us-central1`) to guarantee that EU and US health data never cross borders without explicit consent. Cryptographic immutability and strict IAM controls satisfy rigorous healthcare standards including GDPR, HIPAA, and EU MDR traceability.