## Overview
The Library Management System is a solution for public and academic libraries to catalogue items and manage circulation. The architecture utilizes a containerized microservices approach centered around a Core Transactional Service Container to handle business logic.

## Key Elements
- API Gateway / BFF Container
- Core Transactional Service Container (Microservice / REST / gRPC)
- Search Service Container (Elasticsearch / OpenSearch)
- Message Broker Container (RabbitMQ / Kafka)
- Distributed Cache Container (Redis)
- Worker / Background Task Container
- EU-Hosted Relational Database

## Relationships
- API Gateway / BFF Container -> Core Transactional Service Container: Routes requests [Internal gRPC/REST]
- Core Transactional Service Container -> Message Broker Container: Publishes events [AMQP/Kafka]
- Core Transactional Service Container -> Distributed Cache Container: Caches and retrieves fast data [Redis Protocol]
- Core Transactional Service Container -> EU-Hosted Relational Database: Persists core transactions [SQL/ORM]

## Technology Stack
- gRPC / Protobuf: Internal service-to-service communication for strong typing and performance
- Transactional Outbox Pattern: Ensures reliable event publishing without dual-write inconsistencies
- Domain-Driven Design (DDD): Modular monolith boundaries within the service for circulation and cataloguing
- Optimistic Concurrency Control: Handles high-contention item checkouts via version columns
- W3C Trace Context: Distributed tracing standards for latency and bottleneck analysis

## Rationale
This architecture ensures strict EU-only data residency while maintaining high availability and low latency. Resiliency patterns and modular boundaries protect core circulation workflows from cascading failures.