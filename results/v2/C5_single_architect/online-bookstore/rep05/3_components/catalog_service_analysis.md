## Overview
The Catalog Service is a Go-based microservice responsible for managing book metadata, inventory state, and high-performance keyword searches for the Online Bookstore. It is designed to handle 1M MAU while meeting strict performance requirements under 2 seconds.

## Key Elements
* Catalog API Controller (Go, net/http)
* Search & Indexing Engine (Go, Amazon OpenSearch Service)
* Catalog Domain Manager (Go)
* Cache Aside Proxy (Go, go-redis)

## Relationships
* API Gateway -> Catalog API Controller: Routes catalogue and search queries [gRPC / HTTPS]
* Catalog Domain Manager -> Database (DynamoDB): Persists records [DynamoDB Go SDK]
* Catalog Domain Manager -> Cache Aside Proxy: In-memory lookups [TCP / Redis RESP]
* Catalog Domain Manager -> Search & Indexing Engine: Index synchronization [AWS SDK / Async]
* Message Broker (Amazon SQS) -> Catalog Domain Manager: Subscribes to inventory updates [SQS Protocol]

## Technology Stack
* Go: Chosen for high concurrency and low-latency execution.
* Amazon OpenSearch Service: Offloads full-text search to meet performance targets.
* Amazon DynamoDB: Scalable NoSQL storage for catalogue metadata.
* Amazon ElastiCache (Redis): Caches hot-spot read requests to minimize latency.

## Rationale
This component architecture uses specialized search and caching layers to guarantee sub-2-second page loads for 1M MAU. Go containers deployed on AWS Fargate ensure high availability and scalable throughput.