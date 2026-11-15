## Overview
The Clinic Management System is a hybrid cloud clinical IT platform providing patient registration, EMR, scheduling, and billing. It ensures high availability (99.99%) and HIPAA/GDPR compliance for medium-sized healthcare facilities.

## Key Elements
*   Patients, Receptionists, Attending Physicians, Billing Specialists, Clinic Administrators
*   Identity Provider, Third-Party Payment Gateways, External Lab & Imaging Systems
*   NGINX (Web Application Gateway)
*   Node.js / NestJS (Core API Service)
*   Java / Spring Boot (EMR Engine)
*   Python / Celery (Billing Worker)
*   Sidecar Proxy (Audit Logging Sidecar)
*   PostgreSQL Cluster with AES-256 and LUKS
*   Redis Cluster v7.x with Redis JSON and RediSearch modules
*   Apache Kafka

## Relationships
*   Core API Service -> Redis: Caches data and executes Redlock via `ioredis` [TCP]
*   EMR Engine -> Redis: Caches EMR data and queries indexes via Redis JSON / RediSearch [TCP]
*   Core API Service & EMR Engine -> PostgreSQL Cluster: Persists relational records [TCP, TLS 1.3]
*   Clinic Management System -> External Laboratory & Imaging Systems: Integrates via HL7 FHIR APIs [HTTPS/REST]

## Technology Stack
*   Redis Cluster v7.x: Primary-replica caching and distributed locking for sub-second performance.
*   Redis JSON & RediSearch: In-memory indexing for fast EMR metadata retrieval.
*   Node.js / NestJS: Core API logic and Redlock execution.
*   Java / Spring Boot: High-performance EMR processing.
*   PostgreSQL Cluster: Encrypted relational storage with LUKS.
*   Apache Kafka: Asynchronous event streaming.

## Rationale
This architecture uses Redis caching and in-memory modules to guarantee sub-second EMR load times under high load. Active-active hybrid deployment and strict security controls satisfy 99.99% availability and HIPAA/GDPR compliance mandates.