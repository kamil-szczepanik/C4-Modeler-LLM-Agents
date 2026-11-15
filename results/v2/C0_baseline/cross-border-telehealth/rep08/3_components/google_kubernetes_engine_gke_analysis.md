## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and compliance using a multi-tenant cloud architecture.

## Key Elements
* Google Kubernetes Engine (GKE Standard) in `europe-west3` and `us-central1`
* Ingress Controller & API Gateway Pods (Envoy / Istio Ingress)
* Workload Pods (Go, Python, Java runtimes)
* Policy & Admission Controller (OPA Gatekeeper / Kubernetes ValidatingWebhook)
* Cluster Autoscaler & Horizontal Pod Autoscaler (Kubernetes HPA)
* Runtime Security Component (Falco DaemonSet)
* OpenTelemetry Collectors (DaemonSet)
* Secret Store CSI Driver (Google Secret Manager / HashiCorp Vault)

## Relationships
* External clients connect to Ingress Controller via HTTPS/WSS
* GKE control plane communicates with worker nodes via Kubernetes API over TLS 1.3
* Internal microservices communicate via gRPC/mTLS over Istio service mesh
* Telemetry streams from OpenTelemetry DaemonSet to Cloud Logging via gRPC

## Technology Stack
* Google Kubernetes Engine (GKE Standard): Mandated for precise node-level tuning of memory-intensive media SFUs and AI inference pods
* Istio Service Mesh & Envoy: Enforces mTLS, authorization policies, and geo-routing rules
* OPA Gatekeeper: Programmatically enforces regional data residency constraints
* Falco & Cilium CNI: Provides runtime kernel monitoring and layer-3/4 network policy enforcement
* Google Cloud KMS & Binary Authorization: Secures AI model traceability for EU MDR compliance

## Rationale
GKE Standard with regional multi-tenancy enforces strict GDPR and HIPAA data residency boundaries. Automated autoscaling and strict resource quotas ensure high availability and continuous degraded-mode video consultations over unstable rural connections.