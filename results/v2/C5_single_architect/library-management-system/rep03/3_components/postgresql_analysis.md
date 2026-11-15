## Overview
The Library Management System provides catalogue management, circulation handling, and self-service portals for public and academic libraries. It ensures strict EU-only data residency and high-performance search capabilities.

## Key Elements
- Library Patron and Library Staff (Users)
- Web Application (React, TypeScript)
- API Gateway (Spring Cloud Gateway / Envoy)
- Catalogue Service, Circulation Service, Digital Content Proxy Service (Java, Spring Boot)
- Notification Worker (Node.js)
- PostgreSQL, Redis, Elasticsearch, RabbitMQ
- PostgreSQL Components: Connection Pool & Auth Manager (PgBouncer), Query Planner & Execution Engine, Relational Storage Engine, Row-Level Security Policy Enforcer, Write-Ahead Log (WAL) Manager

## Relationships
- Catalogue Service -> PostgreSQL: Reads/writes catalogue data via TCP / PostgreSQL Wire Protocol
- Circulation Service -> PostgreSQL: Manages transactional checkouts via TCP / PostgreSQL Wire Protocol
- Connection Pool & Auth Manager -> Query Planner & Execution Engine: Routes authenticated queries via Internal IPC
- Query Planner & Execution Engine -> Relational Storage Engine: Accesses data blocks via Internal IPC

## Technology Stack
- React & TypeScript: Frontend implementation for responsive self-service portals
- Java & Spring Boot: Robust backend microservices for business logic
- PostgreSQL: Relational storage with PgBouncer for connection pooling and EU compliance
- Elasticsearch: High-performance indexing for sub-800ms search requirements
- RabbitMQ: Asynchronous messaging between services
- Redis: Caching layer for session and temporary data

## Rationale
This architecture uses containerized microservices combined with PostgreSQL and PgBouncer to guarantee ACID compliance, secure EU-only data residency, and high-performance throughput. Decoupled search (Elasticsearch) and caching (Redis) directly satisfy the sub-800ms 99th-percentile search response requirement.