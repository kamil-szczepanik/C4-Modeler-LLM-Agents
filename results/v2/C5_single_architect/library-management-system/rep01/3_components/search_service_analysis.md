## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It enforces EU-only data residency while guaranteeing high-performance search responses.

## Key Elements
* Patrons / Library Members and Librarians / Staff (Users)
* Web Application (React, TypeScript)
* API Gateway (Kong / Nginx)
* Core Business Service (Java, Spring Boot)
* Search API Application (Java, Spring Boot)
* Elasticsearch Cluster (Elasticsearch 8.x)
* Query Cache Layer (Local Caffeine cache)
* Database (PostgreSQL) and Redis Cache (Redis)
* Notification Worker (Node.js)
* External Payment Gateway, Digital Content Providers, Notification Service, External Enterprise Search Service

## Relationships
* API Gateway -> Search API Application: Forwards search requests via `gRPC`
* Search API Application -> Elasticsearch Cluster: Executes queries via `Transport Client over TCP`
* Core Business Service -> Search API Application: Syncs catalogue changes via `JSON over Kafka` events
* Search API Application -> Query Cache Layer: Checks recent search results via `In-memory Java API`

## Technology Stack
* Java with Spring Boot for Search API Application, providing robust backend logic and EU data residency enforcement
* Elasticsearch 8.x for indexing and full-text search capabilities
* Local Caffeine cache for in-memory query caching
* Apache Kafka for asynchronous event-driven catalogue synchronization
* `gRPC` for internal inter-service communication

## Rationale
This architecture uses an isolated Search API Application fronting an Elasticsearch cluster to meet the strict sub-800ms search performance requirement. Asynchronous Kafka synchronization and local caching minimize latency and resource load while maintaining data consistency.