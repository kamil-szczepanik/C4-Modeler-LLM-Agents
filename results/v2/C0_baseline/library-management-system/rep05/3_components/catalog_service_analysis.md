## Overview
• The Library Management System provides unified cataloging, circulation, and self-service portals for public and academic libraries.
• It ensures rapid asset discovery and strict EU-only data residency compliance.

## Key Elements
• Users: Library Patrons, Library Staff
• External Systems: External Identity Provider, Digital Content Providers, Third-Party Payment Processor, External Notification Gateway, EU-certified Cloud Provider Infrastructure
• Containers: Web Application / API Gateway, Catalog Service (Spring Boot Java), Circulation Service, Notification Service, PostgreSQL, Elasticsearch, Event Bus (Apache Kafka / RabbitMQ), Observability Backend (OpenTelemetry)
• Components (Catalog Service): Catalog Controller, Catalog Management Service, Search & Indexing Engine, Content Sync Client, Digital Access Coordinator

## Relationships
• Web Application / API Gateway -> Catalog Service: Routes catalog queries and commands [gRPC / REST, mTLS]
• Catalog Controller -> Digital Access Coordinator: Delegates digital retrieval requests [gRPC]
• Catalog Management Service -> PostgreSQL: Persists relational catalog metadata [JDBC / Spring Data JPA]
• Search & Indexing Engine -> Elasticsearch: Executes low-latency full-text searches [Elasticsearch REST Client]
• Catalog Management Service -> Event Bus (Apache Kafka / RabbitMQ): Publishes metadata mutation events via Transactional Outbox Pattern [Spring Kafka / AMQP]
• Digital Access Coordinator -> Digital Content Providers: Requests access tokens and streaming links [HTTPS / OAuth2]

## Technology Stack
• Java / Spring Boot: Core runtime for Catalog Service providing robust enterprise capabilities.
• PostgreSQL: Relational database with AES-256 encryption-at-rest for metadata storage.
• Elasticsearch: Search engine delivering <800ms 99th-percentile search performance.
• Apache Kafka / RabbitMQ: Event bus handling asynchronous search synchronization via Outbox Pattern.
• OpenTelemetry: Observability backend for end-to-end distributed tracing.

## Rationale
• This architecture achieves sub-800ms search latency using Elasticsearch while enforcing EU data residency constraints within certified cloud infrastructure.
• It ensures system resilience and security through the Transactional Outbox Pattern, mTLS, and OAuth2-secured digital access coordination.