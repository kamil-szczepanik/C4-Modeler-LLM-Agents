## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to handle patient admissions, electronic medical records, scheduling, and billing. It provides high availability, stringent security compliance, and robust interoperability for clinical workflows.

## Key Elements
- Users: Patient, Receptionist / Front Desk, Clinician / Doctor, Billing Specialist
- External Systems: Identity Provider (IdP), External Lab & Imaging Systems, Insurance Clearinghouses, Payment Gateway, SIEM / Observability System, Centralized Vault
- Containers: API Gateway (NGINX / Kong), Web Application (React SPA), Core Services (Spring Boot / Java), Billing Service (Node.js / Express), Integration Service (Apache Camel), Data Tier (PostgreSQL with Citus, Redis, Kafka/RabbitMQ)
- Gateway Components: TLS Termination Module, Auth & JWT Validation Filter, Rate Limiting Middleware, Dynamic Router & Load Balancer, Telemetry Exporter, Async Audit & Compliance Logger

## Relationships
- Patient, Receptionist, Clinician, Billing Specialist -> API Gateway: Accesses system capabilities via HTTPS / WSS, TLS 1.3, OAuth2 token validation, and MFA
- API Gateway -> Web Application: Serves React SPA via NGINX
- API Gateway -> Centralized Vault: Fetches dynamic secrets via AppRole tokens
- API Gateway -> Core / Billing Services: Forwards requests over mTLS via Istio Service Mesh using gRPC / HTTPS
- Auth Filter -> Audit & Compliance Logger: Dispatches redacted access events asynchronously via an in-memory channel

## Technology Stack
- API Gateway: NGINX / Kong for reverse proxy and edge routing
- Security: OAuth2, JWT, TLS 1.3, and Istio mTLS for zero-trust internal transport
- Backend Services: Spring Boot (Java) for Core Services and Node.js / Express for Billing
- Integration & Data: Apache Camel for HL7 FHIR integration, PostgreSQL with Citus, Redis for distributed rate-limiting, Kafka/RabbitMQ for messaging
- Deployment & Infrastructure: Kubernetes (on-prem-k8s and AWS eu-central-1), ArgoCD for canary deployments, OpenTelemetry and Prometheus for observability

## Rationale
This architecture ensures HIPAA and GDPR compliance through strict edge authentication, data masking, and asynchronous audit logging. It achieves 99.99% availability and meets sub-second EMR performance via active-active hybrid deployment, Redis rate-limiting, and async decoupling.