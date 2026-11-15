## Overview
Core Domain Services handle item cataloging and circulation workflows for the Library Management System. They ensure EU-only data residency and sub-800ms search performance.

## Key Elements
* **Catalog Management Component**: Manages physical and digital item cataloging (Spring Data JPA)
* **Circulation Engine Component**: Handles check-in/out workflows with distributed locking (Spring State Machine)
* **EU Policy Enforcement Interceptor**: Validates EU data residency rules (Spring AOP)
* **Domain Event Publisher**: Emits cryptographically signed events (Spring Kafka)
* **Search Sync Synchronizer Component**: Transforms and buffers events for index updates (Spring Kafka Consumer)

## Relationships
* **Circulation Engine Component** -> **EU Policy Enforcement Interceptor**: Intercepts commands synchronously [In-Memory Method Invocation]
* **EU Policy Enforcement Interceptor** -> **Data Storage (PostgreSQL)**: Persists transactional data [SQL / JDBC]
* **Domain Event Publisher** -> **Async Message Broker (Apache Kafka)**: Publishes domain events [Apache Kafka Protocol]
* **Async Message Broker (Apache Kafka)** -> **Search Sync Synchronizer Component**: Consumes change events [Apache Kafka Protocol]
* **Search Sync Synchronizer Component** -> **Search Engine (Elasticsearch)**: Bulk indexes metadata asynchronously [REST / HTTP with Bulk API]

## Technology Stack
* **Java / Spring Boot**: Core container framework for enterprise reliability and modularity
* **Spring State Machine**: Manages complex circulation state transitions deterministically
* **Spring AOP**: Intercepts method calls to enforce EU-only data residency at the domain layer
* **Apache Kafka & Dead-Letter Queues (DLQ)**: Enables asynchronous event publishing and decoupled search synchronization without blocking core circulation

## Rationale
This architecture uses Domain-Driven Design to isolate business logic, enforce strict EU data residency compliance, and use asynchronous event streaming to meet the 99th-percentile search latency requirement under 800 ms.