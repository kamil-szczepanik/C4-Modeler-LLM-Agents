## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It guarantees sub-800ms search responses and strict EU data residency.

## Key Elements
- Library Patrons, Librarians, Circulation Staff
- Patron Web App & Staff Portal (TypeScript/React SPAs)
- API Gateway (Spring Cloud Gateway)
- Catalog & Search Service (Java/Spring Boot)
- Catalog Ingestion Worker (Node.js/Python/Spring Batch)
- Elasticsearch, PostgreSQL
- Internal Event Bus (Apache Kafka)
- Managed Kubernetes Cluster (EKS/AKS EU-central)

## Relationships
- API Gateway -> Catalog & Search Service [gRPC]
- Catalog & Search Service -> Elasticsearch [Elasticsearch REST Client]
- Catalog Ingestion Worker -> Internal Event Bus [AMQP/Kafka]
- Internal Event Bus -> Catalog & Search Service [AMQP/Kafka]
- Catalog & Search Service -> Digital Content Providers [HTTPS/REST]

## Technology Stack
- Java/Spring Boot: High-performance backend runtime for sub-800ms search requirement (R-05)
- Elasticsearch: Core indexing engine supporting fuzzy matching, typo tolerance, and faceted search
- Apache Kafka: Asynchronous event bus decoupling catalog ingestion and real-time availability projections
- Kubernetes (EKS/AKS): EU-central container orchestration enforcing strict data residency and resource quotas
- OpenTelemetry & Prometheus: Distributed tracing and metrics aggregation for SLA monitoring

## Rationale
Decoupling the ingestion worker from the core search service protects the sub-800ms search SLA during heavy synchronization. Asynchronous event consumption via Kafka ensures reliable, real-time availability projections without cross-service bottlenecks.