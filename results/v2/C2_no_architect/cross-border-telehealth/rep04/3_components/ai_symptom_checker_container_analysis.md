## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and robust handling of unstable rural internet connections.

## Key Elements
- Patients (EU & US), Licensed Clinicians, Compliance & Regulatory Officers
- AI Symptom Checker Container (Python, TensorFlow, Distroless base image, gVisor runtime)
- API Gateway (Istio Service Mesh, Envoy proxy)
- Audit Sidecar and WORM Cloud Storage
- Dead Letter Queue (Google Cloud Pub/Sub)
- Regional GKE Clusters (Google Kubernetes Engine in `europe-west3` and `us-central1`)
- Cloud KMS (Customer-Managed Encryption Keys)

## Relationships
- Patients/Frontend -> API Gateway: Secure client requests [HTTPS, TLS 1.3]
- API Gateway -> AI Symptom Checker Container: Ingress routing and OAuth2/OIDC validation [Istio mTLS]
- AI Symptom Checker Container -> WORM Cloud Storage: Sends immutable audit logs [gRPC/HTTPS]
- AI Symptom Checker Container -> Cloud Pub/Sub DLQ: Handles failed asynchronous store-and-forward submissions [Encrypted TLS 1.3]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider for regional infrastructure isolation
- Google Kubernetes Engine (GKE): Container orchestration using `europe-west3` and `us-central1` regions
- Istio Service Mesh / Envoy: Manages mTLS, ingress traffic, and distributed tracing via OpenTelemetry
- Python / TensorFlow: Core framework for AI symptom analysis running on distroless base images
- Google Cloud gVisor: Runtime sandboxing for container isolation during model inference
- Kubernetes KEDA: Horizontal pod autoscaling based on queue metrics
- Google Cloud Pub/Sub: Dead Letter Queue (DLQ) for asynchronous payload handling

## Rationale
This architecture isolates EU and US health data within regional GKE clusters to satisfy GDPR and HIPAA residency mandates. Using Istio mTLS, gVisor sandboxing, regional CMEK encryption, and a consent-bound asynchronous processing pipeline ensures strict regulatory compliance, model traceability, and high availability for rural patients.