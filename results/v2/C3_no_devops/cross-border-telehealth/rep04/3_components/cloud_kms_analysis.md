## Overview
[The system is a Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. Its core purpose is delivering compliant telemedicine services while enforcing strict regional data residency and auditability.]

## Key Elements
* Key Management Interface (REST/gRPC API)
* Regional Key Rings & CryptoKeys (`europe-west3-keyring`, `us-central1-keyring`)
* IAM & Access Policy Enforcer
* Audit Logging Emitter
* Key Recovery & Rotation Manager

## Relationships
* Spring Boot Core Telehealth Service -> Key Management Interface: Encrypts/Decrypts PHI using CMEK [gRPC/HTTPS]
* Compliance / Regulatory Officers -> Key Recovery & Rotation Manager: Approves emergency key restoration or rotation requests [GCP IAM/MPA Console/API]
* Key Recovery & Rotation Manager -> Regional Key Rings & CryptoKeys: Rotates and restores cryptographic material [Internal GCP control plane]

## Technology Stack
* GCP Cloud KMS: Manages encryption keys with CMEK for data protection
* Cloud HSM: Provides hardware security modules for strict healthcare compliance
* AES-256: Used for cryptographic key strength
* Transport Layer Security (TLS 1.3) with mTLS: Secures data-in-transit between microservices and Cloud KMS
* GCP IAM: Enforces principle of least privilege and condition-based regional access policies

## Rationale
[This architecture satisfies GDPR and HIPAA constraints by utilizing isolated regional key rings backed by Cloud HSM to guarantee that patient health data remains in its respective jurisdiction (`europe-west3` and `us-central1`). Furthermore, it incorporates strict multi-party authorization and immutable audit logging to ensure regulatory compliance and accountability.]