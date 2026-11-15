## Overview
A cross-border telehealth platform delivering video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture enforces strict regional data residency and compliance using GCP.

## Key Elements
* Patients (EU & US)
* Licensed Clinicians
* Pharmacies (EU/US)
* Cross-Border Telehealth Platform (Software System)
* External Pharmacies (EU national gateways and US pharmacy networks)
* Regional Identity & Consent Providers (eIDAS/EU login and US IAM)
* AI Model Providers / Medical Devices (External AI inference APIs)

## Relationships
* Patients -> Cross-Border Telehealth Platform via HTTPS / WebSockets (adaptive codec)
* Cross-Border Telehealth Platform -> External Pharmacies via TLS / Mutual TLS
* Cross-Border Telehealth Platform -> AI Model Providers via HTTPS (REST/gRPC with payload masking)

## Technology Stack
* Cloud Platform: Google Cloud Platform (GCP) deployed in `europe-west3` and `us-central1` for data residency
* Infrastructure & Deployment: Terraform for Infrastructure-as-Code and ArgoCD for GitOps multi-region pipelines
* Security & Encryption: Cloud KMS with Customer-Managed Encryption Keys (CMEK), TLS 1.3, Mutual TLS (mTLS), and Sigstore/cosign for model verification
* Observability & Logging: Cloud Logging and BigQuery for immutable, regionally segregated audit trails

## Rationale
Zero-trust regional isolation guarantees compliance with GDPR and HIPAA by keeping EU health data in the EU and US data in the US. Explicit consent tunnels and payload masking satisfy EU MDR traceability and cross-border privacy mandates.