## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for clinics while ensuring HIPAA and GDPR compliance. The architecture utilizes a high-availability hybrid cloud deployment with Kong/Envoy API gateways and Kubernetes microservices.

## Key Elements
- **API Gateway Container:** Kong/Envoy handling ingress, routing, security, and rate limiting.
- **PWA Client Container:** Nginx and IndexedDB serving the frontend Progressive Web App.
- **Backend Services:** Patient & EMR, Scheduling, Billing, HL7 FHIR Adapter, and DICOM Services (Node.js, Docker, Kubernetes).
- **Security & Authorization:** Tenant Context & Authorization Proxy (Open Policy Agent), Data Encryption & Key Management (PKCS#11, HSM).
- **Data & Storage Tier:** PostgreSQL (CloudNativePG), Redis Enterprise, Apache Kafka, RabbitMQ, Elasticsearch, ClickHouse, and MinIO.
- **Observability & Infrastructure:** Envoy Service Mesh, OpenTelemetry, Prometheus, and Audit Sidecar.

## Relationships
- Patients, Clinical Staff, Hospital Administrators -> API Gateway Container [HTTPS/TLS 1.3]
- PWA Client Container -> API Gateway Container [HTTPS]
- API Gateway Container -> Patient & EMR, Scheduling, Billing Services [OAuth2/OIDC, gRPC over mTLS]
- API Gateway Container -> HL7 FHIR Adapter Container [gRPC]
- API Gateway Container -> Tenant Context & Authorization Proxy Container [Local gRPC loopback]

## Technology Stack
- **Ingress & Gateway:** Kong and Envoy for resilient edge routing and mTLS termination.
- **Compute & Orchestration:** Kubernetes (on-prem-k8s and AWS eu-central-1) for active-active high availability.
- **Backend Runtime:** Node.js for microservices with gRPC communication.
- **Databases & Messaging:** PostgreSQL, Redis, Apache Kafka, RabbitMQ, Elasticsearch, and ClickHouse for persistence, caching, and event streaming.
- **Security:** Open Policy Agent (OPA), OAuth2/OIDC, Wasm/ModSecurity WAF, and AES-256 encryption.

## Rationale
The hybrid Kubernetes architecture guarantees 99.99% uptime via active-active geo-distribution and automated health checks. Strict adherence to HIPAA, GDPR, and 10-year data retention is achieved through dedicated audit sidecars, AES-256 encryption, and zero-trust mTLS service meshes.