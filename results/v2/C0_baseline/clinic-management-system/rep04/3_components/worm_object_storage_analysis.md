## Overview
The WORM object storage container secures electronic medical records for the Clinic Management System, guaranteeing a mandatory 10-year data retention policy. It operates across a hybrid architecture spanning on-prem-k8s and AWS eu-central-1 to fulfill strict HIPAA and GDPR compliance mandates.

## Key Elements
* Object Gateway API (MinIO / AWS S3 API)
* Immutability Enforcement Engine
* Replication & Tiering Controller
* Cryptographic Envelope & Key Manager Integration Module

## Relationships
* Core Services -> Object Gateway API: Persists encrypted EMR objects and metadata [HTTPS, TLS 1.3, S3 REST Protocol, mTLS, STS tokens]
* Replication & Tiering Controller -> AWS S3 in eu-central-1: Asynchronously replicates and tier-transitions EMR blobs [AWS S3 API]
* Cryptographic Envelope & Key Manager Integration Module -> On-Prem HSM: Wraps and manages object encryption keys [PKCS#11 / Secure Key Management API]

## Technology Stack
* MinIO & AWS S3 Object Lock (Compliance Mode): Chosen to enforce unalterable 10-year retention and prevent premature deletion.
* AES-256-GCM & On-Prem HSM: Selected for envelope encryption to guarantee zero-knowledge storage across the hybrid boundary.
* Prometheus: Utilized for scraping storage metrics, tracking replication lag, and detecting anomaly write velocities.
* Terraform / Crossplane: Deployed for Infrastructure-as-Code to maintain strict parity in cross-region lifecycle policies.

## Rationale
This architecture fits requirements by combining cryptographic controls and immutable object locking to satisfy HIPAA and GDPR security mandates. Furthermore, asynchronous hybrid replication and automated cold tiering balance high availability, disaster recovery, and long-term cost governance.