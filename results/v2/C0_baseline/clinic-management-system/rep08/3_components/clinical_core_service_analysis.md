## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It relies on a resilient Clinical Core Service to deliver high availability, strict security, and low-latency clinical workflows.

## Key Elements
- **Users**: Patient, Clinician, Administrative Staff, Compliance Officer / Auditor
- **External Systems**: Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, SIEM & Immutable Cold Storage
- **Containers**: API Gateway / Reverse Proxy (Envoy/NGINX), Patient Portal App (React/Node.js), Clinical Core Service (Go/Spring Boot with Redis/RocksDB edge cache), Interoperability Engine (HAPI FHIR/Apache Camel), Billing & Claims Service (Spring Boot), Sync Orchestrator
- **Clinical Core Service Components**: EMR Management Component, Clinical Workflow Engine, Edge Cache & Sync Component, Audit Interceptor

## Relationships
- API Gateway -> Clinical Workflow Engine: Forwards admission and scheduling commands [gRPC over mTLS]
- Clinical Core Service -> External Lab & Imaging Systems: Exchanges diagnostic data [HL7 FHIR APIs]
- Clinical Workflow Engine -> EMR Management Component: Executes local DB queries [JDBC over SSL]
- Edge Cache & Sync Component -> EMR Management Component: Performs asynchronous eventual-consistency sync [gRPC]
- Audit Interceptor -> SIEM & Immutable Cold Storage: Streams signed, tamper-evident audit events [TLS syslog / gRPC stream]
- EMR Management Component -> External Lab & Imaging Systems: Pulls diagnostic payloads [HL7 FHIR REST over HTTPS]

## Technology Stack
- **Backend Core**: Go and Java/Spring Boot for high-performance and transactional reliability
- **Database & Cache**: PostgreSQL with JDBC over SSL, supported by Redis and embedded RocksDB for offline edge caching
- **Workflow & Sync**: Temporal for state consistency; Vector Clocks and dead-letter queues for conflict resolution
- **Security & Mesh**: Istio service mesh for mTLS, OAuth2/JWT for identity propagation, and envelope encryption with per-patient DEKs
- **Infrastructure**: Kubernetes (on-prem-k8s and eu-central-1 hybrid cloud) with Fluentbit for log shipping and LitmusChaos for failure validation

## Rationale
This architecture uses an active-active hybrid cloud model with edge caching to guarantee sub-second EMR load times and offline survivability. It enforces HIPAA and GDPR compliance through cryptographic erasure, strict RBAC/ABAC, and immutable audit streaming.