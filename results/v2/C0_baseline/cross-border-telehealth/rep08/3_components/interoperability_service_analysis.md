## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and interoperates with regional pharmacy systems.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Client Applications (Flutter / Web)
- API Gateway (Envoy / Google Cloud Endpoints)
- Core Telehealth Service (Go)
- AI Inference Service (Python / FastAPI)
- Interoperability Service (Java / Spring Boot) with internal components: FHIR Translation Engine, EU Gateway Adapter Module, Consent & Policy Enforcement Interceptor, and Async Dispatch & DLQ Manager
- Containerized SFUs (mediasoup)
- Google Kubernetes Engine (GKE) in GCP (`europe-west3`, `us-central1`) with Istio service mesh
- GCP Pub/Sub and Cloud KMS (CMEK)
- External National E-Prescription Gateways (EU) & US Pharmacy Systems

## Relationships
- Client Applications -> API Gateway: Accesses platform features [HTTPS / gRPC]
- API Gateway -> Interoperability Service: Routes interoperability and prescription requests [gRPC over Istio mTLS mesh]
- Interoperability Service (Consent Interceptor) -> FHIR Translation Engine & EU Gateway Adapter: Dispatches validated payloads [Spring Application Events]
- Interoperability Service -> External Gateways: Transmits prescription data [HTTPS / Mutual TLS]
- Interoperability Service -> GCP Pub/Sub: Persists unrecoverable payloads to Dead-Letter Queues [gRPC]

## Technology Stack
- Java / Spring Boot: Chosen for the Interoperability Service to leverage its enterprise ecosystem for complex regional data formats.
- GCP GKE & Istio: Deployed across dual regions (`europe-west3`, `us-central1`) with egress gateways to strictly enforce data residency and regional isolation.
- GCP Pub/Sub & Resilience4j: Implements persistent dead-letter queues and circuit breakers to handle transient failures from external gateways.
- GCP Secret Manager & Cloud KMS (CMEK): Secures external API keys, mTLS certificates, and encrypts DLQ payloads at rest per region.

## Rationale
This architecture ensures strict regulatory compliance with GDPR and HIPAA by enforcing regional data residency and robust consent validation. Furthermore, it guarantees clinical continuity and accountability through resilient asynchronous queuing and distributed tracing.