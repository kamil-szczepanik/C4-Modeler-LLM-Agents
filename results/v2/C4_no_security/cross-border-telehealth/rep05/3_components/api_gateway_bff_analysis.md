## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict cross-border data residency compliance, regulatory traceability, and resilient performance for rural users.]

## Key Elements
• Patients & Clinicians (Users)
• Regional Edge Router & Policy Enforcer (Envoy with Wasm filters)
• BFF Orchestration Layer (Node.js)
• Video Consultation Service (MediaSoup WebRTC SFU)
• AI Symptom Checker Service (Python / FastAPI)
• Consent & Identity Service (Keycloak)
• Integration & Interoperability Service (REST, HL7 FHIR)

## Relationships
• Patients & Clinicians -> Regional Edge Router & Policy Enforcer: Sends client requests [HTTPS / WebSockets / WebRTC (UDP/TCP)]
• Regional Edge Router & Policy Enforcer -> BFF Orchestration Layer: Forwards authorized geo-compliant traffic [HTTP/2]
• BFF Orchestration Layer -> Video Consultation Service: Forwards video traffic [gRPC]
• BFF Orchestration Layer -> AI Symptom Checker Service: Forwards symptom analysis requests [gRPC]
• BFF Orchestration Layer -> Consent & Identity Service: Validates user sessions and access tokens [gRPC]
• BFF Orchestration Layer -> Integration & Interoperability Service: Routes interoperability requests [gRPC]

## Technology Stack
• GCP (europe-west3, us-central1): Targets regional data residency constraints for EU and US compliance.
• Envoy with Wasm filters: Provides native edge routing, TLS termination, and low-latency policy enforcement without extra network hops.
• Node.js: Powers the BFF Orchestration Layer for dynamic response aggregation and payload shaping.
• OpenTelemetry & Prometheus: Enables distributed tracing and observability for audit logging and latency tracking.

## Rationale
[Consolidating security filters directly into Envoy eliminates internal latency to support rural connections below 300 kbit/s. Multi-region GCP deployment with Anycast routing guarantees strict data residency and high availability across the EU and US.]