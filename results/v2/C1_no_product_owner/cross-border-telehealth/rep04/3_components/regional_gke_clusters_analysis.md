## Overview
Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It enforces strict regional data residency and compliance via isolated cloud infrastructure.

## Key Elements
- Regional GKE Clusters: Isolated GCP GKE clusters in `europe-west3` and `us-central1`.
- Ingress Controller: Envoy / GKE Ingress for geo-routing and TLS 1.3 termination.
- Service Mesh Control Plane: Istio for mTLS and internal traffic isolation.
- External Secrets Operator: Manages PHI keys via GCP Secret Manager and Workload Identity.
- Security & Observability Agents: Falco, Argo Rollouts, Prometheus, Grafana, and localized Cloud Logging.

## Relationships
- External Secrets Operator -> GCP Secret Manager: Fetches secrets securely via HTTPS/OIDC federation.
- Ingress Controller -> API Gateway: Routes HTTP/2 and gRPC traffic internally via ClusterIP services.
- Global Management Plane -> Regional GKE Clusters: Drives declarative cluster state via GitOps (ArgoCD).

## Technology Stack
- Google Kubernetes Engine (GKE): Container orchestration with Container-Optimized OS for isolated regional node pools.
- Istio: Service mesh for fine-grained AuthorizationPolicies and strict regional network boundaries.
- GCP Secret Manager & KMS: Externalized secret management with regional customer-managed encryption keys (CMEK) for GDPR/HIPAA compliance.
- Argo Rollouts & ArgoCD: Progressive delivery and GitOps deployment strategy for safe regional updates.

## Rationale
Isolating workloads into dedicated regional GKE clusters ensures strict compliance with EU and US data residency mandates. Integrating native GCP security tools and Istio provides robust auditability and zero-trust boundaries required for healthcare data.