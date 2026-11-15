## Overview
The Clinic Management System manages patient records, scheduling, and billing for medium-sized healthcare facilities. It utilizes a hybrid cloud architecture designed for HIPAA/GDPR compliance, high availability (99.99%), and a strict 10-year data retention mandate.

## Key Elements
- Patients, Clinicians, and Administrative Staff
- External Identity Providers (IdPs) and Third-Party Billing Gateways
- HL7 FHIR-Compliant Lab and Imaging Systems
- API Gateway Container (Kubernetes Ingress / Custom Proxy)
- Domain Containers (Microservices / Kubernetes)
- Integration Service Container (Asynchronous Worker)
- Event Bus / Message Broker Container (Apache Kafka or RabbitMQ)
- Caching Container (Redis Enterprise)
- File/Document Storage Container (Object Storage with WORM support)
- Data Archival & Purging Container (Background Worker)
- Observability & Configuration Container (Prometheus, Fluentbit, Secret Manager)

## Relationships
- Patients and Staff interact with the API Gateway Container via HTTPS (TLS 1.3, Multi-Factor Authentication).
- API Gateway Container routes traffic to Domain Containers using gRPC and REST.
- Domain Containers persist and retrieve operational data from Caching Container and primary transactional database via SQL.
- Integration Service Container communicates with external HL7 FHIR-Compliant Lab/Imaging Systems using HL7 FHIR APIs over HTTPS.
- Integration Service Container exchanges events with Event Bus / Message Broker Container using AMQP/Kafka protocols.
- Data Archival & Purging Container extracts historical data from primary databases, validates via SHA-256 checksums, and transfers it to File/Document Storage Container with WORM support.
- Observability & Configuration Container scrapes metrics from all containers using Prometheus protocols and collects logs via Fluentbit.

## Technology Stack
- Kubernetes (on-prem-k8s and AWS eu-central-1): Ensures active-active high availability (99.99%).
- Apache Kafka / RabbitMQ: Powers asynchronous event-driven messaging and idempotent job queues.
- Redis Enterprise: Provides low-latency caching to achieve EMR screen loads < 1 s P95.
- Object Storage with WORM support: Guarantees immutable 10-year data retention for HIPAA/GDPR compliance.
- Prometheus and Fluentbit: Delivers observability, structured metrics, and audit logging.

## Rationale
The hybrid Kubernetes architecture ensures active-active high availability and satisfies strict performance SLAs under 1 second. Decoupling storage tiers, utilizing asynchronous workers with rate limiting, and enforcing WORM-compliant archival protect system resources and guarantee regulatory compliance.