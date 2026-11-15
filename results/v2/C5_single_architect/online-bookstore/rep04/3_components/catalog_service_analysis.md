## Overview
The Online Bookstore is a scaled-down e-commerce platform for purchasing physical and electronic books with integrated reviews and recommendations. The Catalog Service component provides high-performance browsing and keyword search capabilities to support 1 million monthly active users globally on AWS.

## Key Elements
*   **Catalog API Controller**: Handles incoming gRPC and HTTP requests from the API Gateway using Go.
*   **Catalog Domain**: Encapsulates business logic for browsing, keyword searching, and inventory status using Go modules.
*   **Product Repository**: Manages persistence and SQL query generation using database/sql with the pq driver.
*   **Search Adapter**: Interfaces with text-search indices for complex keyword queries using Go client packages.
*   **Cache Container**: Provides product caching via Amazon ElastiCache Redis.
*   **Product Database**: Stores relational product data via PostgreSQL (RDS).

## Relationships
*   **API Gateway** -> **Catalog API Controller**: Routes catalog queries via gRPC and HTTP.
*   **Catalog API Controller** -> **Catalog Domain**: Invokes business logic via in-memory function calls.
*   **Catalog Domain** -> **Product Repository**: Reads and writes product data via PostgreSQL Wire Protocol over TCP.
*   **Catalog Domain** -> **Cache Container**: Checks and populates product cache via Redis Protocol over TCP.
*   **Catalog Domain** -> **Search Adapter**: Queries product indices via HTTP over TCP.

## Technology Stack
*   **Go**: Powers the Catalog Service components for high concurrency and low latency.
*   **PostgreSQL (RDS)**: Provides reliable relational data storage for product catalogs.
*   **Amazon ElastiCache (Redis)**: Delivers fast in-memory caching to meet strict performance requirements.
*   **AWS OpenSearch / PostgreSQL Full-Text Search**: Enables scalable keyword search functionality.

## Rationale
This clean architecture decouples transport, business logic, and data access to handle 1 million MAU without performance degradation. Utilizing dedicated caching and search adapters ensures page loads remain under two seconds even under heavy user demand.