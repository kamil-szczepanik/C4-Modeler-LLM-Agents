## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It utilizes a distributed architecture with strict EU data residency compliance to ensure sub-800ms search responses.

## Key Elements
- Self-Service Patrons & Library Staff
- Frontend SPA served via CDN
- API Gateway with TLS termination and IAM token validation
- Decoupled Core Business Services
- Elasticsearch/OpenSearch Search Engine Container
- PostgreSQL Database Container
- Apache Kafka or RabbitMQ Async Event Broker Container
- Redis Shared Caching Container
- S3/HTTPS Compatible File Storage Container
- Background Worker Service and Configuration Service

## Relationships
- Core Business Services -> Shared Caching Container: Retrieves and stores cached data [Redis protocol]
- Core Business Services -> PostgreSQL Database Container: Queries persistent data [SQL/TCP]
- Frontend SPA -> API Gateway: Routes client requests [HTTPS]
- API Gateway -> Core Business Services: Forwards validated requests [gRPC/REST]

## Technology Stack
- **Redis:** Chosen for the Shared Caching Container to meet 99th-percentile search performance (< 800 ms) via in-memory data access.
- **PostgreSQL:** Selected as the primary relational database for robust catalog and circulation persistence.
- **Elasticsearch/OpenSearch:** Deployed for high-performance item catalog searching.
- **Apache Kafka / RabbitMQ:** Used for asynchronous messaging between decoupled microservices.

## Rationale
This architecture uses an in-memory caching tier backed by microservices and strict circuit breaker resilience patterns to satisfy high-throughput search and circulation requirements. Regional deployment decisions and robust data governance ensure strict adherence to EU data residency mandates.