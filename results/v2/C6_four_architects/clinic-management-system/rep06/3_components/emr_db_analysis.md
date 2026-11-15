## Overview
The Clinic Management System is a hybrid cloud platform designed to streamline patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict regulatory compliance, and seamless interoperability.

## Key Elements
- Frontend Web App (React SPA)
- API Gateway (Nginx / Kong)
- Identity & Access Proxy (OAuth2 Proxy / Keycloak Sidecar)
- Patient & Scheduling Service (Java / Spring Boot)
- EMR Service (Node.js / TypeScript)
- Billing & Claims Service (.NET Core)
- FHIR Integration Broker (Apache Camel / Python)
- Async Message Broker (Apache Kafka / RabbitMQ)
- Audit & Compliance Log Shipper (Fluentbit / Vector)
- Patient DB (PostgreSQL)
- EMR DB (MongoDB with WiredTiger engine, 3-node Replica Sets, Change Streams, Backup & PITR Agent, Encryption Key Management Module, and Query Access Control Subsystem)
- Distributed Cache (Redis)
- Audit Data Store (AWS S3 / MinIO WORM)
- External Systems: Identity Provider (IdP), External Labs & Imaging Systems, Insurance Payment Gateway, Hospital Notification/SMS Gateway

## Relationships
- EMR Service -> EMR DB: Reads and writes EMR payloads [TLS-encrypted NoSQL driver]
- EMR DB -> Audit & Compliance Log Shipper: Streams oplog data for immutable audit trails [Internal DB Oplog tailing / TLS]
- EMR DB -> Distributed Cache (Redis): Caches frequent patient EMR lookup segments [TCP / Redis wire protocol via TLS]
- EMR DB -> Audit Data Store (AWS S3 / MinIO WORM): Streams encrypted database backups and PITR logs [HTTPS / S3 API over TLS]
- EMR DB -> Identity Provider (IdP) / KMS: Fetches data encryption keys (DEKs) using envelope encryption [KMIP over TLS]
- EMR DB -> Identity & Access Proxy: Validates incoming connection tokens and context [TLS / SCRAM-SHA-256]

## Technology Stack
- MongoDB with WiredTiger: Chosen for flexible schema EMR storage and native AES-256 encryption at rest.
- Kubernetes Operators: Deployed for automated failover across multi-availability zones to ensure 99.99% uptime.
- Redis: Implemented for caching frequent patient EMR lookup segments to meet sub-second performance.
- AWS S3 / MinIO WORM: Utilized for immutable long-term storage meeting the 10-year data retention mandate.

## Rationale
This architecture uses a secure, resilient hybrid cloud deployment to meet strict HIPAA, GDPR, and 99.99% availability mandates. It leverages high-performance components and robust encryption to ensure low-latency clinical operations and long-term data integrity.