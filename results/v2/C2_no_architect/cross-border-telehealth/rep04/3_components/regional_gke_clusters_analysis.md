## Overview
The Cross-Border Telehealth Platform delivers video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency and compliance via dedicated cloud infrastructure.

## Key Elements
- Regional GKE Clusters (Google Kubernetes Engine in `europe-west3` and `us-central1`)
- Istio Service Mesh with Envoy and Calico Network Policies
- ArgoCD for GitOps-driven deployment with Binary Authorization and Cosign
- Falco DaemonSet for runtime security and container anomaly detection
- Google Secret Manager and CSI Secrets Store Driver
- Prometheus and Google Cloud Managed Service for Prometheus

## Relationships
- Regional GKE Clusters -> Google Secret Manager: Injects secrets into memory via CSI Driver using gRPC/TLS
- Regional GKE Clusters -> ArgoCD: Pulls declarative configurations via HTTPS/GitOps
- Istio Service Mesh -> Pods: Enforces zero-trust microsegmentation and mTLS with SPIFFE IDs

## Technology Stack
- Google Kubernetes Engine (GKE Autopilot): Chosen for regional workload isolation and automated failover
- Istio Service Mesh & Calico: Provides Layer 3-7 zero-trust security and microsegmentation
- Google Secret Manager: Eliminates raw etcd secrets for HIPAA/GDPR compliance
- Falco: Provides real-time runtime threat detection for medical device compliance

## Rationale
This architecture guarantees strict regional data isolation between the EU and US to satisfy GDPR and HIPAA mandates. It also ensures high availability and low-latency failover for unstable rural internet connections during critical telehealth sessions.