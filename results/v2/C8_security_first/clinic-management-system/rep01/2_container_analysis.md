## Overview
Clinic Management System provides patient registration, EMR, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, 99.99% uptime, and 10-year data retention across a hybrid cloud architecture.

## Key Elements
- Envoy / NGINX API Gateway
- Patient Intake Container (Python / FastAPI)
- Scheduling Engine Container (Java / Spring Boot)
- EMR Workspace Container (Go / gRPC)
- Billing & Claims Container (Node.js / TypeScript)
- Integration & FHIR Mediator (Apache Camel K / Java)
- Primary Database (PostgreSQL with Citus)
- Event Broker (Redpanda)
- Identity Provider (IdP) & HashiCorp Vault
- Observability Stack (OpenTelemetry, Grafana Mimir/Tempo, Falco)

## Relationships
- External Clients to Envoy / NGINX via HTTPS / TLS 1.3
- Inter-container communication within Kubernetes via gRPC and HTTP/2 over mTLS (Cilium network policies)
- Containers to PostgreSQL and Redpanda via encrypted internal TCP connections
- EMR and Billing to External Systems (Labs, Payment Gateways) via HL7 FHIR APIs and HTTPS
- On-premise clusters to AWS eu-central-1 via IPSec/WireGuard VPN tunnel for WORM audit log replication to AWS S3 Object Lock

## Technology Stack
- **Languages/Frameworks:** Python/FastAPI, Java/Spring Boot, Go, Node.js/TypeScript for microservices isolation and performance
- **Orchestration & Networking:** Kubernetes (on-prem-k8s and AWS eu-central-1), Cilium for zero-trust network policies and mTLS
- **Data & Messaging:** PostgreSQL with Citus, Redis for caching, Redpanda for event streaming
- **Security & Compliance:** HashiCorp Vault for dynamic secrets, Falco for runtime security, WORM storage for immutable audit logs
- **Observability & Deployment:** OpenTelemetry, Grafana Mimir/Tempo, ArgoCD for GitOps, Istio for canary deployments

## Rationale
The containerized microservices architecture with Go/gRPC for EMR guarantees sub-second screen loads (R-07) and high clinician efficiency. Hybrid deployment with active-passive replication, strict network policies, and WORM storage satisfies 99.99% availability (R-06) and 10-year regulatory retention constraints.