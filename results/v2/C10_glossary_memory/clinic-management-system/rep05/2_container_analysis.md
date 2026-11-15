## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for healthcare providers in a hybrid cloud environment. It ensures high availability and strict HIPAA/GDPR compliance across distributed clinical workflows.

## Key Elements
- Patients
- Receptionists
- Clinicians
- Billing Specialists
- API Gateway / BFF Container
- EMR Service Container
- Scheduling Service Container
- Billing Service Container
- Integration Service Container
- Clinical Database
- Audit & Observability Sidecar
- Identity Provider
- Insurance Payment Gateway
- Lab & Imaging Systems
- Hybrid API Gateway

## Relationships
- Patient Portal -> Clinic Management System via HTTPS/REST
- Lab & Imaging Systems -> Integration Service Container via HL7 FHIR over HTTPS
- Insurance Payment Gateway -> Billing Service Container via TLS 1.3
- Identity Provider -> API Gateway / BFF Container via OIDC/SAML 2.0
- API Gateway / BFF Container -> Internal containers (EMR, Scheduling, Billing, Integration) via gRPC over mTLS
- EMR Service Container -> Clinical Database via TLS 1.3

## Technology Stack
- Kong / Envoy: API Gateway / BFF Container for ingress routing and TLS termination
- Java / Spring Boot: EMR Service Container for resilient clinical record management
- Node.js / TypeScript: Scheduling Service Container for resource clash logic
- Go: Billing Service Container for high-performance claim processing
- Apache Camel / FHIR Server: Integration Service Container for HL7 interoperability
- PostgreSQL: Distributed Clinical Database with AES-256 at rest and field-level encryption
- Istio / Linkerd: Service mesh for enforcing mTLS on east-west traffic
- FluentBit / Prometheus: Audit & Observability Sidecar for metrics and tamper-evident logs
- Kubernetes: Container orchestration across on-prem-k8s and eu-central-1

## Rationale
This architecture uses microservices deployed on Kubernetes with active-active regional replication to meet the 99.99% availability requirement. Strict service mesh mTLS, field-level encryption, and automated sidecar auditing ensure comprehensive HIPAA and GDPR compliance without sacrificing sub-second EMR performance.