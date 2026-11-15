## Overview
The Clinic Management System is an enterprise healthcare platform that securely processes patient admissions, electronic medical records, scheduling, and billing. It provides high availability, stringent compliance, and seamless interoperability for medium-sized hospitals and clinics.

## Key Elements
- Clinic Receptionist / Admin
- Clinician (Doctor / Nurse)
- Billing Specialist
- Patient
- Hospital / Clinic Administrator
- External Auditors / Compliance Officers
- External Lab & Imaging Systems
- Insurance Claim Processors / Payment Gateways
- Identity Provider (IdP)
- Envoy / NGINX API Gateway
- Patient Intake Container (Python / FastAPI)
- Scheduling Engine Container (Java / Spring Boot)
- EMR Workspace Container (Go / gRPC)
- Billing & Claims Container (Node.js / TypeScript)
- Integration & FHIR Mediator (Apache Camel K / Java)
- Primary Database (PostgreSQL with Citus)
- Event Broker (Redpanda)
- Observability Stack (OpenTelemetry, Grafana Mimir/Tempo, Falco, Grafana)

## Relationships
- Users access the system via HTTPS/TLS 1.3 through the Envoy/NGINX API Gateway with multi-factor authentication.
- Application containers communicate internally via gRPC and publish events to the Redpanda Event Broker.
- Microservices ship telemetry data to the OpenTelemetry Collector via gRPC/OTLP.
- The OpenTelemetry Collector forwards metrics and traces to Grafana Mimir and Grafana Tempo via HTTP/RemoteWrite.
- Falco streams kernel-level security events to the SIEM sink via Webhook/gRPC.
- The Integration & FHIR Mediator exchanges clinical data with External Lab & Imaging Systems using HL7 FHIR APIs over HTTPS.

## Technology Stack
- **Languages & Frameworks:** Python (FastAPI), Java (Spring Boot, Apache Camel K), Go, Node.js (TypeScript) for robust service segregation and performance.
- **Database:** PostgreSQL with Citus extension for distributed, scalable relational data storage and transactional integrity.
- **Messaging & Streaming:** Redpanda for high-throughput, low-latency event-driven architecture.
- **Security & Infrastructure:** Envoy/NGINX for ingress routing, Falco for eBPF runtime security, AES-256 for data encryption at rest.
- **Observability:** OpenTelemetry, Grafana Mimir, Grafana Tempo, and Grafana UI for end-to-end metrics, traces, and compliance reporting.
- **Deployment:** Hybrid Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) ensuring active-active high availability.

## Rationale
This hybrid microservices architecture guarantees 99.99% uptime and low-latency EMR performance through containerized scaling and distributed databases. Strict adherence to HIPAA and GDPR is enforced via end-to-end encryption, robust RBAC, immutable WORM storage, and advanced telemetry PII scrubbing.