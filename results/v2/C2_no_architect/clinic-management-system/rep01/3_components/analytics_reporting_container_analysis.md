## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing while ensuring HIPAA and GDPR compliance with 99.99% uptime. It utilizes an asynchronous analytics container to process operational metrics and compliance reports securely.

## Key Elements
- Hospital Administrators and Compliance Officers (Users)
- Analytics & Reporting Container (Microservice)
- Event Broker (Apache Kafka / RabbitMQ)
- OLAP Read-Replica / Columnar Store (Data Warehouse)
- Immutable Audit Storage Sink (Secure Storage)
- HashiCorp Vault (Secrets Management)

## Relationships
- API Gateway -> Analytics & Reporting Container [HTTPS, mTLS via SPIFFE/SPIRE]
- Analytics & Reporting Container -> Event Broker [TLS 1.3]
- Analytics & Reporting Container -> OLAP Store [Encrypted JDBC/ODBC]
- Analytics & Reporting Container -> Immutable Audit Storage Sink [Secure Storage API]

## Technology Stack
- Kubernetes & HPA: Isolated container node pools with consumer-lag-driven autoscaling for workload management
- OpenTelemetry & Prometheus: Distributed tracing and metrics for ingestion lag and SLA monitoring
- HashiCorp Vault: AES-256 encryption at rest and secret management for the OLAP store
- Kafka / RabbitMQ: Asynchronous stream processing for event-driven data ingestion

## Rationale
This architecture decouples heavy analytical workloads from core transactional databases to preserve 99.99% EMR and billing availability. It enforces strict data minimization, dynamic masking, and auditability to meet HIPAA and GDPR compliance mandates.