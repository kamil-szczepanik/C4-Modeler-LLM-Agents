## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing. It ensures HIPAA and GDPR compliance, 99.99% high availability, and secure interoperability via HL7 FHIR APIs.

## Key Elements
- **Users:** Receptionists, Clinicians, Billing Officers, Patients
- **External Systems:** External Lab & Imaging Systems, Third-Party Payment Gateway & Insurance Clearinghouses, Identity Provider (IdP), SIEM/Observability Platform
- **Containers:** API Gateway (Kong/Nginx), Patient-Facing UI (React/Next.js), Patient Portal (Web), Clinical Core Services (Spring Boot/Java), Interoperability Service (Apache Camel/Node.js), Billing & Claims Service (Spring Boot/Java)
- **API Gateway Components:** Edge Router & Reverse Proxy, Security & Auth Plugin Module, WAF & Rate Limiting Engine, FHIR Mediator Route, Policy Enforcement Hook, Telemetry & Audit Forwarder
- **Infrastructure:** Redis (distributed rate limiting), Kubernetes (on-prem-k8s), AWS (eu-central-1), ArgoCD/Deck (GitOps)

## Relationships
- Patients, Receptionists, Clinicians, Billing Officers -> API Gateway: Accesses system via HTTPS/TLS with JWT validation [HTTPS/TLS, JWT]
- Patient-Facing UI -> API Gateway: Communicates with backend containers using OAuth2 authorization code flow with PKCE [OAuth2, PKCE]
- API Gateway -> Clinical Core, Billing, Interoperability Service: Routes internal east-west traffic using mTLS over gRPC/HTTP2 [mTLS, gRPC/HTTP2]
- API Gateway -> SIEM/Observability Platform: Streams sanitized OpenTelemetry traces and tamper-evident audit logs asynchronously [OpenTelemetry, HTTPS]
- Interoperability Service -> Lab & Imaging Systems: Exchanges health data using HL7 FHIR APIs [REST/JSON, FHIR JSON]

## Technology Stack
- **API Gateway:** Kong Enterprise (leveraging Nginx core) for edge routing, WAF, and plugin extensibility.
- **Rate Limiting & Caching:** Redis (deployed via Redis Sentinel or active-passive replication) for distributed rate-limiting counters.
- **Backend Services:** Spring Boot (Java) and Node.js for core business logic and interoperability.
- **Deployment & Configuration:** Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) managed declaratively via GitOps (ArgoCD/Deck) to prevent configuration drift.
- **Security & Observability:** TLS 1.3 externally, mTLS internally, local JWKS verification, and OpenTelemetry for distributed tracing without PHI leakage.

## Rationale
The hybrid architecture utilizes Kong Gateway and Kubernetes across on-premises and AWS regions to guarantee active-active high availability (≥ 99.99%) and resilience against cross-environment network partitions. Security modules and local JWKS validation enforce strict HIPAA/GDPR compliance while keeping internal latency low to satisfy the P95 < 1s performance requirement.