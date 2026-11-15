## Overview
[A dedicated Search Service for the Library Management System, designed to catalogue physical and digital items and power sub-800ms search, discovery, and circulation portals.]

## Key Elements
- Search REST/gRPC Controller (Java/Spring Boot)
- Query Builder Component (Java)
- Faceting & Suggestion Engine (Java)
- Elasticsearch Client Adapter (Java / High-Level REST Client)
- Index Synchronization Consumer (Java / Kafka Consumer)
- Search Engine Cluster (Elasticsearch, EU-hosted)

## Relationships
- API Gateway -> Search REST/gRPC Controller: Forwards search requests [gRPC over mTLS]
- Search REST/gRPC Controller -> Query Builder Component: Passes sanitized requests and user roles [In-process Java method calls]
- Query Builder Component -> Faceting & Suggestion Engine: Processes aggregations and spellcheck [In-process Java method calls]
- Query Builder Component -> Elasticsearch Client Adapter: Passes constructed DSL queries [In-process Java method calls]
- Elasticsearch Client Adapter -> Search Engine Cluster: Executes queries/indexing [HTTP/Bolt over TCP with TLS v1.3]
- Index Synchronization Consumer -> Search Engine Cluster: Updates index data [Kafka domain events]

## Technology Stack
- Java / Spring Boot: Chosen for robust enterprise performance, rich ecosystem, and low latency to meet the <800ms NFR.
- Elasticsearch: Selected for high-performance full-text search, native faceting, and suggestion capabilities.
- Kafka: Used for asynchronous index synchronization to ensure eventual consistency without blocking core domain writes.
- OpenTelemetry: Deployed for distributed tracing and tail-latency monitoring.

## Rationale
[This architecture uses an in-process Java component decomposition backed by an isolated Elasticsearch cluster to eliminate network overhead and achieve sub-800ms search performance. Strict EU data residency, mTLS, AES-256 encryption, and circuit breakers ensure regulatory compliance, security, and high availability.]