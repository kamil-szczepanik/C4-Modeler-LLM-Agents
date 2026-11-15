## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency and GDPR/HIPAA compliance via GCP.

## Key Elements
*   **Clients:** Web/Mobile Client Application (Flutter / React)
*   **Edge:** Cloud Load Balancing & Envoy API Gateway (Envoy & GCP Cloud Load Balancing)
*   **Core Containers:** Core Telehealth & Consent Container (Go), AI Symptom Checker Container (Python / FastAPI), Prescription Integration Container (Go)
*   **Internal Components (Go):** Consent Management Component, Consultation Workflow Orchestrator, Regional Data Router, Consent Event Bus
*   **External/Data Services:** Regional Cloud SQL, WebRTC SFU Media Relay, Break-Glass Identity Provider (IdP), Immutable Storage, National E-Prescription Networks (EU), US Pharmacy Systems

## Relationships
*   *Web/Mobile Client* -> *Envoy API Gateway*: HTTPS / TLS 1.3
*   *Envoy API Gateway* -> *Core Telehealth & Consent Container*: gRPC / mTLS (SPIFFE/SPIRE)
*   *Core Telehealth & Consent Container* -> *AI Symptom Checker Container*: gRPC / mTLS with correlation IDs
*   *Regional Data Router* -> *Regional Cloud SQL*: SQL / TLS with regional CMEK
*   *Consent Management* -> *Consent Event Bus* -> *Workflow Orchestrator*: In-process Go channels / NATS

## Technology Stack
*   **Cloud Infrastructure:** Google Cloud Platform (GCP) across `europe-west3` and `us-central1` for regional data residency.
*   **Orchestration & Deployment:** GKE Autopilot, ArgoCD, and Kustomize for GitOps-driven regional configuration.
*   **Backend & Inter-container:** Go with gRPC, Protocol Buffers, and mTLS via SPIFFE/SPIRE.
*   **Policy & Security:** Open Policy Agent (OPA) sidecar, GCP KMS (CMEK), and OAuth2/OIDC via Break-Glass IdP.
*   **Observability:** OpenTelemetry and Google Cloud Operations.

## Rationale
This architecture ensures strict regulatory compliance (GDPR/HIPAA) by isolating patient data regionally using GCP regions and CMEK keys. Go-based microservices with gRPC and OPA sidecars provide high performance, fine-grained consent enforcement, and robust traceability required for medical device compliance.