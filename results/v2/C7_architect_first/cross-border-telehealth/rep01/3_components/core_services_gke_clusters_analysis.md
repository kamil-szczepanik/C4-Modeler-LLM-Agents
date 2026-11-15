## Overview
- The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker across the EU and US.
- It ensures strict regional data isolation, regulatory compliance (GDPR/HIPAA), and robust performance for low-bandwidth rural users.

## Key Elements
- **Users**: Patients and Licensed Clinicians
- **External Systems**: EU National e-Prescription Gateways, US Pharmacy Networks, Third-Party AI Model Providers, Identity Providers
- **Containers**: GCP API Gateway, Web & Mobile App Containers, Core Services GKE Clusters, Data Containers, Media Relay Containers
- **GKE Core Services Components**: Consultation, Prescription, AI Symptom Checker, Consent & Policy, Localization & Fallbandwidth, Notification, BI Ingestion
- **Infrastructure & Security**: Istio Service Mesh, Open Policy Agent (OPA), ArgoCD, Falco, HashiCorp Vault / GCP Secret Manager, OpenTelemetry Collectors

## Relationships
- **Web/Mobile Apps -> GCP API Gateway**: Routes client requests via HTTPS/JSON
- **GCP API Gateway -> Core Services GKE Clusters**: Forwards requests to regional GKE microservices using gRPC over mTLS
- **Core Services GKE Clusters -> Media Relay Containers (Coturn/Mediasoup)**: Connects session traffic using WebRTC (DTLS-SRTP)
- **Core Services GKE Clusters -> Data Containers (Cloud SQL PostgreSQL, Cloud Storage)**: Reads/writes encrypted transactional data via PostgreSQL protocol and Cloud Storage APIs
- **Core Services GKE Clusters -> EU/US e-Prescription Gateways**: Integrates prescription workflows using REST and HL7 FHIR over secure mTLS
- **AI Symptom Checker -> Third-Party AI Model Providers**: Invokes external models via Istio Egress Gateways using HTTPS with strict L7 filtering

## Technology Stack
- **Compute & Orchestration**: Google Kubernetes Engine (GKE) deployed via ArgoCD across `europe-west3` and `us-central1` for strict multi-cluster data residency.
- **Service Mesh & Security**: Istio Service Mesh with mTLS and Open Policy Agent (OPA) sidecars for zero-trust authorization and regional isolation.
- **Microservices & Messaging**: Java (Spring Boot), Python (FastAPI), Go, gRPC for internal communication, and region-locked Apache Kafka/PubSub for asynchronous event streaming.
- **Observability & Runtime Security**: OpenTelemetry for distributed tracing, Falco for runtime container security, and HashiCorp Vault / GCP Secret Manager with Workload Identity for dynamic secrets.

## Rationale
- Multi-cluster GKE deployments with regional message brokers strictly enforce GDPR and HIPAA data residency by preventing unauthorized cross-region data transit.
- Microservices communicating via gRPC over Istio mTLS, combined with dedicated low-bandwidth optimization and OPA policy enforcement, guarantee secure, scalable, and resilient healthcare operations.