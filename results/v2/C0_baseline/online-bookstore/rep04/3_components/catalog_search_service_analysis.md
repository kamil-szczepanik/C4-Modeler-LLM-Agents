## Overview
The Online Bookstore system is a scalable e-commerce platform for physical and electronic books, providing fast discovery, secure checkout, reviews, and recommendations. The Catalog & Search Service is a Java Spring Boot container utilizing Elasticsearch to deliver sub-second, resilient product search and catalog management.

## Key Elements
- **Users**: Book Buyer / Customer, Content Manager
- **External Systems**: Auth0 / AWS Cognito, Currency Exchange Rate Service
- **Containers**: React SPA, AWS API Gateway, Catalog & Search Service (Java Spring Boot, Elasticsearch), Amazon RDS PostgreSQL (with Read Replicas), Amazon ElastiCache (Redis), AWS EventBridge
- **Components**: Search Controller & Faceted Query Engine, Catalog Management Component, Event Publisher Component, Cache-Aside Manager, Localization & Currency Resolver Component, Bulk Index Synchronization Component

## Relationships
- AWS API Gateway -> Search Controller: Routes catalog and search queries via [mTLS / REST and gRPC]
- Search Controller -> Elasticsearch: Executes DSL queries via [Transport over TCP]
- Catalog Management -> Amazon RDS PostgreSQL: Persists catalog state via [JDBC / Encrypted TCP]
- Cache-Aside Manager -> Amazon ElastiCache (Redis): Manages query TTLs via [RESP over TCP]
- Event Publisher -> AWS EventBridge: Publishes `ProductUpdated` and `StockChanged` events via [Asynchronous event publishing]
- Bulk Index Sync -> Amazon RDS PostgreSQL Read Replicas: Reads bulk catalog updates via [JDBC / Encrypted TCP]
- Bulk Index Sync -> Elasticsearch: Bulk upserts documents via [REST/HTTPs]

## Technology Stack
- **Java Spring Boot**: Core container framework for robust, scalable backend logic
- **Elasticsearch**: Enables high-performance keyword and faceted search (R-01, R-06)
- **Amazon RDS PostgreSQL**: Authoritative relational data store utilizing read replicas for scale
- **Amazon ElastiCache (Redis)**: Caches search results and powers distributed rate limiting
- **AWS ECS on Fargate**: Executes zero-downtime blue/green deployments
- **AWS EventBridge**: Handles asynchronous event publishing for recommendations

## Rationale
This architecture uses Elasticsearch and Redis caching to handle 1M MAU with sub-2-second page loads, satisfying performance and scalability NFRs. PostgreSQL read replicas, ECS blue/green deployments, and Resilience4j circuit breakers ensure 99.95% availability and high resilience.