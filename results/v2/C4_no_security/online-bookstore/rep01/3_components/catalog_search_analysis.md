## Overview
The Online Bookstore system provides global book catalog browsing, searching, purchasing, and recommendations. It is architected for high scalability, fault tolerance, and multi-region deployment.

## Key Elements
- **Search Controller & Facade**: Spring MVC component handling REST search requests.
- **Catalog Management Service**: Admin service for CRUD book metadata operations.
- **Index Synchronization Worker**: Spring Batch/Event Listener processing async updates.
- **OpenSearch Client Repository**: Repository interacting with search indexes.
- **Circuit Breaker & Fallback Manager**: Resilience4j component for graceful degradation.
- **Amazon OpenSearch**: Managed search engine for catalog indexing.
- **Amazon RDS (PostgreSQL)**: Relational database for transactional records.
- **AWS EventBridge & SQS**: Event bus and message queue with DLQ support.

## Relationships
- **Search Controller & Facade -> Amazon OpenSearch**: Queries search indices over HTTPS.
- **Catalog Management Service -> Amazon RDS (PostgreSQL)**: Persists transactional data via TLS-encrypted JDBC/TCP.
- **AWS EventBridge -> Index Synchronization Worker**: Delivers domain events via AWS SQS using JSON over HTTPS.
- **Index Synchronization Worker -> Amazon OpenSearch**: Applies document upserts using the OpenSearch REST Client over HTTPS.

## Technology Stack
- **Java / Spring Boot**: Core language and framework for robust backend services.
- **Amazon OpenSearch**: Search engine enabling fast keyword and facet queries.
- **Amazon RDS (PostgreSQL)**: Relational data store providing ACID compliance and durability.
- **Resilience4j**: Circuit breaker library ensuring fault tolerance and availability.
- **AWS EventBridge & SQS**: Messaging infrastructure for decoupled asynchronous event-driven synchronization.

## Rationale
This architecture decouples heavy write-operations from read-heavy search requests via event-driven synchronization, ensuring high availability. Caching, circuit breakers, and multi-region replication guarantee sub-2-second page loads globally.