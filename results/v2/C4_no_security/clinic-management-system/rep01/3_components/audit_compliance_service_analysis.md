## Overview
The Audit & Compliance Service is a component of the Clinic Management System that ensures HIPAA and GDPR compliance through immutable audit logging, policy evaluation, and a 10-year data retention mandate. It operates within a hybrid cloud environment across on-premise Kubernetes and AWS (`eu-central-1`).

## Key Elements
- Compliance Officer and System Administrator (Primary Users)
- Audit Event Ingestion Engine (Spring Boot / Reactive WebFlux)
- Compliance Policy Evaluator (Python / Celery)
- Report Generator & Redactor (Spring Boot)
- Retention Management Worker (Python)
- Apache Kafka (Message Broker)
- PostgreSQL Clusters (Hot Storage, Active-Active)
- Object Storage with S3 Object Lock / WORM (Cold Storage)
- SMS/Email Notification Gateway

## Relationships
- Service Mesh -> Apache Kafka: Streams asynchronous audit events [gRPC over mTLS]
- Audit Event Ingestion Engine -> Apache Kafka: Consumes audit streams [Kafka Protocol over mTLS]
- Audit Event Ingestion Engine -> PostgreSQL Clusters: Appends hot audit log entries [SQL over TLS 1.3 / AES-256]
- Compliance Policy Evaluator -> SMS/Email Notification Gateway: Dispatches real-time security alerts [HTTPS]
- Report Generator & Redactor -> API Gateway: Exposes Compliance Dashboard API [gRPC]
- Report Generator & Redactor -> Object Storage (S3 / WORM): Queries archived immutable logs [HTTPS / S3 API]
- Retention Management Worker -> Object Storage (S3 / WORM): Migrates logs for 10-year retention [HTTPS / S3 API]

## Technology Stack
- Spring Boot / Reactive WebFlux & Python (Component runtimes for high throughput and policy evaluation)
- Apache Kafka (Decoupled event streaming and buffering for high availability)
- PostgreSQL Clusters with AES-256 (Hot storage with 30-day active retention)
- AWS S3 with Object Lock / WORM (Cold-tier storage ensuring tamper-proof 10-year retention)
- OpenTelemetry with W3C Trace Context (Distributed tracing across hybrid boundaries)

## Rationale
This architecture decouples ingestion using Kafka and tier-storage with WORM-enabled S3, satisfying strict 10-year retention and HIPAA/GDPR mandates without degrading hot database performance. The hybrid design and containerized components ensure 99.99% availability and secure audit trails across multi-region deployments.