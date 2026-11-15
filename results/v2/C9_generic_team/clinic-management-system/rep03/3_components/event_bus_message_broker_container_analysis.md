## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and 10-year data retention.

## Key Elements
- Patients, Clinicians, and Administrative Staff
- API Gateway Container (Kubernetes Ingress)
- Domain Containers (Kubernetes Microservices)
- Event Bus Container (Apache Kafka)
- Schema Registry & Event Catalog
- Observability Container (Prometheus, Grafana)
- Object Storage Container (WORM support)

## Relationships
- Domain Containers -> Event Bus Container: Publishes/consumes events via [AMQP/Kafka] using TLS and SASL/SCRAM
- Domain Containers -> Object Storage Container: Stores large clinical assets via [HTTPS] using secure reference URIs
- Event Bus Container -> Observability Container: Exposes metrics via [Prometheus Scraping] for consumer lag and health checks

## Technology Stack
- Apache Kafka: Selected for append-only commit log, supporting 10-year auditability and event sourcing.
- Confluent Schema Registry: Enforces backward/forward compatibility and payload schemas.
- Kubernetes: Powers the hybrid deployment across on-premise clusters and AWS (eu-central-1).
- Prometheus & Grafana: Provides real-time observability, consumer lag alerts, and health probes.

## Rationale
This architecture uses an event-driven microservices pattern with Apache Kafka to guarantee high availability (99.99%) and decoupled scalability across hybrid clouds. Strict encryption, schema validation, and audit controls ensure full HIPAA and GDPR compliance.