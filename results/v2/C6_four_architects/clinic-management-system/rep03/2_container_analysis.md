## Overview
The Clinic Management System manages patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized clinics. It operates via a hybrid cloud deployment across on-premises Kubernetes and AWS (eu-central-1) to ensure high availability and compliance.

## Key Elements
- **Users**: Patients, Doctors, Administrators
- **Frontend Container**: Web Frontend (React/TypeScript)
- **Edge Container**: API Gateway (Kong/NGINX)
- **Core Containers**: Core Microservices (Go/Spring Boot), Background Worker (Go/Celery)
- **Integration Containers**: Integration Service (Apache Camel/Node.js), Message Broker (Apache Kafka/RabbitMQ)
- **Data & Caching Containers**: PostgreSQL, Object Storage (MinIO/S3), Caching & Session Container (Redis Enterprise)
- **Security & Ops Containers**: Audit & Compliance Logging (FluentBit/OpenSearch), Backup & Archive Manager (Velero/AWS Backup)
- **External Systems**: Identity Provider, Third-Party Billing Gateway, External Lab/Imaging Systems, Notification Gateway, Cloud Backup Archive

## Relationships
- Users -> **Web Frontend**: HTTPS
- **Web Frontend** -> **API Gateway**: HTTPS/JSON
- **API Gateway** -> **Core Services**: gRPC / Internal mTLS
- **Core Services** -> **PostgreSQL**: TLS
- **Core Services** -> **Caching & Session Container**: Redis Protocol / TLS
- **Core Services** -> **Message Broker**: AMQP / TLS
- **Message Broker** -> **Background Worker**: AMQP / TLS
- **Integration Service** -> **External Lab Systems**: HL7 FHIR over HTTPS
- **All Containers** -> **Audit & Compliance Logging**: Syslog / gRPC
- **Backup & Archive Manager** -> **Cloud Backup Archive**: HTTPS / TLS 1.3

## Technology Stack
- **API Gateway**: Kong or NGINX for TLS termination and OAuth2/OIDC token validation.
- **Frontend**: React and TypeScript served via NGINX.
- **Core Services**: Go and Spring Boot for domain microservices.
- **Data Layer**: PostgreSQL with AES-256 encryption for relational EMR/scheduling data; MinIO/S3 for medical imaging.
- **Caching**: Redis Enterprise in active-active mode for sub-second EMR performance and session management.
- **Messaging**: Apache Kafka or RabbitMQ active-active cluster for async events.
- **Integration**: Apache Camel or Node.js utilizing HL7 FHIR APIs.
- **Observability & Backup**: FluentBit/OpenSearch for audit logging; Velero/AWS Backup for 10-year data retention.

## Rationale
This architecture uses an active-active hybrid design with encrypted PostgreSQL and Redis caching to achieve 99.99% availability and sub-second EMR performance. Centralized audit logging, mTLS, and automated backup management ensure strict adherence to HIPAA and GDPR compliance mandates.