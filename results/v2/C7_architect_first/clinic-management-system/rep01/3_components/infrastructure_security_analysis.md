## Overview
The Clinic Management System is a hybrid healthcare platform designed to manage patient admissions, EMRs, scheduling, and billing while ensuring strict HIPAA/GDPR compliance. It provides high-availability (99.99%) clinical operations across on-premise Kubernetes clusters and AWS (eu-central-1).

## Key Elements
- Service Mesh Control Plane & Envoys (Istio)
- Secrets & Key Management Service (HashiCorp Vault & AWS KMS with FIPS HSM backing)
- GitOps Deployment Engine (ArgoCD)
- Observability & Distributed Tracing Pipeline (OpenTelemetry, Prometheus, Grafana Tempo)
- Policy & Identity Enforcement Engine (Open Policy Agent / OPA)
- Distributed Policy Cache (Redis / OPA sidecar caching)
- Secrets & Key Replication Manager

## Relationships
- API Gateway -> Service Mesh Control Plane & Envoys: Enforces ingress security and mutual TLS [gRPC]
- EMR Core Service -> Secrets & Key Management Service: Fetches envelope encryption keys with local caching [gRPC / HTTPS]
- System Administrators -> GitOps Deployment Engine: Triggers hybrid deployments [Git/HTTPS]
- All Containers -> Observability & Distributed Tracing Pipeline: Exports metrics, logs, and traces [OTLP/gRPC]
- Policy & Identity Enforcement Engine -> Distributed Policy Cache: Reads cached evaluation rules [In-memory / Local IPC]

## Technology Stack
- Istio Service Mesh: Manages mTLS and zero-trust traffic policies across hybrid clusters.
- HashiCorp Vault & AWS KMS: Enforces AES-256 encryption at rest and FIPS-validated key management.
- Open Policy Agent (OPA): Provides fine-grained ABAC and patient consent enforcement.
- OpenTelemetry, Prometheus, Grafana Tempo: Delivers distributed tracing and PHI-scrubbed observability.
- Redis / OPA sidecars: Localizes policy evaluation to maintain <50ms latency budgets.

## Rationale
This architecture uses a secure, zero-trust service mesh and distributed caching to enforce HIPAA/GDPR compliance without violating the strict <1s P95 EMR performance requirement. Hybrid replication and declarative GitOps ensure 99.99% availability and high resilience across on-premise and cloud environments.