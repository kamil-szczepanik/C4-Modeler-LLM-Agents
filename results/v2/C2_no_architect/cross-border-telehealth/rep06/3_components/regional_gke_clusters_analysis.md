## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It ensures strict regulatory compliance, data residency, and reliable healthcare delivery over unstable connections.

## Key Elements
- Patients, Licensed Clinicians, Platform Administrators, Compliance Auditors
- Regional GKE Clusters (Google Kubernetes Engine, `europe-west3`, `us-central1`)
- API Gateway Container (Istio Service Mesh, OAuth2/OIDC JWT, ABAC)
- WebRTC SFU Media Servers
- AI Symptom Checker Container
- GCP Cloud Armor, Cloud CDN
- External Pharmacies, National Health Authorities, WORM Audit Logs

## Relationships
- Regional GKE Clusters -> External Pharmacies: Transmits e-prescriptions via national standards and HL7 FHIR
- Regional GKE Clusters -> National Health Authorities: Interoperates via REST APIs with mTLS
- Regional GKE Clusters -> WORM Audit Logs: Streams tamper-proof Kubernetes audit logs using Fluentbit/Vector
- Patients/Clinicians -> GCP Cloud Armor/Cloud CDN: Connects securely via HTTPS and WebRTC

## Technology Stack
- Google Cloud Platform (GCP): Chosen for robust multi-region infrastructure (`europe-west3`, `us-central1`).
- Google Kubernetes Engine (GKE): Provides regional container orchestration and auto-scaling.
- Istio Service Mesh: Manages mTLS, traffic routing, and outlier detection.
- Google Cloud KMS: Enforces customer-managed encryption keys for regional data residency.
- ArgoCD (GitOps) & Velero: Ensures drift-free declarative states and regional backups.

## Rationale
Regional GKE clusters enforce strict data residency to satisfy GDPR and HIPAA requirements. Advanced container security, adaptive streaming, and decoupled audit logging guarantee compliance, traceability, and high availability in rural areas.