## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for clinical IT environments. It ensures HIPAA/GDPR compliance, 99.99% availability, and 10-year data retention across a hybrid cloud topology.

## Key Elements
- Patients & Clinic Staff (Users)
- External Labs & Imaging Systems (External Systems)
- Third-Party Insurance Gateways (External Systems)
- Clinic Management System Core (System)
- API Gateway with NGINX Ingress (Container)
- Internal Microservices via gRPC (Containers)
- PostgreSQL Databases & Apache Kafka (Containers)
- Local-First Envoy Sidecars & Caching Layers (Containers)

## Relationships
- Patients & Staff interact with API Gateway via HTTPS (OAuth 2.0 / OIDC)
- Labs & Imaging interact with CMS via HL7 FHIR over mutual TLS (mTLS)
- Insurance Gateways interact via Apache Kafka over TLS 1.3
- Internal services communicate via gRPC over mTLS protected by service mesh
- Cross-site replication uses Kafka MirrorMaker 2 across hybrid links

## Technology Stack
- Kubernetes (on-prem-k8s and AWS eu-central-1): Hybrid deployment for high availability
- ArgoCD: GitOps pipeline management and state synchronization
- Apache Kafka: Asynchronous message queuing for resilient billing and claim submissions
- NGINX Ingress: API Gateway pattern for edge routing, rate-limiting, and TLS termination
- Envoy Sidecar: Local-first caching and resilience during WAN outages
- PostgreSQL: Primary persistence layer with AES-256 encryption at rest
- OpenTelemetry: Distributed tracing for EMR latency performance monitoring

## Rationale
The hybrid architecture combines local-first caching with active-active cloud clusters to maintain sub-second EMR performance and survive WAN outages. Strict mTLS, HSM key management, and automated WORM logging fulfill HIPAA and GDPR security mandates.