## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency and purpose-based consent while maintaining low-latency availability.

## Key Elements
- Patients (EU/US), Licensed Clinicians, Compliance Auditors/Officers
- Regional API Gateway / BFF (Node.js, GraphQL)
- Consent & Policy Engine (.NET 8)
- Regional WORM Storage (GCP Cloud Storage, Cloud KMS)
- Regional Memorystore (Redis) with Pub/Sub Invalidation Bus
- GCP Memorystore (Redis) & GCP Pub/Sub DLQ

## Relationships
- Regional API Gateway / BFF -> Consent & Policy Engine: Verifies user consent and policies [gRPC, mTLS, Istio Service Mesh]
- Consent & Policy Engine -> Regional WORM Storage: Stores compliance and policy records securely [TLS 1.3, Cloud KMS]
- Consent & Policy Engine -> Regional Memorystore (Redis): Evaluates local policy caches and handles real-time Pub/Sub revocations [TCP, TLS]

## Technology Stack
- .NET 8 / ASP.NET Core: Powers the high-performance Consent & Policy Engine services
- gRPC: Enables ultra-low latency internal communication over Istio Service Mesh
- GCP Memorystore (Redis): Provides regional local-first caching and pub/sub invalidation bus
- OpenTelemetry: Streams compliance audit traces directly to GCP Cloud Logging

## Rationale
Local-first caching via Redis and cryptographic tokens ensure sub-millisecond policy evaluation and 99.999% availability, even during unstable internet connections or cross-region outages. Regional GKE deployments with strict cryptographic controls satisfy rigorous GDPR and HIPAA data residency requirements.