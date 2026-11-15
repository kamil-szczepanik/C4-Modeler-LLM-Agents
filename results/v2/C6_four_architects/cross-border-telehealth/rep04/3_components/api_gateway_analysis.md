## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and EU MDR traceability.

## Key Elements
- Ingress Layer: Google Cloud Global HTTPS Load Balancer, Google Cloud Armor, Google Cloud DNS
- API Gateway (Google Cloud API Gateway) containing:
  - Authentication & Token Validator Component (Envoy/Lua-based JWT validator)
  - Region Routing & Geofencing Filter (Custom Envoy Filter / Cloud API Gateway Extension)
  - Rate Limiter & Threat Protection Component (Redis-backed Rate Limiter)
  - Request Telemetry & Audit Injector Component (OpenTelemetry SDK / Custom Interceptor)
  - Payload Validation & Sanitization Component (JSON Schema / OpenAPI Validator)
  - Service Discovery & Upstream Router Component (Envoy Cluster Manager / gRPC Resolver)
- Distributed Rate Limiter Cache (Google Cloud Memorystore / Redis)
- Core Telehealth Service (Node.js / Go)
- Video Consultation Service (LiveKit)
- AI Symptom Checker Service (Python / FastAPI)
- Consent Management Service (Go)
- E-Prescription & Interoperability Gateway (Node.js / TypeScript, Java / Spring Boot FHIR Adapter)
- Audit & Compliance Logging Service (Go)
- Message Broker (Google Cloud Pub/Sub)
- Database (Google Cloud SQL for PostgreSQL)

## Relationships
- Ingress Layer -> Authentication & Token Validator Component [HTTPS]
- Authentication & Token Validator Component -> Payload Validation & Sanitization Component [Internal]
- Payload Validation & Sanitization Component -> Region Routing & Geofencing Filter [Internal]
- Region Routing & Geofencing Filter -> Request Telemetry & Audit Injector Component [Internal]
- Region Routing & Geofencing Filter -> Service Discovery & Upstream Router Component [Internal]
- Rate Limiter & Threat Protection Component -> Distributed Rate Limiter Cache [RESP / TCP]
- Request Telemetry & Audit Injector Component -> Audit & Compliance Logging Service [gRPC over mTLS]
- Service Discovery & Upstream Router Component -> Core Downstream Services [gRPC over mTLS]

## Technology Stack
- Cloud Provider: GCP (regions `europe-west3` and `us-central1`) for regional data residency isolation
- API & Edge Gateway: Google Cloud API Gateway with Envoy-based internal components
- Caching & Rate Limiting: Google Cloud Memorystore (Redis) for sliding-window rate limits
- Backend Services: Node.js, Go, Python (FastAPI), Java (Spring Boot)
- Real-time Video: LiveKit for unstable rural internet connections
- Interoperability & Standards: HL7 FHIR (US) and national e-prescription standards (EU)

## Rationale
The GCP multi-region architecture guarantees health data remains strictly within the EU (`europe-west3`) or US (`us-central1`) to satisfy GDPR and HIPAA mandates. The Envoy-based API gateway components enforce regional routing, payload validation for EU MDR compliance, and telemetry logging at the edge.