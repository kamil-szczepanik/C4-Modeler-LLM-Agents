## Overview
- The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers.
- It delivers high availability and HIPAA/GDPR compliance across hybrid on-prem Kubernetes and AWS eu-central-1 infrastructure.

## Key Elements
- Patients, Clinicians, and Billing Staff (Users)
- Next.js Single Page Application & Go API Gateway
- Java Spring Boot Microservices (`PatientService`, `SchedulingService`, `EMRService`, `BillingService`, `AuditService`)
- Apache Camel K Integration Broker & Apache Kafka
- Multi-master PostgreSQL Cluster & Redis Enterprise

## Relationships
- Go API Gateway -> Java Spring Boot Microservices: Routes requests via gRPC with mTLS
- Java Spring Boot Microservices -> PostgreSQL & Redis: Persists and caches data via gRPC and SQL protocols over TLS
- Java Spring Boot Microservices -> Apache Kafka: Streams audit events and Saga messages via TCP/TLS
- Java Spring Boot Microservices -> External Payment Gateways & Insurance Clearinghouses: Processes financial transactions via HTTPS
- EMRService -> External Lab and Imaging Systems: Interoperates using HL7 FHIR APIs over HTTPS

## Technology Stack
- Spring Boot 3.2: Powers core domain microservices with Spring Data JPA and Spring Cloud OpenFeign
- Redis Enterprise: Provides low-latency EMR caching via Lettuce to meet sub-second P95 performance targets
- Apache Kafka: Handles event streaming and distributed Saga orchestration
- HAPI FHIR Spring Boot Starter: Enables standardized clinical interoperability
- Google Tink & Hibernate: Enforces AES-256 encryption and dynamic row-level security

## Rationale
- Microservices combined with Spring Security and mTLS ensure strict HIPAA/GDPR compliance and robust data isolation.
- Active-active deployment on hybrid Kubernetes clusters with Redis caching delivers 99.99% uptime and sub-second EMR retrieval.