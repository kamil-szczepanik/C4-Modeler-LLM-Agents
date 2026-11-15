## Overview
The Clinic Management System is an enterprise healthcare platform that securely manages patient admissions, electronic medical records, appointments, and billing. It provides high availability, stringent compliance, and seamless interoperability for medium-sized clinics and hospitals.

## Key Elements
- Patients, Clinicians, Receptionists, Billing Specialists, and Compliance Auditors
- NGINX/Kong API Gateway
- EMR, Appointment, and Billing Containers
- Audit & Compliance Container
- HL7 FHIR Interoperability Service
- Apache Kafka (Brokers, KRaft Quorum, Schema Registry, Kafka Connect Sink)
- PostgreSQL with Redis caching
- External IDP, Payment Gateways, and Lab/Imaging Systems

## Relationships
- Users access system via HTTPS/REST/gRPC through NGINX/Kong API Gateway
- EMR Service publishes events to Apache Kafka via TLS 1.3 (Kafka protocol)
- Kafka Brokers stream data to Schema Registry (Avro/Protobuf)
- Kafka Connect Sink streams encrypted data to S3/MinIO Object Storage via HTTPS
- HL7 FHIR Service connects to external Lab and Imaging Systems via HL7 FHIR APIs

## Technology Stack
- Node.js / Go: Powers microservice containers for high performance and low P95 latency
- Python / FastAPI: Implements HL7 FHIR Interoperability Service for rapid healthcare standard integration
- Apache Kafka & KRaft: Event streaming bus and metadata management ensuring 99.99% uptime
- PostgreSQL & Redis: Primary data persistence and caching layer with AES-256 envelope encryption
- Prometheus & Grafana: Infrastructure and business SLA monitoring via JMX Exporter

## Rationale
This hybrid cloud architecture guarantees 99.99% uptime and low latency through decoupled Kafka event streaming and active-active clustering. It strictly enforces HIPAA and GDPR compliance via mTLS, per-patient envelope encryption, and immutable cryptographic erasure.