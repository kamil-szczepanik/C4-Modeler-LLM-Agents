## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker across the EU and US. The architecture enforces strict regional data residency, GDPR/HIPAA compliance, and robust audit traceability.

## Key Elements
* Patients and Licensed Clinicians (Users)
* API Gateway / Edge Proxy Container (GCP Cloud Load Balancing / Envoy)
* Integration & Translation Container (Node.js / GCP Cloud Run)
* State & Session Management Container (Redis / GCP Memorystore)
* Audit & Traceability Logging Container (GCP Pub/Sub / GCP Cloud Logging / GCP Cloud Storage)
* Identity & Access Management Container (OAuth2 / OpenID Connect / JWTs)
* Health & Resilience Monitoring Container (GCP Cloud Monitoring / Prometheus)
* Secrets & Certificate Management Container (GCP Secret Manager)
* Data Persistence Container (Cloud SQL / Spanner)

## Relationships
* API Gateway / Edge Proxy -> Integration & Translation Container: Routes requests [HTTPS / gRPC]
* Application Containers -> Audit & Traceability Logging Container: Publishes asynchronous logs with at-least-once delivery [GCP Pub/Sub]
* Audit & Traceability Logging Container -> GCP Cloud Storage: Archives tamper-evident logs to WORM storage [HTTPS]
* API Gateway / Edge Proxy -> State & Session Management Container: Manages active sessions [Redis Protocol]

## Technology Stack
* GCP Cloud Run & Cloud Load Balancing: Scalable container hosting and edge routing
* GCP Pub/Sub: Asynchronous messaging with at-least-once delivery and Dead-Letter Queues (DLQ)
* GCP Cloud Logging & Cloud Storage: Region-isolated logging buckets and WORM storage with Bucket Lock
* Node.js: Lightweight runtime for integration and translation microservices
* Redis (GCP Memorystore): Low-latency state and session management

## Rationale
The architecture ensures strict data residency by isolating EU and US workloads within specific GCP regions (`europe-west3` and `us-central1`). Resilient design patterns like Write-Ahead Logging (WAL) and local batching accommodate unstable rural internet connections while maintaining cryptographic traceability for medical AI compliance.