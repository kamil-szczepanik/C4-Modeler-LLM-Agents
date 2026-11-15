## Overview
The Search Microservice of the Library Management System catalogues and retrieves physical and digital items. It uses a decomposed Java/Spring Boot architecture to ensure EU-only data residency and sub-800ms search performance.

## Key Elements
- Search API Controller (Java 17, Spring Boot)
- Search Query Engine (Java 17, Spring Boot, Elasticsearch High-Level REST Client)
- Index Synchronizer (Java 17, Spring Boot, RabbitMQ Consumer)
- Search Cache Manager (Java 17, Spring Boot, Redis)
- Elasticsearch (Search Engine & Data Store)
- PostgreSQL (Primary Relational Database)
- Message Broker (RabbitMQ)
- Secure Vault (HashiCorp Vault)

## Relationships
- API Gateway -> Search API Controller [mTLS, REST/JSON]
- Search API Controller -> Secure Vault [HTTPS/Token]
- Search Query Engine -> Search Cache Manager [In-Memory/TCP]
- Search Query Engine -> Elasticsearch [TLS/mTLS, TCP/Transport]
- Index Synchronizer -> Message Broker [AMQP]
- Index Synchronizer -> PostgreSQL [JDBC]
- Index Synchronizer -> Elasticsearch [TLS/mTLS, TCP/Transport]
- Search Cache Manager -> Secure Vault [HTTPS/Token]

## Technology Stack
- Java 17 & Spring Boot: Core runtime and framework for microservice components providing enterprise reliability.
- Elasticsearch: Dedicated search engine ensuring 99th-percentile search responses under 800 ms (R-05).
- Redis: In-memory cache for frequent search queries to reduce Elasticsearch load.
- RabbitMQ: Asynchronous message broker for reliable index synchronization.
- HashiCorp Vault: Secure credential management using short-lived tokens.

## Rationale
Decomposing the search container into specialized Spring Boot components with caching, circuit breaking, and secure data storage isolates business logic and guarantees EU data compliance. This structure directly satisfies performance SLAs and strict security mandates.