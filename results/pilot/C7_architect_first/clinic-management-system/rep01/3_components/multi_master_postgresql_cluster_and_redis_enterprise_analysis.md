## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It utilizes a hybrid cloud architecture to ensure high availability, security, and strict regulatory compliance.

## Key Elements
- Patients, Clinicians, and Billing Staff (Users)
- External Payment Gateways, Insurance Clearinghouse, Third-Party Lab/Imaging Systems, IdP, External Notification Service (External Systems)
- Next.js Single Page Application (Next.js / CDN)
- Go API Gateway (Go)
- Java Spring Boot Microservices (Java Spring Boot)
- Apache Camel K Integration Broker (Apache Camel K)
- Apache Kafka (Apache Kafka)
- Multi-master PostgreSQL Cluster and Redis Enterprise (PostgreSQL, Redis, AES-256)

## Relationships
- Patients & Clinicians -> Next.js SPA via HTTPS/TLS 1.3
- Next.js SPA -> Go API Gateway via HTTPS/REST/GraphQL
- Go API Gateway -> Java Spring Boot Microservices via gRPC / mTLS
- Java Spring Boot Microservices -> Multi-master PostgreSQL Cluster via PostgreSQL Wire Protocol (TCP, gRPC)
- Java Spring Boot Microservices -> Redis Enterprise Cluster Proxy via RESP/RESP3
- Apache Camel K -> Lab & Imaging Systems via HL7 FHIR APIs

## Technology Stack
- Next.js / CDN: Frontend presentation layer for fast UI rendering
- Go: High-performance routing at the API gateway layer
- Java Spring Boot: Microservices framework for robust business logic
- Apache Kafka: Event streaming backbone for asynchronous messaging
- PostgreSQL & Redis Enterprise: Active-active multi-master data tier with CRDTs for low-latency persistence and scheduling locks

## Rationale
This architecture uses active-active multi-master replication and an odd-node consensus model to achieve 99.99% availability and eliminate split-brain risks across hybrid regions. AES-256 encryption, mTLS, row-level security, and audit logging satisfy stringent HIPAA and GDPR compliance mandates.