## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals for academic and public libraries. It uses an event-driven microservices architecture hosted in the EU to ensure strict data residency and high performance.

## Key Elements
- Patron Web App & Staff Portal (TypeScript/React SPAs)
- API Gateway (Nginx / Spring Cloud Gateway)
- Catalog & Search Service (Java/Spring Boot + Elasticsearch)
- Circulation Service (Java/Spring Boot + PostgreSQL)
- Notification & Integration Worker (Node.js/Python)
- Internal Event Bus (Apache Kafka)
- Schema Registry (Confluent Schema Registry with Avro/JSON Schema)
- Dead Letter Queue (DLQ) Topics (Apache Kafka Topics)
- EU-hosted Log & Metrics Aggregator
- Managed Kubernetes Cluster (EKS/AKS in `eu-central-1`)

## Relationships
- Circulation Service -> Internal Event Bus: Publishes circulation events [Apache Kafka Protocol]
- Internal Event Bus -> Notification & Integration Worker: Consumes events for notification processing [Apache Kafka Protocol]
- Catalog & Search Service -> Internal Event Bus: Publishes item state change events [Apache Kafka Topics]
- Circulation Service -> Schema Registry: Validates event payloads prior to publishing [HTTP/REST over TLS]
- Internal Event Bus -> Dead Letter Queue Topics: Routes failed messages after max retry attempts [Apache Kafka Protocol]
- Internal Event Bus -> EU-hosted Log & Metrics Aggregator: Forwards audit logs and metrics [Syslog/OTLP over TLS]

## Technology Stack
- Apache Kafka: Provides durable, append-only commit logs for at-least-once delivery and zero-blocking resilience during outages.
- Confluent Schema Registry: Enforces strict payload contracts via Avro/JSON Schema to prevent breaking changes.
- PostgreSQL & Elasticsearch: Persistent data storage and high-performance search (<800ms response).
- Managed Kubernetes: Ensures scalability and adheres to EU-only data residency constraints in `eu-central-1`.

## Rationale
This architecture decouples core services using an asynchronous event bus to guarantee system reliability and prevent downstream outages from blocking patron workflows. Managed EU infrastructure and strict schema governance ensure data residency compliance, transactional integrity, and rapid search performance.