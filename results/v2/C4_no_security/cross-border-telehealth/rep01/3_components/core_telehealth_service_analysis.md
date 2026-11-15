## Overview
[The Core Telehealth Service manages cross-border video consultations, e-prescriptions, and policy enforcement for patients in the EU and US. It ensures GDPR/HIPAA compliance, data residency, and low-bandwidth resilience.]

## Key Elements
- Consultation Orchestrator (Go)
- Consent & Policy Engine (Go, Open Policy Agent)
- Prescription Coordinator (Go)
- Notification Event Publisher (Go, Cloud Pub/Sub)

## Relationships
- Consultation Orchestrator -> WebRTC SFU Media Server: Adjusts stream parameters [gRPC / WebRTC control plane]
- Consultation Orchestrator -> Consent & Policy Engine: Validates access rights [In-memory / gRPC]
- Consultation Orchestrator -> Notification Event Publisher: Publishes stream degradation events [Asynchronous / Cloud Pub/Sub]
- Prescription Coordinator -> Notification Event Publisher: Publishes prescription status updates [Asynchronous / Cloud Pub/Sub]

## Technology Stack
- Google Kubernetes Engine (GKE): Regional container orchestration for isolated deployments
- Go: Chosen for concurrency and low memory footprint in core microservices
- Open Policy Agent (OPA): Embedded for fast, local compliance and consent rule evaluation
- Cloud Pub/Sub: Asynchronous messaging with Dead Letter Queues for decoupled event handling
- OpenTelemetry & Prometheus: Distributed tracing and real-time network telemetry

## Rationale
[This architecture separates clinical domain logic from media and notifications to maintain scalability across regions. Utilizing embedded OPA and regional GKE isolation strictly enforces data residency and rapid compliance checks.]