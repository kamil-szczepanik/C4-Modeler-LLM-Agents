## Overview
The Clinic Management System is a clinical IT solution designed to handle patient admissions, EMRs, scheduling, and billing. It ensures secure, high-availability operations for medium-sized healthcare providers.

## Key Elements
- Spring Boot Core Services (Spring Boot, Java)
- Internal Components: Patient Management, Scheduling Engine, EMR Core, Billing & Claims, Security/Masking Interceptor, Event-Driven Audit Component, Data-Access Encryption Interceptor
- PostgreSQL (Primary & Read-Replica)
- Redis (Cache & Distributed Locking)
- HashiCorp Vault (Secrets & Key Management)
- Istio Service Mesh & Kong API Gateway

## Relationships
- Istio Service Mesh -> Spring Boot Core Services: Routes secured traffic [gRPC/HTTP]
- Spring Boot Core Services -> PostgreSQL: Persists transactional data [JDBC]
- Spring Boot Core Services -> Redis: Manages locks and sessions [TCP]
- Spring Boot Core Services -> HashiCorp Vault: Retrieves secrets and encryption keys [HTTPS]

## Technology Stack
- Spring Boot & Spring MVC: Core business logic and web controllers for low-latency request handling
- Spring Data JPA & Hibernate: Transactional persistence with custom JPA `AttributeConverter` for encryption
- Spring Cloud Vault: Secret retrieval and local AES key caching with secure rotation TTL
- Redis: High-performance distributed locking for appointment scheduling
- PostgreSQL: ACID-compliant relational data storage

## Rationale
This architecture uses Spring Boot components combined with asynchronous event processing and local key caching to meet sub-second EMR latency requirements. It implements stringent security and encryption protocols to ensure HIPAA and GDPR compliance without compromising high availability.