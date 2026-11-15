## Overview
[The Online Bookstore system provides scalable e-commerce browsing, checkout, and recommendations for global users. The Catalog Container specifically manages book listings, keyword searches, and inventory metadata.]

## Key Elements
- [API Gateway & BFF: Routes incoming catalog requests using HTTPS/REST]
- [Catalog Container: Docker container hosted on Amazon ECS/EKS]
- [Internal Modules: Separated into search, inventory, and metadata packages]
- [Application Cache: Amazon ElastiCache (Redis) for rapid metadata and search retrieval]
- [Database: Amazon Aurora/RDS with Read Replicas]

## Relationships
- [API Gateway & BFF -> Catalog Container: Forwards search and browse requests via HTTPS/REST]
- [Catalog Container -> Amazon Aurora/RDS: Queries primary database and Read Replicas via SQL/TCP]
- [Catalog Container -> Amazon ElastiCache (Redis): Fetches and caches search results and exchange rates via Redis Protocol]

## Technology Stack
- [Docker & Amazon ECS/EKS: Containerization and orchestration for scalability]
- [Amazon Aurora/RDS: Relational database with connection pooling for inventory and metadata storage]
- [Amazon ElastiCache (Redis): In-memory caching layer for low-latency searches and rate limiting]
- [OpenTelemetry: Distributed tracing middleware for performance monitoring]
- [Flyway/Liquibase: Automated zero-downtime database migration management]

## Rationale
[This architecture uses containerization, caching layers, and read replicas to meet the 1M MAU scalability and sub-2-second performance requirements. Modular design and robust operational controls ensure high availability (99.95%) and secure compliance.]