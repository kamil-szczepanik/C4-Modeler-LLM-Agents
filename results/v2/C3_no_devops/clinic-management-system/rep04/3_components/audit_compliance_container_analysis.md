## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing securely. It ensures high availability (99.99%), strict regulatory compliance (HIPAA/GDPR), and long-term data retention (≥ 10 years).

## Key Elements
- **Users**: Patient, Clinic Staff/Receptionist, Clinician/Doctor, Billing Specialist, System Administrator, Compliance Officer / Data Protection Officer (DPO).
- **External Systems**: Lab & Imaging Systems, Insurance Clearinghouses, Identity Provider (IdP), Payment Gateway.
- **Containers**: Frontend Container, API Gateway, Core Services Container, EMR Service Container, Integration Service Container, Notification Container, Audit & Compliance Container, PostgreSQL Database, ClickHouse Database, Apache Kafka.
- **Audit & Compliance Components**: Audit Ingestion Component, Compliance Storage & Indexing Component, Audit Query & Reporting API Component, Retention & Archival Manager Component.

## Relationships
- *Core Services / EMR / Integration / Notification Containers* -> *Audit & Compliance Container*: Streams audit events [Apache Kafka, TLS + SASL]
- *Audit Ingestion Component* -> *Compliance Storage Component*: Persists streaming logs [ClickHouse Native Protocol, mTLS]
- *Audit Query & Reporting API Component* -> *Compliance Storage Component*: Executes analytical queries [SQL, mTLS]
- *Retention & Archival Manager* -> *Compliance Storage Component*: Manages partition rotation [SQL/Admin API]
- *Retention & Archival Manager* -> *Object Storage (Cold)*: Archives aged logs with SHA-256 hashes [HTTPS/S3 API, AES-256]

## Technology Stack
- **Frontend**: React, TypeScript, CDN, Nginx for responsive client delivery.
- **API Gateway**: Kong / Envoy with Istio Service Mesh for routing and mTLS.
- **Backend Services**: Go, Spring Boot, Node.js for high-performance microservices.
- **Event Bus**: Apache Kafka with TLS + SASL for asynchronous, reliable event streaming.
- **Databases**: PostgreSQL (AES-256) for transactional data; ClickHouse for high-throughput, searchable audit logs.
- **Storage & Compliance**: MinIO / S3 with WORM compliance mode and customer-managed AES-256 encryption for cold archival.

## Rationale
The hybrid architecture utilizes on-premise Kubernetes and AWS (eu-central-1) to balance local data residency needs with scalable cloud resources. ClickHouse and WORM-enabled S3 storage directly satisfy the strict 10-year audit retention and HIPAA/GDPR immutability requirements without impacting clinical performance.