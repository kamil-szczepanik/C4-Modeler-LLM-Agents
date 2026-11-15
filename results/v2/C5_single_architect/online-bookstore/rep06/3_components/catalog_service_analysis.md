## Overview
The Catalog Service is a core microservice within the Online Bookstore e-commerce platform that handles book browsing, keyword searches, and product data management. It ensures high performance and scalability to support 1 million monthly active users while meeting sub-2-second page load requirements.

## Key Elements
* Customer / Users
* API Gateway (Amazon API Gateway)
* Catalog Service (Go)
* Catalog API Handler (Go component)
* Search Engine Client / Indexer (Go component)
* Product Repository (Go component)
* Cache Manager (Go component)
* Amazon OpenSearch Service
* Amazon Aurora PostgreSQL
* Amazon ElastiCache (Redis)
* Amazon SNS / Amazon SQS

## Relationships
* API Gateway -> Catalog API Handler: Routes catalog requests [gRPC / HTTPS]
* Catalog API Handler -> Product Repository: Encapsulates data access [In-process Go interfaces]
* Catalog API Handler -> Search Engine Client / Indexer: Executes keyword searches [In-process Go interfaces]
* Search Engine Client / Indexer -> Amazon OpenSearch Service: Queries product search index [HTTPS / JSON]
* Catalog API Handler -> Cache Manager: Manages hot data retrieval [In-process Go structs]
* Cache Manager -> Amazon ElastiCache (Redis): Caches frequent product details [TCP / Redis Protocol]
* Product Repository -> Amazon Aurora PostgreSQL: Persists transactional catalog data [TCP / PostgreSQL protocol]
* Aurora PostgreSQL -> OpenSearch Service: Synchronizes search index [Amazon SNS / SQS]

## Technology Stack
* Go: Chosen for high-throughput, low-latency microservice performance.
* Amazon OpenSearch Service: Provides fast, scalable keyword and search indexing to meet performance SLA.
* Amazon Aurora PostgreSQL: Relational storage for reliable transactional catalog data.
* Amazon ElastiCache (Redis): In-memory caching layer to reduce database load and ensure high availability.
* Amazon SNS / Amazon SQS: Asynchronous messaging for reliable data synchronization.

## Rationale
This architecture uses Go and caching layers to achieve high availability and sub-2-second page loads. Offloading keyword search to Amazon OpenSearch Service decouples heavy queries from the transactional database, enabling the system to scale smoothly to 1M MAU.