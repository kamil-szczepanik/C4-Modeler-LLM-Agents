## Overview
[The Catalog & Search Container delivers rapid product discovery, keyword search, and personalized recommendations for the Online Bookstore system. It ensures high performance and scalability to support global users across multiple regions.]

## Key Elements
- Anonymous Shoppers and LoggedIn Customers
- API Gateway / Router Component (Go)
- Search & Query Component (Spring Boot)
- Indexing & Synchronization Component (Spring Boot)
- Recommendation Component (Go)
- Amazon OpenSearch
- Amazon SQS

## Relationships
- Edge & Ingress -> API Gateway / Router: Forwards search requests [gRPC over TLS]
- API Gateway / Router -> Search & Query Component: Routes internal queries [gRPC]
- Indexing & Synchronization Component -> Amazon SQS: Consumes CDC events and clickstream payloads [SQS Polling]
- Search & Query Component & Recommendation Component -> Amazon OpenSearch: Executes queries and retrieves indices [HTTPS / REST client]

## Technology Stack
- Go: Powers high-throughput API routing and recommendation processing for low latency.
- Spring Boot: Implements robust search query handling and indexing logic.
- Amazon OpenSearch: Stores searchable catalog data and powers ML/KNN recommendations.
- Amazon SQS: Buffers clickstream data to prevent ingestion saturation.
- AWS ECS/EKS & Route 53: Provides container orchestration, canary deployments, and multi-region failover.

## Rationale
[This decoupled, multi-region architecture uses asynchronous SQS buffering and Amazon OpenSearch to guarantee sub-2-second response times and 99.95% availability under high load. It cleanly separates query routing, indexing, and recommendation logic while maintaining strict GDPR and CCPA compliance.]