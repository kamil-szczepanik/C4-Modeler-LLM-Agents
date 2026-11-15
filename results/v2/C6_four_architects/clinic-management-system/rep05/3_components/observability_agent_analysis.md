## Overview
[The Clinic Management System manages patient admissions, medical records, scheduling, and billing for clinical environments. It uses a hybrid cloud infrastructure to ensure HIPAA and GDPR compliance with 99.99% availability.]

## Key Elements
* Patient and Clinician/Staff (Primary Users)
* Billing Administrator (Administrative User)
* API Gateway (Nginx / Kong)
* Patient & Scheduling Service (Java / Spring Boot)
* EMR Service (Java / Spring Boot)
* Billing Service (Node.js / TypeScript)
* FHIR Interoperability Service (Python / FastAPI)
* Background Worker (Python / Celery)
* Keycloak Container (Docker / Keycloak)
* Observability Agent (Prometheus / Grafana Promtail / OpenTelemetry Collector)
* Distributed Cache (Redis Enterprise)
* Message Broker (Apache Kafka)
* Primary Database (PostgreSQL)
* Database Access Proxy (PgBouncer)
* Audit & Archival Store (AWS S3 / On-Prem Object Storage)
* Internal Service Mesh (Istio / Envoy)

## Relationships
* Users to API Gateway (HTTPS / TLS 1.3)
* API Gateway to Internal Microservices (gRPC / mTLS via Istio Service Mesh)
* Microservices to Primary Database via PgBouncer (TCP / PostgreSQL Wire Protocol)
* FHIR Interoperability Service to External Lab & Imaging Systems (HL7 FHIR REST APIs)
* Services to Message Broker (TCP / Kafka Protocol)
* Services to Distributed Cache (TCP / Redis Protocol)
* Observability Agent to Central Observability Cluster (gRPC over TLS)

## Technology Stack
* Kubernetes (Container orchestration on-prem and in AWS eu-central-1)
* Java Spring Boot and Python FastAPI (Core backend services for high-performance EMR and FHIR processing)
* PostgreSQL with AES-256 Encryption at Rest (Primary data persistence)
* Apache Kafka (Event-driven messaging backbone)
* Keycloak (Identity and Access Management with MFA support)
* OpenTelemetry and Prometheus (Observability and tracing)

## Rationale
[This hybrid cloud architecture leverages containerization and active-active replication to meet the stringent 99.99% uptime requirement. Microservices and strict encryption-at-rest ensure HIPAA and GDPR compliance while maintaining high-performance clinical operations.]