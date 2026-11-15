## Overview
The Consent Management Service is a secure, multi-region component of the Cross-Border Telehealth Platform responsible for granular patient consent tracking, regulatory compliance (GDPR/HIPAA), and auditable cross-region data access. It runs on Google Kubernetes Engine (GKE) using Spring Boot to provide low-latency policy evaluation, instant revocation, and cryptographic audit logging.

## Key Elements
- Consent REST Controller
- Consent Policy Engine (including Consent Revocation Handler & Break-Glass Protocol)
- Audit & Compliance Logger (including Metadata Enricher)
- Consent Persistence Adapter
- Google Cloud Pub/Sub
- regional PostgreSQL instances
- Redis cache

## Relationships
- Patients and Mobile Clients invoke Consent REST Controller via HTTPS/REST (OAuth2/JWT)
- Core Telehealth communicates with Consent Policy Engine via gRPC with mTLS (Istio service mesh)
- Consent Policy Engine queries regional PostgreSQL instances using JPA/Hibernate
- Consent Policy Engine interacts with local Redis cache via Spring Cache
- Audit & Compliance Logger pushes events to Google Cloud Pub/Sub and BigQuery

## Technology Stack
- Spring Boot & Spring Security: Core application framework and security handling
- Google Kubernetes Engine (GKE): Container orchestration across `europe-west3` and `us-central1`
- Istio Service Mesh: Enforces mTLS and zero-trust networking
- Google Cloud KMS (CMEK): Regional data encryption ensuring residency compliance
- Google Cloud Pub/Sub: Asynchronous event messaging for cache invalidation and audit logging
- Redis: Low-latency local read-through caching for policy evaluation

## Rationale
This architecture ensures strict regional data isolation between the EU and US while delivering high-availability consent evaluations under 300 kbit/s constraints. Cryptographic audit trails and instant revocation mechanisms guarantee full GDPR and HIPAA compliance without compromising emergency patient care.