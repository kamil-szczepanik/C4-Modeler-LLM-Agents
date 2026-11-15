## Overview
The Online Bookstore is a multi-region e-commerce platform built on AWS to sell physical and electronic books with recommendations and reviews. The Catalog & Search Container handles book inventory, search capabilities, and AI/ML recommendations.

## Key Elements
- **Catalog Controller**: Spring Web/gRPC component acting as the entry point.
- **Search Service**: Elasticsearch/AWS OpenSearch component for full-text indexing and queries.
- **Inventory Manager**: Spring Data JPA component for stock and metadata.
- **Recommendation Ingestion Component**: Spring Batch component for interaction data.
- **ML Inference Bridge**: AWS SDK / SageMaker Runtime component.
- **Amazon Aurora PostgreSQL & Amazon DynamoDB**: Relational and NoSQL datastores.
- **Amazon SageMaker**: Managed machine learning service.

## Relationships
- **API Gateway -> Catalog Controller**: Routes catalog requests [gRPC over TLS].
- **Catalog Controller -> Search Service**: Queries product indices [Internal REST/HTTP over TLS].
- **Catalog Controller -> ML Inference Bridge**: Fetches recommendations [gRPC].
- **Search Service -> Amazon OpenSearch**: Indexes and retrieves catalog items [HTTPS].
- **Inventory Manager -> Amazon Aurora PostgreSQL**: Persists book data [JDBC over TLS].
- **Recommendation Ingestion Component -> Amazon DynamoDB**: Reads aggregated history [NoSQL over TLS].
- **ML Inference Bridge -> Amazon SageMaker**: Invokes models [HTTPS over TLS].

## Technology Stack
- **Spring Boot / Spring Web / Spring Batch**: Framework for internal container components.
- **Elasticsearch / AWS OpenSearch**: Full-text search and indexing engine.
- **Amazon Aurora PostgreSQL**: Relational database for transactional inventory data.
- **Amazon DynamoDB**: NoSQL database for user purchase history.
- **Amazon SageMaker**: Machine learning platform for product recommendations.

## Rationale
This architecture decouples heavy search and recommendation workloads from transactional inventory writes to ensure high performance and scalability under 1M MAU. Multi-region AWS deployment satisfies stringent availability and latency targets globally.