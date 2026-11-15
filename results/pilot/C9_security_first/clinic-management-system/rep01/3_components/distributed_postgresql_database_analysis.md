## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It utilizes a hybrid cloud architecture to ensure high availability and HIPAA/GDPR compliance.

## Key Elements
* Patients, Receptionists, Clinicians, Billing Specialists
* React SPA Frontend
* NGINX / Kong API Gateway
* Patient Service, Scheduling Service, EMR Service, Billing Service (Java, Spring Boot, gRPC)
* Apache Camel Integration Service
* Distributed PostgreSQL Database (PostgreSQL with Citus, Patroni, pgAudit, and AES-256 encryption)
* Apache Kafka Event Broker
* Third-Party Lab & Imaging Systems, Payment Gateways, Insurance Clearinghouses

## Relationships
* React SPA Frontend -> NGINX/Kong API Gateway: HTTPS/REST and gRPC
* Microservices -> Apache Kafka Event Broker: SASL/SCRAM over TLS 1.3
* Microservices -> Distributed PostgreSQL Database: SQL over TLS 1.3 via connection pooling
* Apache Camel -> Third-Party Lab & Imaging Systems: HL7 FHIR APIs
* Distributed PostgreSQL Database -> Distributed PostgreSQL Database: Streaming replication with WAL shipping over mTLS

## Technology Stack
* React SPA / NGINX / Kong: Frontend rendering and API routing for high performance
* Java & Spring Boot: Microservices framework for enterprise reliability
* gRPC & Apache Kafka: Inter-service communication and event streaming
* PostgreSQL, Citus, Patroni: Distributed database sharding and active-active high availability
* AES-256 & mTLS: Data encryption at rest and in transit for HIPAA/GDPR compliance

## Rationale
The hybrid architecture distributes workloads across on-premise Kubernetes and AWS eu-central-1 to satisfy strict 99.99% availability requirements. Encrypted distributed storage with automated failover protects sensitive patient data while supporting long-term compliance mandates.