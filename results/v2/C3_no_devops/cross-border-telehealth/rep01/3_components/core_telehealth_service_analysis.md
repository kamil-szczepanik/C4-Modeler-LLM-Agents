## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system ensures strict regulatory compliance through regional data residency and dynamic consent orchestration.

## Key Elements
* Patients and Licensed Clinicians (Users)
* API Gateway (Cloud Endpoints / Envoy)
* Core Telehealth Service (Go backend container)
* Consent & Policy Engine (Embedded Open Policy Agent / OPA library)
* Session Manager (Go component)
* Appointment & Routing Coordinator (Go component)
* Notification & Dispatcher Component (Go worker pools)
* Video Media Server (LiveKit SFU)
* Regional Databases (Cloud Spanner / Cloud SQL across europe-west3 and us-central1)

## Relationships
* API Gateway -> Consent & Policy Engine: Validate incoming requests [gRPC / mTLS]
* Session Manager -> Video Media Server: Control media streams and bandwidth thresholds [gRPC]
* Appointment & Routing Coordinator -> Notification & Dispatcher: Trigger prescription alerts [Asynchronous Go channels / Cloud Pub/Sub]
* Notification & Dispatcher -> External Notification Providers: Deliver alerts [HTTPS / REST]
* Core Telehealth Service -> Regional Databases: Persist and retrieve data [Secure TCP / PostgreSQL via internal VPC connectors using SPIFFE/SPIRE Workload Identities]

## Technology Stack
* Go: Chosen for high concurrency and low footprint in the Core Telehealth Service container.
* Open Policy Agent (OPA): Embedded library for zero-latency, dynamic consent and policy evaluation.
* LiveKit SFU: WebRTC media server for handling real-time video consultations and degraded connection modes.
* Cloud Pub/Sub & BigQuery: Asynchronous messaging and immutable audit log streaming for GDPR/HIPAA compliance.
* GCP (europe-west3 and us-central1): Cloud provider utilizing regional KMS keys for cryptographic tenant isolation.

## Rationale
This architecture guarantees strict regional data residency and compliance with GDPR and HIPAA through isolated GCP regions and SPIFFE/SPIRE workload identities. The modular Go-based Core Telehealth Service efficiently handles unstable rural internet connections and real-time consent orchestration without compromising performance.