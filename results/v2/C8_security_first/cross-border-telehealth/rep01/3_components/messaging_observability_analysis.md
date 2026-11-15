## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict regional data residency, HIPAA/GDPR compliance, and low-bandwidth resilience.

## Key Elements
- Patients and Clinicians (End users)
- API Gateway / Ingress (Envoy / GCP HTTPS Load Balancer)
- Video Consultation Service (Mediasoup WebRTC SFU containers)
- AI Symptom Checker Container (Python, FastAPI, PyTorch)
- E-Prescription Integration Container (Node.js, FHIR protocol adapters)
- Patient Consent & Profile Container (Go)
- Messaging & Observability Container (Google Cloud Pub/Sub, OpenTelemetry Collector, Cloud Audit Logs)
- Data Tier (Cloud SQL PostgreSQL, Memorystore with CMEK)
- External Systems: National E-Prescription Gateways (EU), US Pharmacy Networks, Identity Providers (IdP)

## Relationships
- Patients/Clinicians -> API Gateway / Ingress: Accesses platform services via HTTPS and WSS
- API Gateway / Ingress -> Microservices: Routes internal traffic via gRPC over mTLS
- Microservices -> Messaging & Observability (Google Cloud Pub/Sub): Publishes/subscribes to regional event topics via gRPC
- Microservices -> OpenTelemetry Collector: Pushes telemetry traces and metrics via OTLP/gRPC
- Audit Logger Component -> Cloud Storage / BigQuery: Sinks immutable audit trails via HTTPS API

## Technology Stack
- Google Cloud Platform (GCP): Primary cloud provider spanning `europe-west3` and `us-central1` regions
- Google Cloud Pub/Sub: Manages regional event-driven messaging and Dead-Letter Queues with CMEK
- OpenTelemetry: Handles distributed tracing, metrics, and telemetry data masking
- Cloud SQL PostgreSQL & Memorystore: Persists relational data and caching with regional encryption
- Terraform & ArgoCD: Automates regional GitOps deployments and infrastructure provisioning

## Rationale
This architecture strictly enforces regional data residency requirements by partitioning GCP resources between `europe-west3` and `us-central1`. It ensures high availability and regulatory compliance for healthcare workflows through automated audit logging, encrypted messaging, and low-bandwidth telemetry optimization.