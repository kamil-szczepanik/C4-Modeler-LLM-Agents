## Overview
[The system is a Cross-Border Telehealth Platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. Its core purpose is to deliver secure, compliant telemedicine services while strictly enforcing regional data residency.]

## Key Elements
- GKE Regional Clusters (`europe-west3` and `us-central1`)
- Kubernetes Control Plane (Regional Managed)
- Istio Service Mesh with SPIFFE/SPIRE
- Cilium CNI (Datapath V2 with eBPF)
- Cluster Ingress Controller (Nginx / GCP Gateway API)
- Node Pools (Standard VMs for clinical workloads; reserved non-clinical Spot VMs)
- ArgoCD (Multi-Region GitOps)
- OPA/Gatekeeper or Kyverno (Admission Control)
- Falco (Runtime Threat Detection)

## Relationships
- GKE Regional Clusters interact with Regional API Gateways (Kong / GCP Gateway API) via Cluster Ingress Controllers using HTTP/HTTPS.
- Internal microservices communicate via gRPC / HTTP/2 over mTLS enforced by Istio Service Mesh.
- Pod networking and network policies are enforced locally via Cilium CNI using eBPF data paths.
- Regional workloads securely access regional GCP Cloud Spanner and BigQuery via GKE Workload Identity.

## Technology Stack
- Google Kubernetes Engine (GKE): Container orchestration for regional isolation.
- Istio & SPIFFE/SPIRE: Zero-trust service mesh and mTLS identity verification.
- Cilium CNI (eBPF): High-performance networking and kernel-level network security enforcement.
- ArgoCD: Isolated regional GitOps deployment controllers.
- Binary Authorization & Cosign/Sigstore: Container image supply chain security.
- Falco: Kernel-level runtime threat detection.

## Rationale
[This architecture fits requirements by isolating EU and US workloads into dedicated GKE regional clusters to guarantee strict data residency and regulatory compliance. Additionally, it ensures high availability and low-latency real-time video consultations through optimized eBPF data paths and robust multi-region operational controls.]