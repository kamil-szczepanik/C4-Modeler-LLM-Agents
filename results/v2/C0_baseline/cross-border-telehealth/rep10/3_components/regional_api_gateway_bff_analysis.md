## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system enforces strict regional data residency and compliance using a cloud-native Google Cloud Platform architecture.

## Key Elements
- Patients (EU/US), Licensed Clinicians, Local Pharmacies, Compliance Auditors
- Regional API Gateway / BFF (Node.js, GraphQL)
- Routing & Geo-Enforcement Middleware, GraphQL Resolvers, Audit & Telemetry Interceptor, Client Context & Policy Injector
- Consent & Policy Engine (.NET), Video Session Service (Go), AI Orchestration Service (Python, FastAPI), FHIR & Prescription Integration Service (.NET)
- GCP Cloud Storage (Regional WORM Storage), Cloud KMS, GCP Cloud Monitoring, Cloud CDN, Google Kubernetes Engine (GKE)

## Relationships
- Patients & Clinicians -> Regional API Gateway / BFF via HTTPS / GraphQL / WebSockets [TLS 1.3]
- Regional API Gateway / BFF -> Consent & Policy Engine, Video Session Service, AI Orchestration Service, FHIR & Prescription Integration Service via gRPC over mTLS [Istio Service Mesh]
- Audit Interceptor -> GCP Cloud Monitoring via OTLP / gRPC
- Cloud CDN -> Regional API Gateway / BFF for static assets only (no PHI/PII caching)

## Technology Stack
- Node.js & GraphQL: Chosen for backend-for-frontend flexibility and efficient data fetching for low-bandwidth rural clients.
- Google Kubernetes Engine (GKE): Enables horizontal pod autoscaling and multi-region deployment across `europe-west3` and `us-central1`.
- Istio Service Mesh: Provides mTLS, circuit breaking, and traffic splitting for secure microservices communication.
- gRPC: Ensures low-latency, high-performance internal communication between the BFF and backend microservices.

## Rationale
This architecture guarantees strict regulatory compliance by enforcing data residency per region using Istio service mesh and geo-enforcement middleware. It maintains high availability and low-bandwidth resilience for rural users through GraphQL BFF patterns, edge compression, and GKE autoscaling.