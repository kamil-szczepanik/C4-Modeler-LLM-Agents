## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to manage patient registration, EMR, scheduling, and billing while ensuring HIPAA and GDPR compliance with 99.99% availability. It utilizes an event-driven architecture powered by a secured asynchronous event bus to decouple core domain services.

## Key Elements
- Asynchronous Event Bus (Kafka/RabbitMQ) with centralized Schema Registry
- Core Domain Containers (Billing, EMR, Scheduling) deployed on Kubernetes
- Dead Letter Queues (DLQ) and Redis Distributed Rate Limiting Store
- Secure Object Storage for large clinical payloads
- OpenTelemetry Observability Container and Prometheus Monitoring

## Relationships
- Core Domain Containers -> Asynchronous Event Bus: Publish and consume domain events [AMQP/Kafka with TLS and Envelope Encryption]
- Core Domain Containers -> Secure Object Storage: Offload large clinical payloads via URIs [HTTPS]
- Asynchronous Event Bus -> Dead Letter Queues (DLQ): Route malformed or failed messages [AMQP/Kafka]
- Observability Container -> Asynchronous Event Bus: Scrape consumer lag and throughput metrics [Prometheus]

## Technology Stack
- Kafka/RabbitMQ: Chosen as the message broker for asynchronous, decoupled event-driven workflows and high availability.
- Avro / JSON Schema Registry: Enforces strict backward and forward compatibility to prevent schema drift across services.
- OpenTelemetry: Propagates distributed trace contexts (`traceparent`) for end-to-end debugging across services.
- Prometheus: Tracks consumer lag, throughput, and queue depth to maintain uptime targets.

## Rationale
This architecture ensures strict regulatory compliance, data integrity, and high availability for sensitive medical workflows. Decoupling services via an event bus with strict schema governance, envelope encryption, and idempotency prevents cascading failures while meeting performance SLAs.