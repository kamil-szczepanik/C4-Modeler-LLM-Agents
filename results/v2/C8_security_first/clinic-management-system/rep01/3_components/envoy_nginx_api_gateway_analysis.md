## Overview
The Clinic Management System is a clinical IT platform that manages patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals. It ensures high availability, strict HIPAA/GDPR compliance, and interoperability with external healthcare systems.

## Key Elements
- **Users**: Clinic Receptionist/Admin, Clinician (Doctor/Nurse), Billing Specialist, Patient, Hospital/Clinic Administrator, External Auditors/Compliance Officers
- **External Systems**: External Lab & Imaging Systems, Insurance Claim Processors / Payment Gateways, Identity Provider (IdP) with local on-premise cache proxy
- **Containers**: Envoy / NGINX API Gateway (Envoy), Patient Intake Container (Python / FastAPI), Scheduling Engine Container (Java / Spring Boot), EMR Workspace Container (Go / gRPC), Billing & Claims Container (Node.js / TypeScript), Integration & FHIR Mediator (Apache Camel K / Java), Primary Database (PostgreSQL with Citus), Event Broker (Redpanda), Observability Stack (OpenTelemetry, Grafana Mimir/Tempo, Falco)
- **Envoy Components**: Listener & TLS Termination Component, Authentication Filter Component, Rate Limiting & WAF Filter Component, Routing & Load Balancing Component, Telemetry & Tracing Export Component

## Relationships
- Users -> Envoy API Gateway: Accesses platform workflows [HTTPS / TLS 1.3]
- Envoy API Gateway -> Internal Containers (Intake, Scheduling, EMR, Billing): Routes validated traffic [HTTP/2 / gRPC over mTLS]
- Envoy API Gateway -> Identity Provider (IdP): Validates authentication tokens [OAuth 2.0 / OIDC]
- Envoy API Gateway -> Observability Stack: Exports telemetry and access logs [OpenTelemetry / gRPC]

## Technology Stack
- **Envoy**: Chosen for native Lua/WASM extensibility, gRPC proxying efficiency, and deep OpenTelemetry integration.
- **TLS 1.3 & mTLS**: Enforces forward-secrecy cipher suites (ECDHE-ECDSA-AES256-GCM-SHA384) for ingress and service mesh communication.
- **PostgreSQL with Citus**: Provides scalable primary data storage supporting AES-256 encryption at rest.
- **OpenTelemetry & Grafana (Mimir/Tempo)**: Delivers distributed tracing and P95 latency monitoring to meet 99.99% uptime targets.

## Rationale
This architecture uses an active-active hybrid cloud deployment with an Envoy API Gateway acting as a Policy Enforcement Point to satisfy stringent HIPAA/GDPR security constraints. Decoupled microservices combined with gRPC over mTLS and comprehensive observability guarantee high availability (99.99%) and sub-second EMR performance.