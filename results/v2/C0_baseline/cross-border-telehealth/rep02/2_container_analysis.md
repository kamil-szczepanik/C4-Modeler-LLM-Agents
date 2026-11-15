## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI-driven symptom checker for patients across the EU and US. The architecture enforces strict regional data residency, regulatory compliance (GDPR, HIPAA, EU MDR), and high availability over unstable connections.

## Key Elements
* **Users & Personas:** Patients (EU & US), Licensed Clinicians, Platform Administrators, Support Agents, Pharmacy Partners, Regulatory Officers.
* **Client Layer:** Web / Mobile Client (React / React Native).
* **Edge & Routing:** API Gateway (Envoy / Cloud Endpoints), local TURN/STUN relays.
* **Core Containers:** Core Telehealth Service (Node.js / NestJS), AI Symptom Service (Python/FastAPI), Localization Service, Billing / Payment Container.
* **Data & Storage:** Google Cloud SQL (PostgreSQL), Cloud Storage WORM buckets.
* **Infrastructure & Security:** GCP regions (`europe-west3`, `us-central1`), ArgoCD, OpenTelemetry collectors, GCP Secret Manager, Falco (eBPF).

## Relationships
* **Client to Gateway:** HTTPS (TLS 1.3) and WSS over public internet.
* **Internal Routing:** gRPC over mTLS between API Gateway and regional backend containers.
* **Data Persistence:** TCP/TLS connections from Core Telehealth Service to regional Google Cloud SQL.
* **Audit Logging:** Direct write of immutable payloads from AI Symptom Service to regional Cloud Storage WORM buckets.
* **External Integration:** REST / HL7 FHIR to regional Pharmacy Partners.

## Technology Stack
* **Cloud Platform:** Google Protection Cloud (GCP) for isolated regional deployments.
* **Backend & AI:** Node.js/NestJS for core services; Python/FastAPI for isolated AI symptom checking.
* **Database & Storage:** Google Cloud SQL (PostgreSQL) with CMEK for localized PHI; WORM Cloud Storage for AI audit logs.
* **Networking & Resilience:** Envoy API Gateway; WebRTC SFU with local TURN/STUN relays.
* **Operations & Security:** ArgoCD for GitOps, OpenTelemetry for regional metrics, GCP Secret Manager, Falco for runtime security.

## Rationale
This containerized microservices architecture enforces strict data residency by deploying isolated stacks in `europe-west3` and `us-central1` backed by regional storage. Isolating the AI Symptom Service with WORM logging ensures explicit EU MDR traceability while meeting stringent cross-border healthcare compliance mandates.