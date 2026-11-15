## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers secure, high-availability clinical IT operations compliant with HIPAA and GDPR regulations.

## Key Elements
- **Users**: Patient, Clinician/Staff, Billing Administrator
- **External Systems**: Identity Provider (IdP), Insurance Gateway, External Lab & Imaging Systems, National Health Registry, External Archival Storage, SMS/Notification Gateway
- **API Gateway Components**: TLS Termination & Routing Engine (Nginx/Kong), Authentication & Authorization Plugin (Kong OIDC), Rate Limiting Component (Redis Enterprise), Request Audit & Logging Interceptor, WAF & Threat Protection Engine (Coraza WAF), Request Transformation & Sanitization Component, Health Check & Circuit Breaker Engine
- **Core Containers**: Patient & Scheduling Service, EMR Service, Billing Service, FHIR Interoperability Service, Background Worker
- **Infrastructure & Data**: Keycloak Container, Observability Agent (Prometheus/Grafana Promtail), Distributed Cache (Redis Enterprise), Message Broker (Apache Kafka), Primary Database (PostgreSQL), Database Access Proxy (PgBouncer), Audit Store (AWS S3 / On-Prem Object Storage), Service Mesh (Istio / Envoy)

## Relationships
- Patient / Clinician / Billing Administrator -> API Gateway: Access portal, clinical workflows, and billing [HTTPS / TLS 1.3]
- API Gateway -> Patient & Scheduling Service, EMR Service, Billing Service, FHIR Interoperability Service: Routes traffic [Istio Service Mesh (mTLS / HTTP/2)]
- API Gateway -> Keycloak Container: Validates JWT tokens and IAM requests [HTTPS / OIDC]
- API Gateway -> Distributed Cache (Redis Enterprise): Token caching and rate limit counters [RESP / TCP]
- API Gateway -> Message Broker (Apache Kafka): Offloads audit events for compliance [Kafka Protocol / TCP]
- API Gateway -> Observability Agent: Streams audit and access logs [Fluent Bit / gRPC]

## Technology Stack
- **API Gateway**: Nginx / Kong with Coraza WAF for edge security and threat protection
- **Services**: Java / Spring Boot for core clinical services, Node.js / TypeScript for billing, Python / FastAPI for FHIR interoperability
- **Security & IAM**: Keycloak Container with OIDC, AES-256 encryption at rest
- **Messaging & Caching**: Apache Kafka for asynchronous event streaming, Redis Enterprise for distributed caching
- **Storage**: PostgreSQL with PgBouncer proxy, AWS S3 / On-Prem Object Storage for 10-year audit retention
- **Networking & Observability**: Istio / Envoy service mesh with mTLS, Prometheus and Grafana Promtail

## Rationale
This architecture leverages a robust API gateway coupled with an Istio service mesh to ensure 99.99% active-active uptime and strict hybrid cloud interoperability. Integrated WAF, OIDC authentication, and encrypted data storage satisfy stringent HIPAA and GDPR compliance mandates.