## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures high availability, strict security compliance, and sub-second performance.

## Key Elements
* **Patient & Clinician/Receptionist**: External users accessing the platform.
* **API Gateway**: Kong / NGINX handling ingress traffic.
* **Patient & Scheduling Service**: Spring Boot (Java) container with Redis.
* **EMR Service**: Spring Boot (Java) with PostgreSQL.
* **Billing & Claims Service**: Node.js container.
* **Integration Service**: Apache Camel / Spring Integration using HL7 FHIR.
* **Audit Service**: Elasticsearch / WORM storage.
* **Redis**: Container providing caching, session state, and scheduling locks via Redis Enterprise / Open Source Redis 7.x, Redis Master/Replica nodes, TLS 1.3 proxy, and client-side encryption middleware.
* **External Systems**: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Notification Service, On-Premise K8s / AWS.

## Relationships
* **Patient & Scheduling Service** -> **Client-Side Encryption/Decryption Middleware**: Passes serialized PII/PHI [In-memory function call].
* **Client-Side Encryption/Decryption Middleware** -> **Redis Master Node**: Stores encrypted key-values [RESP protocol over TLS 1.3].
* **Redis Master Node** -> **Redis Replica Nodes**: Data replication [RESP].
* **Integration Service** -> **External Lab & Imaging Systems**: Data exchange [HL7 FHIR APIs].

## Technology Stack
* **Spring Boot (Java) & Node.js**: Core microservices runtime for business logic.
* **Redis 7.x / Redis Enterprise**: In-memory data store for caching, session state, and locks (R-02, R-07).
* **PostgreSQL**: Primary relational database with AES-256 encryption at rest (R-05).
* **Apache Kafka**: Event streaming for asynchronous service communication.
* **TLS 1.3 & Client-Side Encryption**: Transport and in-memory data protection for HIPAA/GDPR compliance (R-05).
* **Kubernetes (On-Prem K8s & AWS eu-central-1)**: Hybrid infrastructure supporting active-active 99.99% availability (R-06).

## Rationale
This architecture leverages a resilient hybrid Kubernetes deployment with active-active replication to guarantee 99.99% uptime and strict HIPAA/GDPR compliance via end-to-end encryption. Decoupled microservices backed by Redis caching and HL7 FHIR integration ensure sub-second EMR performance and seamless interoperability.