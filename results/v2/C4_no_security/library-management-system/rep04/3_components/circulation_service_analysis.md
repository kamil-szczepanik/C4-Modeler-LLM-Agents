## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. The system ensures EU-only data residency and sub-800ms search responses.

## Key Elements
- Circulation Service (Java/Spring Boot container)
- PostgreSQL database (EU-hosted)
- Internal Event Bus (Apache Kafka)
- Payment Gateway (External)
- LoanManagementComponent, HoldQueueComponent, FineManagementComponent, PolicyOverrideComponent, CirculationDataRepository, CirculationEventPublisher (Spring @Service components)
- Managed Kubernetes Cluster (EKS/AKS) in EU-central
- EU-hosted Log & Metrics Aggregator

## Relationships
- Circulation Service -> PostgreSQL: Reads/writes transactional data via PostgreSQL wire protocol
- Circulation Service -> Payment Gateway: Processes fine payments via HTTPS/REST
- Circulation Service -> Internal Event Bus: Publishes domain events via Kafka protocol
- Circulation Service components -> EU-hosted Log & Metrics Aggregator: Routes logs/metrics via OpenTelemetry

## Technology Stack
- Java 17 / Spring Boot: Core runtime for the Circulation Service
- Spring Data JPA & HikariCP: Database interaction and connection pooling
- Resilience4j: Circuit breakers for payment gateway resilience
- Apache Kafka & Spring Cloud Stream: Event-driven messaging
- Managed Kubernetes (EKS/AKS) with HPA: Container orchestration and scaling

## Rationale
This architecture isolates core transactional logic into modular Spring components while leveraging Kubernetes and Kafka for scalable, resilient self-service workflows. Strict compliance with EU data residency is maintained via localized database persistence and EU-hosted observability tooling.