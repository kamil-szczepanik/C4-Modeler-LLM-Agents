## Overview
The Clinic Management System is an enterprise clinical IT platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high-availability, HIPAA- and GDPR-compliant services for medium-sized hospitals and clinics.

## Key Elements
- Patients, Clinic Staff, Clinicians, Billing Specialists (Users)
- Envoy Proxy API Gateway (Ingress & Routing Container)
- OAuth2-Proxy / Keycloak Sidecar (Authentication)
- EMR & Patient Service (Node.js / Fastify)
- Billing & Claims Service (Java Spring Boot)
- FHIR Interoperability Gateway (HAPI FHIR)
- PostgreSQL with CloudNativePG & AES-256 (Database)
- Apache Kafka (Messaging)

## Relationships
- Patients / Staff / Clinicians / Billing Specialists -> Envoy Proxy API Gateway: Secure access and management [HTTPS / TLS 1.3]
- Envoy Proxy API Gateway -> OAuth2-Proxy / Keycloak Sidecar: Internal token validation [Internal HTTP / mTLS]
- Envoy Proxy API Gateway -> EMR, Billing, and FHIR Services: Upstream microservice routing [Internal mTLS]
- External Lab, Imaging Systems, and Clearinghouses -> FHIR Interoperability Gateway: Data exchange [HL7 FHIR APIs]

## Technology Stack
- Envoy Proxy: Edge routing, rate limiting, and TLS 1.3 termination for high performance and security
- OAuth2-Proxy / Keycloak: Zero-trust token inspection and identity management
- Node.js / Fastify & Java Spring Boot: High-throughput microservice implementation for EMR and billing
- HAPI FHIR: Standards-based interoperability for lab and imaging integration
- PostgreSQL (CloudNativePG): Encrypted relational storage meeting 10-year data retention rules
- Apache Kafka: Event streaming for reliable asynchronous messaging

## Rationale
This hybrid architecture uses an active-active Envoy Proxy gateway combined with rigorous mTLS, AES-256 encryption, and strict audit logging to guarantee HIPAA/GDPR compliance. The containerized microservices and Kubernetes deployment model achieve the required 99.99% uptime and sub-second EMR response times.