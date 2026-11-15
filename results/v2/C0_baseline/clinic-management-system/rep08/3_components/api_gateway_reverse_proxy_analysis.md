## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It provides a highly available, secure, and interoperable clinical IT architecture complying with HIPAA and GDPR standards.

## Key Elements
- Patients, Clinicians, Administrative Staff, Compliance Officer / Auditor
- API Gateway / Reverse Proxy (Envoy/NGINX) with Edge Listener, Authentication, Rate Limiting, Routing, Token Transformation, Error Formatting, and WAF components
- Patient Portal App (React/Node.js)
- Clinical Core Service (Go/Spring Boot with Redis/RocksDB)
- Interoperability Engine (HAPI FHIR/Apache Camel)
- Billing & Claims Service (Spring Boot)
- Sync Orchestrator (Custom Go/Java)
- External Systems: Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, SIEM & Immutable Cold Storage, Administrative Dashboard

## Relationships
- Patient Portal App -> API Gateway / Reverse Proxy: Sends API requests [HTTPS / TLS 1.3]
- API Gateway / Reverse Proxy -> Clinical Core Service: Routes internal traffic and enforces schema validation [gRPC over mTLS (Istio service mesh)]
- API Gateway / Reverse Proxy -> Billing & Claims Service: Routes billing traffic [gRPC over mTLS]
- API Gateway / Reverse Proxy -> Identity Provider: Validates tokens and introspects sessions [HTTPS / OIDC]
- API Gateway / Reverse Proxy -> SIEM & Immutable Cold Storage: Exports sanitized access logs [OTLP / gRPC]
- API Gateway / Reverse Proxy -> Administrative Dashboard: Serves telemetry metrics [Prometheus / HTTPS]

## Technology Stack
- Envoy/NGINX: API Gateway for secure routing, rate limiting, and TLS termination
- Redis: Edge caching and rate limit storage for performance and availability
- Istio: Service mesh providing mTLS and service-to-service security
- React/Node.js & Go/Spring Boot: Container application runtimes for web and microservices
- HAPI FHIR/Apache Camel: Healthcare interoperability engine for HL7 standards
- Kubernetes (on-prem-k8s) & AWS (eu-central-1): Hybrid cloud deployment infrastructure

## Rationale
The hybrid architecture utilizes regional failover and active-active Kubernetes clusters to guarantee the required 99.99% availability. Strict edge security controls, mTLS encryption, and token transformation ensure full HIPAA and GDPR compliance for sensitive clinical data.