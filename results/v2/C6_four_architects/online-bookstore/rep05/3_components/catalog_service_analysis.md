## Overview
The Online Bookstore system is a scalable e-commerce platform for purchasing physical and electronic books, featuring reviews and recommendations. The Catalog Service container manages book catalogue data, search indexing, inventory availability reads, and multi-currency pricing.

## Key Elements
- **Catalog API Controller**: Handles incoming Express routes and input validation.
- **Catalog Service Layer**: Implements core business logic for book details.
- **Search & Filter Engine**: Manages keyword searches via Amazon OpenSearch Service.
- **Data Access Repository**: Handles persistence via Aurora PostgreSQL.
- **Cache Manager**: Manages hot catalog reads using Amazon Redis.
- **Event Listener Component**: Consumes inventory events from Amazon SQS.
- **Inventory Manager**: Encapsulates stock-availability read logic.
- **Pricing & Currency Translator**: Applies USD, EUR, and GBP currency conversions.

## Relationships
- Catalog API Controller -> Catalog Service Layer: In-process method calls
- Catalog Service Layer -> Cache Manager: Read/Write hot items [Redis Protocol / TCP]
- Search & Filter Engine -> Amazon OpenSearch Service: Query catalog index [HTTPS]
- Data Access Repository -> Aurora PostgreSQL (Region Read Replica): SQL queries [TCP/TLS]
- Amazon SQS -> Event Listener Component: Consume inventory change events [HTTPS / SQS SDK]
- Event Listener Component -> Cache Manager: Evict/Update stale keys [Redis Protocol]
- Event Listener Component -> Search & Filter Engine: Update document index [OpenSearch REST API]
- Catalog Service Layer -> Inventory Manager: Verify stock availability [In-process]
- Inventory Manager -> Data Access Repository: Stock-check queries [TCP/TLS]
- Catalog Service Layer -> Pricing & Currency Translator: Enrich book prices [In-process]

## Technology Stack
- **Runtime & Language**: Node.js v20+ with TypeScript for type-safe component boundaries.
- **Framework**: Express for routing and HTTP handling.
- **Caching**: Amazon Redis utilizing the `ioredis` client with regional read endpoints.
- **Search Client**: `@opensearch-project/opensearch` for querying Amazon OpenSearch Service.
- **Messaging SDK**: `@aws-sdk/client-sqs` for consuming Amazon SQS events.
- **Database Driver**: Native PostgreSQL drivers connecting to Amazon Aurora PostgreSQL.

## Rationale
This architecture decomposes the Catalog Service into decoupled components to handle 1 million MAU and achieve sub-2-second page loads globally. Asynchronous event consumption via SQS ensures eventual consistency across PostgreSQL, Redis, and OpenSearch without blocking HTTP threads.