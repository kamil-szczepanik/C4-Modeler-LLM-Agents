## Overview
The Clinic Management System is a hybrid-cloud healthcare platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability and strict compliance with HIPAA and GDPR regulations.

## Key Elements
- React SPA (React)
- Node.js Mobile BFF (Node.js / Express)
- API Gateway (Nginx / Kong)
- Service Mesh (Istio / Linkerd)
- Clinical Services (Java / Spring Boot)
- Billing Services (Python / FastAPI)
- HAPI FHIR Interoperability (Java)
- Notification Worker (Go)
- Compliance Worker (Python / Celery) with internal Audit Log Ingestion, Retention Policy Engine, Tiered Storage Archiver, and Report Generation Sub-components
- PostgreSQL with AES-256 encryption
- Apache Kafka
- S3-compatible Tiered Storage with WORM (Object Lock)

## Relationships
- React SPA and Node.js Mobile BFF communicate with API Gateway via HTTPS / REST / GraphQL
- API Gateway routes internal microservice traffic via gRPC over Istio Service Mesh
- Compliance Worker consumes audit logs from Apache Kafka via Kafka Protocol
- Tiered Storage Archiver writes archives to Tiered Storage via HTTPS / S3 API with WORM headers
- Clinical and Billing Services read and write encrypted data to PostgreSQL via TCP

## Technology Stack
- React & Node.js: Frontend and mobile BFF for responsive client access
- Java Spring Boot & Python FastAPI: Microservices backend chosen for performance and rapid development of clinical and billing domains
- Apache Kafka: Event streaming backbone ensuring decoupled, reliable message processing
- PostgreSQL: Relational database with AES-256 encryption at rest for patient records
- Python Celery: Asynchronous task queue powering background compliance and retention jobs
- S3-compatible Tiered Storage: Long-term storage utilizing Object Lock for immutable data retention

## Rationale
This architecture ensures 99.99% high availability through an active-active hybrid setup while maintaining sub-second EMR screen loads. Strict data governance, encryption, and WORM-compliant tiered storage satisfy mandatory 10-year retention policies and HIPAA/GDPR compliance.