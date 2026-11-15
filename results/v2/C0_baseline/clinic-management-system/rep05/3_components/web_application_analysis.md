## Overview
The Clinic Management System provides patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized healthcare facilities. It utilizes a hybrid cloud architecture designed for high availability, performance, and strict HIPAA/GDPR compliance.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists (Users)
- Identity Provider (IdP)
- NGINX API Gateway / CDN
- Web Application (React SPA)
- Core Services (Spring Boot / Java)
- Data Tier (PostgreSQL with Citus, Redis, Kafka/RabbitMQ)

## Relationships
- Web Application -> NGINX API Gateway: HTTPS / JSON REST via TLS 1.3
- Web Application -> Identity Provider: OIDC with PKCE via HTTPS
- NGINX API Gateway -> Core Services: gRPC over mTLS (Istio service mesh)
- Core Services -> PostgreSQL / Redis: TCP / SQL over TLS

## Technology Stack
- React SPA: Chosen for high-performance client-side rendering and sub-second EMR load times.
- Spring Boot / Java: Chosen for robust enterprise backend integration and strict security controls.
- PostgreSQL with Citus: Chosen for scalable, HIPAA-compliant relational data storage with AES-256 encryption at rest.
- Istio / gRPC: Chosen for secure service-to-service communication with mutual TLS.

## Rationale
This architecture combines a responsive React frontend with a secure, microservices-based backend to meet stringent sub-second performance targets. The hybrid deployment model and strict encryption protocols ensure full compliance with healthcare data regulations while maintaining 99.99% availability.