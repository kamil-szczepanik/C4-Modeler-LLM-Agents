## Overview
Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture relies on regional cloud infrastructure to enforce strict data residency and regulatory compliance.

## Key Elements
- Regional GKE Clusters (`europe-west3` and `us-central1`)
- Istio Service Mesh & Envoy Gateways
- Localization & Regulatory Service
- WebRTC Media Server Containers (SFUs)
- AI Symptom Checker Container
- Fluent Bit & Google Cloud Logging
- GCP Cloud Storage with Object Retention Policies

## Relationships
- Patients & Clinicians -> Regional GKE Clusters: Access video consultations and portal via HTTPS/TLS and WebRTC
- Regional GKE Clusters -> GCP Cloud Storage: Store immutable AI audit logs via secure internal APIs
- Localization & Regulatory Service -> Regional Databases: Manage consent data via SQL/TLS with CMEK encryption
- Istio Service Mesh -> Pods: Enforce mandatory mTLS and authorization policies for all intra-cluster traffic

## Technology Stack
- Google Kubernetes Engine (GKE): Container orchestration for regional workloads
- Istio & Envoy: Service mesh and ingress optimization for unstable rural connections
- GCP Cloud KMS: Customer-Managed Encryption Keys for data at rest isolation
- Fluent Bit: Edge log-forwarding and PII stripping for regulatory compliance
- GCP Cloud Storage: Immutable regional storage for AI MDR traceability logs

## Rationale
Regional GKE clusters guarantee complete separation of EU and US health data, satisfying strict GDPR and HIPAA mandates. Localized multi-zonal resilience and Istio ingress optimizations ensure stable performance for rural patients without violating cross-border data boundaries.