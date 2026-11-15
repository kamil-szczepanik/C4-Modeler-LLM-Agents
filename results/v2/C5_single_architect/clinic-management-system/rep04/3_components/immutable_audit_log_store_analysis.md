## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for healthcare clinics. It ensures strict HIPAA and GDPR compliance while maintaining 99.99% high availability and a 10-year data retention policy.

## Key Elements
- **Users:** Patients, Clinical Staff, Administrative Staff, Compliance Officers
- **External Systems:** Lab & Imaging Systems, Payment Gateway & Insurance Clearinghouses
- **Containers:** Nginx / Envoy API Gateway, React / TypeScript Web App, Spring Boot Patient & EMR Service, Node.js / Go Scheduling Service, Spring Boot Billing & Integration Service, Redis Enterprise Cache, Apache Kafka Event Broker, PostgreSQL Primary Database
- **Immutable Audit Log Store Components:** Audit Ingestion API (gRPC), Log Normalizer & Enricher, WORM Storage Engine, Retention Policy Manager, Audit Query Interface, Cryptographic Verifier Component

## Relationships
- Web Application to API Gateway via HTTPS/WSS
- API Gateway to Microservices via gRPC and REST over TLS 1.3
- Microservices to PostgreSQL and Redis via JDBC and RESP
- Microservices to Apache Kafka via TCP/TLS
- Microservices to Lab/Imaging Systems via HL7 FHIR APIs over HTTPS
- Kafka to Audit Ingestion API via TLS 1.3 gRPC

## Technology Stack
- **Frontend:** React / TypeScript for responsive UI (< 1s P95 load time)
- **Backend Services:** Spring Boot and Node.js / Go for scalable domain logic
- **Messaging & Caching:** Apache Kafka for event streaming; Redis Enterprise for distributed caching
- **Database & Storage:** PostgreSQL with AES-256 encryption at rest; S3 Object Lock / MinIO WORM mode for immutable audit logs
- **Protocols:** gRPC (Protocol Buffers over HTTP/2), HTTPS, TLS 1.3, HL7 FHIR

## Rationale
This architecture uses active-active hybrid cloud deployment (on-premise Kubernetes and AWS eu-central-1) to achieve 99.99% availability. WORM storage with cryptographic Merkle tree verification ensures strict HIPAA/GDPR compliance and tamper-proof 10-year data retention.