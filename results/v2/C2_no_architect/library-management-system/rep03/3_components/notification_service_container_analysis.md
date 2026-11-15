## Overview
The Library Management System is a EU-compliant platform for public and academic libraries to catalogue items and manage circulation. The Notification Service Container manages secure, reliable, and privacy-compliant user communications.

## Key Elements
- Library Patrons and Library Staff (Users)
- Notification Service Container (Kubernetes Microservice)
- EU-Hosted Email/SMS Gateway (External System)
- EU Cloud Infrastructure Boundary & Audit and Compliance Trust Zone
- Kubernetes Egress Gateway with FQDN filtering

## Relationships
- API Gateway Container -> Notification Service Container: Triggers notifications [mTLS, internal Kubernetes network policies, JWT claims]
- Notification Service Container -> EU-Hosted Email/SMS Gateway: Sends external messages [HTTPS, short-lived credentials via SPIFFE/SPIRE, field-level encryption]
- Notification Service Container -> Audit and Compliance Trust Zone: Emits tamper-evident audit logs and delivery statuses [Encrypted network transport]
- Notification Service Container -> In-Region APM and Log Aggregation Pipeline: Streams scrubbed metrics and traces [OpenTelemetry, W3C Trace Context]

## Technology Stack
- Kubernetes & HPA: Container orchestration and queue-driven horizontal autoscaling for bulk notification management
- SPIFFE/SPIRE: Workload identity for secure, credential-less authentication to external communication gateways
- OpenTelemetry: Distributed tracing and metrics collection with automated PII scrubbing
- Encrypted Persistent Volumes: Backing for the persistent Dead Letter Queue (DLQ) enforcing EU data residency

## Rationale
This architecture ensures strict compliance with EU data residency and GDPR privacy mandates through egress filtering, PII masking, and encrypted storage. It guarantees high reliability and scalability for critical library notifications via resilient queueing and autoscaling.