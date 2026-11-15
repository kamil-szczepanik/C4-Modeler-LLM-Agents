## Overview
The Clinic Management System is a hybrid, highly available clinical IT platform managing patient admissions, EMRs, scheduling, and billing for medium-sized clinics. It ensures strict HIPAA and GDPR compliance while supporting 99.99% uptime and high-throughput interoperability.

## Key Elements
* Patients, Clinicians, and Billing Staff (Users)
* Next.js Single Page Application (Frontend Container)
* Go API Gateway (Routing and Rate Limiting Container)
* Java Spring Boot Microservices: Patient, Scheduling, EMR, Billing
* Apache Camel K Integration Broker (HL7 FHIR Interoperability)
* Apache Kafka (Event Stream and Immutable Audit Log Container)
* Multi-master PostgreSQL Cluster and Redis Enterprise (Persistence and Caching Containers)
* External Payment Gateways, Insurance Clearinghouses, and Lab/Imaging Systems

## Relationships
* Users to Next.js SPA via HTTPS/JSON
* Next.js SPA to Go API Gateway via HTTPS/JSON
* Go API Gateway to Java Microservices via gRPC with mTLS
* Java Microservices to PostgreSQL and Redis via gRPC and SQL protocols
* Java Microservices to Apache Kafka via TCP/TLS
* Apache Camel K Broker to External Lab Systems via HL7 FHIR over HTTPS

## Technology Stack
* Next.js / CDN: Delivers sub-second P95 frontend screen loads
* Go: Powers the API Gateway for high-performance request routing
* Java Spring Boot: Handles robust enterprise transactions for EMR and Billing
* Apache Camel K: Manages isolated HL7 FHIR integrations
* Apache Kafka: Provides immutable event streaming for 10-year audit retention
* PostgreSQL & Redis Enterprise: Ensures multi-master active-active persistence and low-latency scheduling checks with AES-256 encryption
* Kubernetes: Orchestrates hybrid workloads across on-prem and AWS `eu-central-1`

## Rationale
This architecture achieves 99.99% uptime and low-latency performance using active-active geo-replication, gRPC, and Redis caching. Containerized microservices, Kafka audit logs, and strict mTLS trust boundaries guarantee HIPAA/GDPR compliance and secure interoperability.