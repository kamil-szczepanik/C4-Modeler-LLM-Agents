## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker across the EU and US. It ensures stringent GDPR and HIPAA compliance while supporting unstable rural internet connections.

## Key Elements
* Configuration and Secrets Management Sidecars (GCP Secret Manager Sidecar)
* Stateless Core Application Containers
* GCP Cloud KMS (Key Management Service)
* Local Loopback Unix Domain Socket
* Observability & Telemetry Exporter Sidecars (Prometheus / OpenTelemetry)

## Relationships
* Sidecars communicate with GCP Secret Manager via gRPC/HTTPS for configuration and secrets retrieval
* Sidecars deliver configuration to Core Application Containers via local loopback Unix domain sockets
* Sidecars communicate with GCP Cloud KMS via secure APIs for ciphertext encryption and decryption
* Sidecars emit Prometheus metrics to Observability Exporter Sidecars for sync status tracking

## Technology Stack
* GCP Secret Manager Sidecar: Manages credentials and configuration decoupling from application code
* GCP Cloud KMS: Provides keys for ciphertext encryption at rest for locally cached files
* Local Unix Domain Socket: Transmits configurations securely without plain-text environment variables
* Prometheus / OpenTelemetry: Emits and exports sidecar sync status, cache rates, and decryption health metrics

## Rationale
This architecture uses GCP Secret Manager sidecars with local caching and circuit-breakers to ensure high availability and resilient bootstrapping during unstable rural network conditions. Strict IAM scoping, Unix domain sockets, and KMS encryption at rest maintain rigorous HIPAA and GDPR compliance.