## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMR, scheduling, and billing for healthcare clinics. It ensures 99.99% uptime, strict HIPAA/GDPR compliance, and seamless offline resilience via edge synchronization.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists
- API Gateway (Envoy / NGINX)
- Web Application Container (React / Next.js)
- Clinical & EMR Core Container (Spring Boot / Java)
- Billing & Claims Container (Node.js / Express)
- HL7 FHIR Integration Container (Apache Camel)
- Edge Sync Container (Go Daemon with Outbox Poller, Encryption & Transformer, Cloud Sync Client, DLQ & Spool Manager components)
- Primary DB & Audit Store (PostgreSQL with Patroni)
- External Systems: Identity Provider, Payment Gateway & Insurance Clearinghouse, External Lab & Imaging Systems

## Relationships
- Web Application Container -> API Gateway: HTTP/REST [TLS 1.3]
- API Gateway -> Clinical & EMR Core Container: gRPC / HTTP/2
- Edge Sync Container -> Primary DB & Audit Store: Reads un-synced events [SQL]
- Edge Sync Container -> Cloud Tier: Syncs encrypted data [gRPC over mTLS]
- HL7 FHIR Integration Container -> External Lab & Imaging Systems: Interoperability [HL7 FHIR REST APIs]

## Technology Stack
- Go: Selected for the Edge Sync Container due to low memory footprint, fast startup, and native concurrency.
- PostgreSQL with Patroni: Chosen for high availability and transactional outbox pattern implementation.
- gRPC over mTLS: Used for secure, high-performance cloud synchronization.
- Kubernetes: Deployed via hybrid on-premise K8s and AWS eu-central-1 for high availability.

## Rationale
This architecture uses an active-active hybrid model with edge-sync capabilities to guarantee continuous offline patient care during internet outages. The design strictly enforces HIPAA/GDPR compliance through end-to-end encryption, local disk spooling, and isolated audit trails.