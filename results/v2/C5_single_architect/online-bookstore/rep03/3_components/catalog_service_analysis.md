## Overview
The Catalog Service is a microservice within the Online Bookstore that manages book catalog data, keyword search, and customer reviews. It uses a modular internal architecture to support scalable e-commerce operations.

## Key Elements
- **CatalogController**: NestJS controller exposing RESTful endpoints for browsing, search, and reviews.
- **SearchService**: Encapsulates query logic for high-performance keyword searches.
- **ReviewService**: Manages business logic for customer reviews and 5-star ratings.
- **CacheManager**: Handles caching of hot catalog data to reduce database load.
- **CatalogRepository**: Handles core book metadata persistence.
- **Amazon OpenSearch**: External system providing keyword search indexing.
- **Amazon DynamoDB**: NoSQL database for customer reviews and ratings.
- **Amazon ElastiCache (Redis)**: In-memory cache for frequently accessed book details and search results.

## Relationships
- `CatalogController` -> `SearchService`: In-process method calls [TypeScript]
- `CatalogController` -> `ReviewService`: In-process method calls [TypeScript]
- `CatalogController` -> `CacheManager`: In-process method calls [TypeScript]
- `SearchService` -> `Amazon OpenSearch`: Performs keyword search [HTTPS / REST]
- `ReviewService` -> `Amazon DynamoDB`: Reads and writes reviews [TCP / DynamoDB API]
- `CacheManager` -> `Amazon ElastiCache (Redis)`: Caches hot catalog data [TCP / Redis Protocol]

## Technology Stack
- **TypeScript & NestJS**: Core language and framework for modular service decomposition and maintainability.
- **Amazon OpenSearch**: Chosen for high-performance keyword search capabilities (R-01).
- **Amazon DynamoDB**: Selected for low-latency read/writes of customer reviews and ratings (R-03).
- **Amazon ElastiCache (Redis)**: Implemented to meet strict <2s page load performance (R-06) and 1M MAU scalability (R-05).

## Rationale
This component architecture uses specialized data stores (OpenSearch, DynamoDB, Redis) coordinated via NestJS components to meet stringent scalability and sub-2-second performance requirements. The internal caching and search offloading ensure high availability and efficient resource utilization under heavy load.