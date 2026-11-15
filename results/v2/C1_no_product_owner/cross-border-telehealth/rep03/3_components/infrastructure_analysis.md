## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The infrastructure architecture ensures strict data residency, regulatory compliance, and resilience for low-bandwidth users across GCP regions.

## Key Elements
- Regional GKE Clusters (`europe-west3`, `us-central1`)
- Istio Service Mesh (Ingress and Egress Gateways)
- Google Cloud VPC Service Controls
- External Secrets Operator and GCP Secret Manager
- ArgoCD (Regional GitOps instances)
- Prometheus & Google Cloud Operations Suite
- Cloud KMS (Customer-Managed Encryption Keys with regional key rings)
- cert-manager & Private CA
- GKE Workload Identity
- Falco Runtime Security

## Relationships
- API Gateway -> Istio Ingress Gateway (HTTPS/REST/gRPC): Routes external client traffic into regional GKE clusters.
- Istio Service Mesh -> Core Telehealth & AI Services (mTLS/gRPC): Secures internal container-to-container communication.
- Regional GKE Clusters -> Cloud KMS (Internal GCP APIs via VPC-SC): Performs region-locked cryptographic operations for data-at-rest encryption (BYOK).
- Istio Service Mesh (Egress) -> External Consent Validator (mTLS/gRPC): Inspects and authorizes cross-region (EU-US) payloads using patient consent tokens.

## Technology Stack
- Google Kubernetes Engine (GKE): Orchestrates containerized workloads across regional boundaries.
- Istio: Manages zero-trust service mesh networking, mTLS, and cross-border traffic governance.
- GCP VPC Service Controls: Establishes hard network perimeters to prevent cross-region data exfiltration.
- Cloud KMS: Provides region-isolated Customer-Managed Encryption Keys (CMEK) for data-at-rest.
- cert-manager: Automates short-lived X.509 certificate management for mesh security.
- Falco: Delivers real-time kernel-level runtime threat detection within Kubernetes.

## Rationale
This architecture uses regional isolation, hard network perimeters, and zero-trust mesh routing to strictly enforce GDPR and HIPAA data residency requirements. It integrates robust observability, automated GitOps, and workload identity to guarantee high availability and cryptographic accountability across borders.