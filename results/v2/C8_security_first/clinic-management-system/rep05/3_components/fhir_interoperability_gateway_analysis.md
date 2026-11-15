## Overview
- The system is the Clinic Management System designed to handle patient records, scheduling, billing, and clinical interoperability.
- Its core purpose is providing secure, high-availability healthcare IT infrastructure for medium-sized hospitals and clinics.

## Key Elements
- Patients / Consumers
- Clinic Staff / Receptionists
- Clinicians / Doctors
- Billing Specialists / Administrators
- Envoy Proxy API Gateway
- OAuth2-Proxy / Keycloak
- EMR & Patient Service (Node.js / Fastify)
- Billing & Claims Service (Java Spring Boot)
- FHIR Interoperability Gateway (HAPI FHIR JPA Server)
- PostgreSQL (CloudNativePG with AES-256)
- Apache Kafka
- Redis

## Relationships
- External Lab & Imaging Systems -> FHIR Interoperability Gateway: Data exchange [mTLS, HL7 FHIR APIs over HTTPS]
- FHIR Interoperability Gateway -> Apache Kafka: Event publishing [Kafka Producer API, TCP/SASL_SSL]
- FHIR Interoperability Gateway -> PostgreSQL: Data persistence [JDBC over TLS, HikariCP]
- FHIR Interoperability Gateway -> Redis: Token caching and session state [Redis Protocol]

## Technology Stack
- Java / Spring Boot: Core runtime for FHIR Interoperability Gateway and HAPI FHIR JPA Server for standards-compliant clinical endpoints.
- Apache Kafka: Asynchronous event streaming for decoupled service communication and audit publishing.
- PostgreSQL (CloudNativePG): Relational data store providing AES-256 encryption at rest for strict data retention.
- Redis: In-memory store for distributed token caching, consent policies, and session management.
- Envoy Proxy: Ingress/egress load balancing and mTLS termination for secure external connectivity.

## Rationale
- The hybrid cloud architecture with active-active Kubernetes clusters ensures 99.99% high availability and fault tolerance.
- Layered security controls—including mTLS, SMART on FHIR, and AES-256—guarantee full HIPAA and GDPR compliance.