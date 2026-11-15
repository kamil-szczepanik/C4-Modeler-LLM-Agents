## Overview
[The Consent & Audit Logging Service manages patient data consent and immutable audit trails for a cross-border telehealth platform operating in the EU and US. Its core purpose is to enforce strict regional data residency and regulatory traceability for GDPR, HIPAA, and EU MDR compliance.]

## Key Elements
* Consent API Handler Component (Go, `grpc-go`, `net/http`)
* Consent Manager Component (Go, Open Policy Agent)
* Audit Logger Component (Go, Crypto-Shredding & Hashing Sub-component)
* Compliance Export Component (Go)
* Storage Abstraction Layer (Go, CMEK Key Management Interface)
* Cloud Pub/Sub
* Cloud SQL PostgreSQL (europe-west3, us-central1)
* Cloud Storage (WORM configuration)
* GCP KMS

## Relationships
* API Gateway -> Consent API Handler: gRPC over HTTP/2
* Core Telehealth Service & AI Symptom Checker Service -> Consent Manager: gRPC synchronous checks
* Cloud Pub/Sub -> Audit Logger: AMQP/PubSub protocol
* Consent API Handler -> Consent Manager & Audit Logger: In-process Go function calls / channels
* Audit Logger -> Cloud Storage (WORM): HTTPS/Storage API
* Consent Manager -> Regional Cloud SQL Databases: PostgreSQL wire protocol via TLS 1.3
* Storage Abstraction Layer -> GCP KMS: gRPC/Cloud KMS API via TLS 1.3
* Compliance Export Component -> Storage Abstraction Layer: Internal Go interface calls

## Technology Stack
* Go: Chosen for high-performance backend components and concurrency support.
* Open Policy Agent (OPA): Embedded for rapid, stateless GDPR and HIPAA access rule evaluations.
* Cloud SQL & Cloud Storage: Provides regional persistence with WORM capabilities.
* GCP KMS: Enforces regional Customer-Managed Encryption Keys (CMEK).

## Rationale
[This architecture uses regional service boundaries, cryptographic tamper-evidence, and policy-driven enforcement to satisfy strict EU/US data residency mandates. The component design ensures full compliance with GDPR, HIPAA, and EU MDR traceability requirements without sacrificing system availability.]