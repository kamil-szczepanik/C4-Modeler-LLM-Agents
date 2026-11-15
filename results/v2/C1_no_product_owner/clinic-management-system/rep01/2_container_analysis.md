## Overview
The Clinic Management System is a hybrid cloud clinical IT solution designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals. It ensures 99.99% availability, strict HIPAA/GDPR compliance, and 10-year data retention.

## Key Elements
- Hospital Staff (Users)
- External Systems (Patient Portal, External Lab & Imaging Systems, Insurance Clearinghouses, IdP, Regulatory Audit System)
- API Gateway & Edge Router (Kong/Envoy)
- Web Application Frontend (React SPA, Nginx)
- Core Microservices: Patient Service, Scheduling Service, EMR Service, Billing Service (Spring Boot, Kubernetes)
- Integration Service (Apache Camel/Node.js)
- Data Persistence Layer (PostgreSQL with AES-256 and HSM-managed column encryption)
- Message Broker Container (Geo-local Apache Kafka clusters with MirrorMaker)

## Relationships
- Hospital Staff to Web Application Frontend via HTTPS
- Web Application Frontend to API Gateway via REST/JSON over HTTPS
- API Gateway to Core Microservices via mTLS and service mesh (Istio/Linkerd)
- Core Microservices to Data Persistence Layer via TLS-secured JDBC
- Core Services to Message Broker via TLS/mTLS and SCRAM-SHA-512
- Integration Service to External Lab & Imaging Systems via HL7 FHIR APIs

## Technology Stack
- Kong/Envoy: Edge routing, TLS termination, and mTLS enforcement
- React / Nginx: Frontend delivery for hospital staff
- Spring Boot / Java: Core microservices business logic encapsulation
- PostgreSQL: Multi-region primary and replica data storage with 10-year retention support
- Apache Kafka: Asynchronous event-driven communication via geo-local clusters
- Istio/Linkerd & SPIFFE/SPIRE: Service mesh and zero-trust crypto identity propagation
- OpenTelemetry & WORM Storage: Distributed tracing and immutable audit log retention

## Rationale
This architecture uses a hybrid containerized microservices design to isolate high-load workloads like EMR and achieve sub-second latency. Geo-local Kafka messaging and split services ensure 99.99% active-active availability while meeting strict healthcare compliance and data retention constraints.