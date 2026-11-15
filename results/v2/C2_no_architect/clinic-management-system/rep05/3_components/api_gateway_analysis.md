## Overview
The Clinic Management System is a hybrid cloud platform designed to securely manage patient admissions, electronic medical records (EMR), scheduling, and billing for healthcare providers. It ensures high availability (99.99%), strict regulatory compliance (HIPAA, GDPR), and interoperability with external clinical systems.

## Key Elements
- Patients, Clinical Staff, Administrative/Billing Staff, Compliance Officers
- API Gateway (Istio Service Mesh, Envoy proxy)
- Patient Portal (React, Web)
- EMR & Billing Containers (Java, Spring Boot, PostgreSQL, PgBouncer)
- Analytics & Audit Reporting Container (Python, OpenTelemetry, Datadog/Prometheus)
- Patient Notification Microservice (Node.js)
- External Lab and Imaging Systems

## Relationships
- Users -> API Gateway: Access workflows via HTTPS [HTTPS / OAuth2 / OIDC / DPoP]
- API Gateway -> Patient Portal & Downstream Containers: Routes traffic and enforces policies [gRPC / HTTPS with mTLS / SPIFFE/SPIRE]
- EMR & Billing Containers -> PostgreSQL: Persists clinical and financial data [TCP / AES-256]
- API Gateway -> External Lab/Imaging Systems: Interoperates via standardized healthcare interfaces [HL7 FHIR APIs]

## Technology Stack
- Istio Service Mesh & Envoy: Provides geo-distributed multi-cluster routing, rate-limiting, and circuit breaking for 99.99% availability.
- Java Spring Boot & PostgreSQL: Powers robust EMR and billing microservices with PgBouncer connection pooling.
- OpenTelemetry & Prometheus: Injects distributed tracing and metrics at the proxy layer for P95 latency tracking (<1s).
- ArgoCD: Manages GitOps-based configuration syndication across hybrid environments (`on-prem-k8s` and `eu-central-1`).

## Rationale
This architecture uses an active-active hybrid multi-cluster deployment with Envoy and Istio to meet strict 99.99% uptime and low-latency performance targets. Perimeter security controls, DPoP token binding, and mTLS satisfy HIPAA and GDPR mandates without degrading core clinical workflows.