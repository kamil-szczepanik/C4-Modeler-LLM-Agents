## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability across distributed regional clusters.

## Key Elements
* **Patients & Licensed Clinicians**: End-users accessing mobile/web applications.
* **GCP GKE Regional Clusters**: Isolated container orchestration platforms deployed in `europe-west3` (EU) and `us-central1` (US).
* **Kubernetes Ingress Controllers (NGINX / Envoy)**: Manages TLS termination and ingress traffic routing.
* **Network Policy Enforcer (GKE Dataplane V2 / eBPF)**: Enforces pod isolation and namespace segmentation.
* **Log Forwarder & OTel Collectors (Fluentbit / OpenTelemetry)**: Streams audit logs and telemetry data.
* **Core Telehealth & AI Inference Services**: Microservices handling video streaming, prescriptions, and AI symptom analysis.

## Relationships
* **Patients/Clinicians to GCP API Gateway**: HTTPS/gRPC for application traffic.
* **Ingress Controllers to Internal Microservices**: HTTPS/gRPC for container-to-container communication.
* **Log Forwarder/OTel to GCP Cloud Logging/Monitoring**: gRPC/HTTPS for telemetry and audit streaming.
* **Network Policy Enforcer**: Layer 3/4 eBPF protocols for internal workload isolation.

## Technology Stack
* **GCP GKE Regional Clusters**: Container orchestration enforcing regional data boundaries.
* **GKE Dataplane V2 / eBPF**: Network policy enforcement for security isolation.
* **Fluentbit & OpenTelemetry**: Standardized logging and tracing for regulatory traceability.
* **ArgoCD**: GitOps continuous deployment ensuring consistent multi-region state.
* **Google Cloud KMS**: Customer-Managed Encryption Keys (CMEK) for regional data-at-rest encryption.

## Rationale
This architecture isolates EU and US health data within designated GCP regions to satisfy strict GDPR and HIPAA compliance mandates. Multi-zonal cluster deployment and GitOps-driven zero-downtime upgrades guarantee continuous availability for critical telehealth consultations, even under unstable network conditions.