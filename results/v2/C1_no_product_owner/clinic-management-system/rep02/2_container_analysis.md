## Overview
The Clinic Management System is a hybrid cloud platform designed to securely manage patient records, scheduling, and billing for healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and interoperability with external clinical systems.

## Key Elements
* Patients and Clinicians/Staff (Users)
* External Lab, Imaging Systems, and Payment Gateways/Insurance Clearinghouses (External Systems)
* Envoy (API Gateway / Reverse Proxy)
* Istio (Service Mesh)
* Patient & Scheduling Service (Node.js/Go)
* EMR Core Service (Java/Spring Boot)
* Billing & Integration Service (Python/FastAPI)
* PostgreSQL (Primary Datastore) with Patroni (Active-Passive Failover)
* NATS / RabbitMQ (Edge Brokers) and AWS Kafka (Event Brokers)
* WORM-compliant S3 / MinIO (Object Storage Archive)
* HashiCorp Vault (Secret Management)

## Relationships
* Clients -> API Gateway via HTTPS / JSON
* API Gateway -> Microservices via gRPC over Istio mTLS
* Billing & Integration Service -> External Systems via HTTPS / HL7 FHIR
* Microservices -> Edge/Cloud Event Brokers via TLS 1.3
* Microservices -> PostgreSQL via encrypted SQL connections

## Technology Stack
* Envoy: Chosen for rate limiting, TLS termination, and OAuth2/MFA validation.
* Istio: Selected for zero-trust segmentation and mTLS enforcement.
* PostgreSQL with Patroni: Provides a reliable Active-Passive high availability database topology.
* NATS / RabbitMQ and Apache Kafka: Federated messaging for asynchronous, low-latency cross-boundary integration.
* HashiCorp Vault: Centralized secret management for dynamic token generation.

## Rationale
This architecture uses an active-passive hybrid topology and federated messaging to prevent multi-master split-brain risks and WAN latency. Security controls like Istio mTLS, AES-256 encryption, and HashiCorp Vault ensure strict HIPAA and GDPR compliance without compromising 99.99% availability.