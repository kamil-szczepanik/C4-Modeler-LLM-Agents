## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, appointment scheduling, and billing for healthcare providers while maintaining strict regulatory compliance. It ensures high availability, rigorous data security, and interoperability across clinical workflows.

## Key Elements
- Patients and Clinic Staff (Doctors, Receptionists, Billing Specialists)
- Envoy Proxy API Gateway
- OAuth2-Proxy / Keycloak Sidecar
- EMR & Patient Service (Node.js / Fastify)
- Billing & Claims Service (Java Spring Boot)
- FHIR Interoperability Gateway (HAPI FHIR)
- PostgreSQL (CloudNativePG with AES-256 encryption)
- Apache Kafka message broker
- Redis session cache cluster
- External Enterprise Identity Provider (IdP)

## Relationships
- Patient Portal Interface -> Envoy Proxy API Gateway [HTTPS / TLS 1.3]
- Envoy Proxy API Gateway -> OAuth2-Proxy / Keycloak Sidecar [Internal HTTP / mTLS]
- OAuth2-Proxy Sidecar -> Redis Cache [RESP over TLS 1.3]
- OAuth2-Proxy Sidecar -> Enterprise IdP [HTTPS / TLS 1.3]
- Microservices -> PostgreSQL [PostgreSQL Wire Protocol over TLS 1.3]
- Microservices -> Apache Kafka [TCP / TLS 1.3]
- FHIR Interoperability Gateway -> External Lab & Imaging Systems [HL7 FHIR REST API / TLS 1.3]

## Technology Stack
- Node.js / Fastify: Chosen for high-throughput, low-latency EMR and patient services to meet the <1s P95 load requirement.
- Java Spring Boot: Selected for billing and claims services due to robust enterprise transactional support.
- Go (OAuth2-Proxy): Utilized for lightweight, stateless authentication sidecars to minimize memory footprint and latency.
- PostgreSQL (CloudNativePG): Deployed with AES-256 encryption at rest to satisfy HIPAA and GDPR data protection mandates.
- Apache Kafka: Implemented for asynchronous event streaming across core clinical services.
- Redis: Configured in a high-availability cluster for low-latency active-active session state management.

## Rationale
This architecture combines a secure, stateless proxy pattern with local JWKS caching and encrypted session storage to meet strict HIPAA/GDPR security controls and sub-second performance targets. Deploying across hybrid Kubernetes clusters with active-active replication ensures the required 99.99% uptime and high availability for critical clinical environments.