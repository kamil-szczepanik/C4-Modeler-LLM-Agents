## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. The architecture enforces strict EU-only data residency and sub-800ms search performance.

## Key Elements
* Core Domain Services (Microservices / gRPC / REST)
* Cataloguing and Circulation bounded contexts
* Primary Transactional Datastore (Relational Database / SQL)
* Caching Layer (Redis)
* Dedicated Search Tier
* Asynchronous Event Bus (Message Broker) (AMQP / Kafka)
* API Composition / BFF Container (HTTP/REST, OpenAPI)

## Relationships
* API Composition / BFF Container -> Core Domain Services [gRPC/REST]
* Core Domain Services -> Primary Transactional Datastore [TCP/SQL]
* Core Domain Services -> Caching Layer (Redis) [TCP/SQL]
* Core Domain Services -> Asynchronous Event Bus (Message Broker) [AMQP/Kafka]
* Background Worker / Job Scheduling Container -> Core Domain Services [Internal Protocol]

## Technology Stack
* gRPC: Selected for internal communication to provide strong typing and performance supporting the <800ms latency requirement.
* Protocol Buffers: Utilized for contract-first development and backward compatibility.
* Redis: Used as a caching layer with regional pinning to satisfy EU data residency.
* CQRS Pattern: Implemented to separate write operations from read-heavy queries targeting the Dedicated Search Tier.
* Hexagonal Architecture: Enforced within microservices to isolate core domain logic from infrastructure.

## Rationale
The architecture combines CQRS and gRPC caching to meet strict performance targets under load. Hexagonal design, contract-first APIs, and regional pinning guarantee maintainability and compliance with EU data residency.