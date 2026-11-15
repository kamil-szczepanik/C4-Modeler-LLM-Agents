## Overview
The Library Management System is a solution for public and academic libraries to catalogue items and manage circulation. The architecture utilizes a unified Search Service to deliver sub-800ms search performance while enforcing EU data residency.

## Key Elements
- Search Service (Java/Spring Boot)
- Search Index (Elasticsearch 8.x)
- Async Event Broker (Apache Kafka)
- API Gateway (Nginx / Spring Cloud Gateway)
- Core Domain Container (PostgreSQL)

## Relationships
- API Gateway -> Search Service: `REST/JSON over TLS`
- Search Service -> Search Index: `Elasticsearch Native Bolt/REST with mTLS`
- Search Service -> Async Event Broker: `Kafka Protocol over TLS`

## Technology Stack
- Java / Spring Boot: Unified runtime for search routing, synchronization, and analytics
- Elasticsearch 8.x: Scalable storage with fuzzy matching and faceted search support
- Apache Kafka: Asynchronous event streaming for eventual consistency and telemetry
- Kubernetes: Container orchestration with strict resource limits and persistent volume encryption

## Rationale
Unifying the search runtime into a single Java/Spring Boot service reduces operational complexity while meeting stringent EU data residency and security mandates. Elasticsearch configurations and Resilience4j circuit breakers guarantee the 800ms performance SLA.