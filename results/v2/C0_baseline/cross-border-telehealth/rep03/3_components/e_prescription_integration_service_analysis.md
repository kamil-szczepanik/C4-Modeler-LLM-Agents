## Overview
[A secure, regionally isolated e-prescription integration service for a cross-border telehealth platform, designed to dispatch prescriptions to EU national gateways and US Surescripts networks.]

## Key Elements
- Prescription Orchestrator Component (Go)
- US FHIR Adapter Component (Go)
- EU National Gateway Adapter Component (Go)
- Audit & Compliance Logger Component (Go)
- Event Dispatcher Component (Go)
- Circuit Breaker & Retry Middleware (Go)

## Relationships
- Core Telehealth Backend -> Prescription Orchestrator: gRPC over Istio mTLS mesh
- Prescription Orchestrator -> US FHIR Adapter & EU National Gateway Adapters: Internal Go interfaces
- US FHIR Adapter -> Surescripts / US Pharmacy Networks: HTTPS/REST (HL7 FHIR)
- EU National Gateway Adapters -> National E-Prescription Gateways (EU): Mutual TLS / REST
- Event Dispatcher -> Core Telehealth Backend: Google Cloud Pub/Sub

## Technology Stack
- Go: High-throughput, lightweight concurrency for regional micro-adapters
- Google Kubernetes Engine (GKE): Regionally isolated deployments in europe-west3 and us-central1
- Google Cloud Pub/Sub & Dead Letter Queues (DLQ): Resilient asynchronous message processing
- Google Secret Manager & Cloud KMS: Region-specific secret storage and cryptographic signing
- Open Policy Agent (OPA): Service-to-service authorization and RBAC/ABAC enforcement

## Rationale
[This architecture enforces strict regional data residency and compliance via isolated GKE deployments and regional secret management. It ensures high availability and resilience across unstable networks using circuit breakers, DLQs, and localized Go-based adapters.]