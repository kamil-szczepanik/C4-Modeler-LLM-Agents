## Overview
The Search & Discovery container provides high-performance keyword search, faceted filtering, and telemetry for the Online Bookstore. It processes search requests and syncs catalog data to meet strict latency and scalability requirements.

## Key Elements
- Search API Controller (Java, Spring Boot)
- Query Parser & Matcher (Apache Lucene Query DSL)
- Catalog Synchronization Consumer (Java, Apache Kafka Consumer)
- Facet & Filter Aggregator (Java, OpenSearch Aggregations API)
- Search Analytics Tracker (Java, Kafka Producer)
- Amazon OpenSearch Cluster
- Amazon MSK (Apache Kafka)

## Relationships
- AWS API Gateway -> Search API Controller [gRPC over TLS]
- Search API Controller -> Query Parser & Matcher [In-process]
- Search API Controller -> Facet & Filter Aggregator [In-process]
- Query Parser & Matcher -> Facet & Filter Aggregator [In-process]
- Query Parser & Matcher -> Amazon OpenSearch Cluster [HTTPS]
- Facet & Filter Aggregator -> Amazon OpenSearch Cluster [HTTPS]
- Amazon MSK -> Catalog Synchronization Consumer [Kafka Protocol]
- Search API Controller -> Search Analytics Tracker [In-process]
- Search Analytics Tracker -> Amazon MSK [Kafka Protocol]

## Technology Stack
- Java / Spring Boot: Core runtime for internal container components providing robust enterprise capabilities.
- Apache Lucene Query DSL & OpenSearch: Powers fuzzy matching, relevance scoring, and scalable search indexes.
- Apache Kafka (Amazon MSK): Decouples write-path catalog synchronization and telemetry streaming.
- gRPC over TLS: Ensures low-latency, secure communication from the API Gateway.

## Rationale
This decoupled event-driven architecture isolates read and write paths to guarantee sub-2-second page loads on mobile networks. The design scales horizontally on AWS to easily handle 1 million monthly active users while ensuring high availability.