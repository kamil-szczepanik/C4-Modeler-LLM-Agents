## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized clinics while ensuring HIPAA and GDPR compliance. Its core purpose is to provide highly available, secure clinical operations with a 10-year data retention mandate.

## Key Elements
- **Users**: Patients, Clinicians, Administrative Staff, Billing Officers, Compliance Officers
- **External Systems**: Insurance/Payer Gateways, External Lab/Imaging Systems, Identity Provider (IdP)
- **Containers**: NGINX/Envoy API Gateway, React/React Native Clinical App, Next.js Patient Portal, Node.js/NestJS EMR & Scheduling Service, Java/Spring Boot Billing Service, Apache Camel Interoperability Service, Python/FastAPI Audit Service, Apache Kafka Message Broker
- **Data Tier Components**: Primary Relational DB Cluster (PostgreSQL), Audit & Compliance WORM Store (AWS S3 Object Lock / MinIO), Change Data Capture Component (Debezium), Connection Pooling Component (PgBouncer), Automated PITR & Backup Controller

## Relationships
- **Clinical App to API Gateway**: HTTPS (REST/GraphQL)
- **API Gateway to EMR Service**: gRPC / HTTPS (TLS 1.3)
- **EMR Service to PostgreSQL Cluster**: TCP/SQL via PgBouncer (TLS 1.3)
- **PostgreSQL to Debezium CDC**: TCP (Database Replication Log Stream)
- **Debezium to Apache Kafka**: TCP
- **PostgreSQL / WAL Archiver to WORM Store**: HTTPS (S3 API)
- **Interoperability Service to External Systems**: HL7 FHIR over HTTPS

## Technology Stack
- **PostgreSQL & PgBouncer**: Active-passive synchronous replication with automated fencing for secure, reliable transactional data storage and connection management.
- **AWS S3 Object Lock & MinIO**: WORM Object Storage with AES-256 encryption at rest to guarantee immutable 10-year data retention.
- **Debezium & Apache Kafka**: Real-time change data capture and event streaming to decouple microservices without impacting read/write latencies.
- **Kubernetes (On-Premises & AWS `eu-central-1`)**: Hybrid infrastructure foundation ensuring high availability and container orchestration.

## Rationale
This architecture uses active-passive PostgreSQL replication with strict automated fencing to prevent CAP-theorem data corruption across hybrid boundaries. PgBouncer and Debezium isolate workloads to guarantee sub-second EMR responses and 99.99% uptime while meeting rigorous HIPAA, GDPR, and 10-year retention standards.