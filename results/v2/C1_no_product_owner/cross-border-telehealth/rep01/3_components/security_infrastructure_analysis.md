## Overview
The Cross-Border Telehealth Platform provides secure, compliant video consultations, e-prescriptions, and AI symptom checking for patients across the EU and US. The architecture enforces strict regional data residency, privacy controls, and zero-trust security on Google Cloud Platform.

## Key Elements
- **Clients**: Web and mobile applications used by patients and clinicians.
- **Identity-Aware Proxy (IAP)**: Google Cloud IAP for edge authentication and zero-trust perimeter enforcement.
- **Istio Service Mesh**: Secures service-to-service communication with strict mTLS and SPIFFE/SPIRE workload identities.
- **Policy Enforcement Engine**: OPA-Gatekeeper integrated with Istio via Envoy for runtime data residency validation.
- **Audit Logging Collector**: Fluentbit and Google Cloud Audit Logs pipelines routing to region-locked WORM storage.
- **ArgoCD (Hub-and-Spoke)**: Localized GitOps control planes per region (`europe-west3` and `us-central1`).
- **External Secrets Operator**: Manages dynamic secrets retrieval from regional GCP Secret Manager instances.
- **Security & Infrastructure**: GCP KMS managing regional Customer-Managed Encryption Keys (CMEK) and cryptographic erasure.

## Relationships
- *Clients* uses *Identity-Aware Proxy* via HTTPS/OIDC for edge authentication.
- *Policy Enforcement Engine* uses *Istio Service Mesh* via Envoy Ext-Authz to inspect inter-service traffic headers for regional compliance.
- *Istio Service Mesh* validates workload identities against *SPIFFE/SPIRE* via gRPC for zero-trust authorization.
- *Audit Logging Collector* writes to *Regional GCS Buckets* via HTTPS using regional GCP KMS keys for WORM-compliant encryption.
- *ArgoCD (EU)* and *ArgoCD (US)* manage *Kubernetes Control Planes* (`europe-west3`, `us-central1`) via Kubernetes API.
- *External Secrets Operator* reads from *GCP Secret Manager* via IAM Workload Identity for regional secret synchronization.

## Technology Stack
- **Cloud Provider**: Google Cloud Platform (`europe-west3` for EU, `us-central1` for US) to enforce geographic data residency.
- **Networking & Security**: Istio Service Mesh, Google Cloud IAP, OPA-Gatekeeper, SPIFFE/SPIRE for zero-trust networking and runtime policy enforcement.
- **Secret & Key Management**: GCP KMS and GCP Secret Manager with regional CMEK key rings for data protection and cryptographic erasure.
- **GitOps & Delivery**: Hub-and-spoke ArgoCD instances and External Secrets Operator for region-isolated deployments.
- **Observability**: Fluentbit and Google Cloud Audit Logs for tamper-evident compliance logging.

## Rationale
This architecture guarantees strict regulatory compliance with GDPR, HIPAA, and EU MDR by enforcing regional data isolation, cryptographic shredding, and WORM storage audit sinks. The hub-and-spoke GitOps model and Istio service mesh ensure high availability and zero-trust security even under unstable network conditions.