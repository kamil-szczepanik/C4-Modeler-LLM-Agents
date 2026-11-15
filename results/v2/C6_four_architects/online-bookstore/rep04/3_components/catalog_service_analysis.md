## Overview
The Catalog Service component of the Online Bookstore manages physical and electronic book catalogs, supporting high-throughput browsing, keyword searches, and digital asset delivery. It is built as a microservice running on AWS ECS Fargate using Node.js and the NestJS framework.

## Key Elements
*   **Catalog API Controller**: Exposes HTTP/2 endpoints for browsing and searching.
*   **Product Domain Service**: Encapsulates business logic, featuring a decorator-patterned Cache Interceptor.
*   **Search & Indexing Repository**: Integrates with Amazon OpenSearch for catalog searches.
*   **Relational Persistence Adapter**: Uses TypeORM to communicate with Amazon Aurora PostgreSQL.
*   **Catalog Cache Interceptor / Repository**: Backed by an Amazon ElastiCache Redis cluster via TCP.
*   **Event Publisher**: Emits domain events using the AWS SDK for Node.js.
*   **Asset Management Adapter**: Manages digital book assets stored in Amazon S3.

## Relationships
*   **Catalog API Controller -> Product Domain Service**: Invokes business logic [TypeScript Interfaces]
*   **Product Domain Service -> Catalog Cache Interceptor**: Reads/writes cached data [Redis TCP]
*   **Search & Indexing Repository -> Amazon OpenSearch**: Queries catalog indices [HTTP/2 / HTTPS REST]
*   **Relational Persistence Adapter -> Amazon Aurora PostgreSQL**: Manages relational records [PostgreSQL TCP]
*   **Asset Management Adapter -> Amazon S3**: Generates pre-signed asset URLs [HTTPS / AWS SDK]
*   **Event Publisher -> Amazon SNS/SQS**: Publishes asynchronous domain events [AWS SDK / HTTPS]

## Technology Stack
*   **Node.js with NestJS**: Chosen for modularity, clean architectural layering, and robust ecosystem support.
*   **Amazon Aurora PostgreSQL**: Provides scalable, ACID-compliant relational storage for transactional book data.
*   **Amazon OpenSearch**: Enables sub-2-second keyword search performance across the catalogue.
*   **Amazon ElastiCache Redis**: Reduces database read load and ensures low latency via in-memory caching.
*   **Amazon S3**: Securely stores digital book previews and downloadable assets.

## Rationale
This component architecture uses a modular NestJS framework and caching layers to achieve sub-2-second page loads under 1 million monthly active users. Distributed adapters isolate persistence, search, and caching concerns while maintaining strict GDPR compliance and AWS integration standards.