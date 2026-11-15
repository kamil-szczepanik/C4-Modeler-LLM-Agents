## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability in rural areas.

## Key Elements
* Patients (EU & US) and Licensed Clinicians
* AI Symptom Checker Container
* Regional GKE Clusters (`europe-west3`, `us-central1`)
* Regional Redis Instances
* Cloud KMS and Cloud Logging
* Istio Service Mesh

## Relationships
* Patients to AI Symptom Checker: Invokes triage functions via HTTPS/TLS and gRPC with JWT authentication
* AI Symptom Checker Container to Regional Redis: Persists ephemeral session state via encrypted connections
* AI Symptom Checker Container to Cloud Logging: Writes audit logs and inputs via gRPC
* Istio to AI Symptom Checker Container: Enforces mTLS and rate limiting on ingress gRPC endpoints

## Technology Stack
* Google Cloud Platform: Target cloud providing regional infrastructure in `europe-west3` and `us-central1`
* Kubernetes & Istio: Orchestration and service mesh for mTLS, traffic management, and rate limiting
* gRPC: Protocol for internal container-to-container communication and client-server interactions
* Redis: In-memory datastore for low-latency stateless session persistence with strict TTLs
* Cloud KMS: Key management service for regional encryption-at-rest of audit logs and state

## Rationale
This architecture uses regional GKE clusters and Redis instances to strictly enforce EU and US data residency mandates. Istio, gRPC, and sidecar logging guarantee secure, resilient, and traceable operations for regulatory compliance under GDPR, HIPAA, and EU MDR.