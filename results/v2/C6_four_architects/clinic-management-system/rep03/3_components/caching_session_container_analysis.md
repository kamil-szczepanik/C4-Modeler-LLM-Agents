## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for clinical environments. It uses a hybrid cloud architecture to deliver high availability and regulatory compliance.

## Key Elements
- **Users**: Patients, Doctors, Administrators
- **External Systems**: Identity Provider, Third-Party Billing Gateway, External Lab/Imaging Systems, Notification Gateway, Cloud Backup Archive
- **Containers**: Web Frontend, API Gateway, Core Microservices, Background Worker, Integration Service, Message Broker, PostgreSQL, Object Storage, Caching & Session Container, Audit & Compliance Logging, Backup & Archive Manager
- **Caching & Session Components**: Session Manager, EMR Cache-Aside, Cluster Coordination, Data Masking & Encryption, Eviction & TTL Policy Manager, Redis Core Storage Engine

## Relationships
- **Core Microservices -> Caching & Session Container**: Queries and updates session and EMR data via RESP / TLS 1.3
- **Caching & Session Container -> Audit & Compliance Logging**: Sends audit logs via Syslog / gRPC
- **Cluster Coordination -> External Redis Enterprise Peers**: Synchronizes CRDT state across hybrid regions via Encrypted TCP / TLS 1.3

## Technology Stack
- **Redis Enterprise**: Provides active-active geo-distribution for high availability.
- **Redis Modules (ReJSON, RedisBloom)**: Enables structured EMR caching and partial document caching.
- **Redis Enterprise Security Module**: Enforces in-memory encryption and AES-256 for HIPAA/GDPR compliance.
- **PostgreSQL**: Stores relational transactional data with AES-256 at rest.
- **React / TypeScript / NGINX**: Powers the Web Frontend container.

## Rationale
This architecture fits the requirements by combining active-active caching with in-memory encryption to guarantee 99.99% availability, sub-second EMR performance, and strict HIPAA/GDPR compliance. Hybrid deployment flexibility bridges on-premises Kubernetes with AWS eu-central-1 seamlessly.