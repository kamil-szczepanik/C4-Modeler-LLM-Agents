## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data isolation, regulatory compliance, and high availability.

## Key Elements
* Patients and Licensed Clinicians
* EU/US Pharmacies & National E-Prescription Gateways
* Cryptographic Vault Container (GCP Cloud KMS / HSM)
* API Gateway (HTTPS, WebSockets)
* Regional Databases (GCP Managed Database in `europe-west3` and `us-central1`)
* Offline Sync/Queue Container

## Relationships
* API Gateway communicates with Regional Databases via TLS over GCP Cloud Infrastructure.
* Cryptographic Vault interacts with GCP Cloud KMS/HSM using a Provider-Agnostic Key Management Interface (Wrapper Pattern).
* Calling microservices interact with the Cryptographic Vault via gRPC with Protocol Buffers.
* Application services request Data Encryption Keys (DEKs) using Envelope Encryption.

## Technology Stack
* GCP Cloud KMS / Hardware Security Module: Hardware-backed key isolation for GDPR and HIPAA compliance.
* gRPC with Protocol Buffers: Low-latency, type-safe API communication for vault operations.
* GCP Managed Databases (`europe-west3`, `us-central1`): Enforces regional data residency.
* Python / Background Worker Framework: Used for asynchronous task processing and inference services.

## Rationale
The architecture ensures strict data residency and regulatory compliance by physically isolating EU and US health data using region-bound master keys within GCP Cloud KMS. Envelope encryption, zero-knowledge principles, and cryptographically signed audit logs secure sensitive health information while maintaining system performance and accountability under GDPR, HIPAA, and EU MDR.