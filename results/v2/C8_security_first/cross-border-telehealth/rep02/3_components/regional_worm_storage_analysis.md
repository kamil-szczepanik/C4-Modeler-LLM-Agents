## Overview
A secure, cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It enforces strict regional data residency, immutability, and compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
* Patients and Licensed Clinicians (Users)
* Auditors & Compliance Officers (Secondary Personas)
* Local Pharmacies, Identity Providers (IdP), AI Triage Engine (External Systems)
* Istio Service Mesh & API Gateway (Istio)
* Backend-for-Frontend (BFF) (Node.js, GraphQL)
* Mediasoup SFU (Mediasoup WebRTC)
* AI Triage Service, Consent Manager, E-Prescription Adapter (Containerized Services)
* Regional WORM Storage (GCP Storage): Comprising Access Control & Policy Enforcer, Uniform Access Enforcer, Encryption & Key Manager Interface, Immutability & Retention Engine, and Lifecycle & Disposal Engine.

## Relationships
* BFF, AI Triage Service, Consent Manager -> Access Control & Policy Enforcer [mTLS/HTTPS]: Requests read/write operations
* Access Control & Policy Enforcer -> Uniform Access Enforcer [GCP API]: Rejects legacy ACLs entirely
* Access Control & Policy Enforcer -> Encryption & Key Manager Interface [Internal GCP API]: Applies regional CMEK for data at rest
* Access Control & Policy Enforcer -> Immutability & Retention Engine [Internal GCP API]: Applies WORM lock on write
* Immutability & Retention Engine -> Lifecycle & Disposal Engine [Internal API]: Triggers object purging post-retention expiration

## Technology Stack
* Google Cloud Platform (GCP): Target cloud provider for `europe-west3` and `us-central1` regions ensuring data residency.
* GCP Cloud Storage: Used for Regional WORM Storage with Object Retention Policies in "Compliance Mode" for tamper-proof audit trails.
* Google Cloud KMS: Provides Customer-Managed Encryption Keys (CMEK) with regional key rings.
* Terraform: Infrastructure-as-Code for automated regional provisioning and WORM activation.
* Istio: Secures data in transit using TLS 1.3 and mTLS.

## Rationale
The architecture uses strict regional isolation and GCP WORM storage to guarantee GDPR and HIPAA compliance while meeting EU MDR traceability requirements. Automated lifecycle management and uniform access controls balance strict legal immutability with cost efficiency and operational security.