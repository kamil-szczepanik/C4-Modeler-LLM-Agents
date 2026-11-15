## Overview
The Catalog & Search Container manages product discovery and browsing for the Online Bookstore across multiple global regions. It utilizes a read-optimized, highly scalable architecture to guarantee rapid search responses under heavy user traffic.

## Key Elements
- Web Application/API Gateway
- Catalog & Search Container
- AWS OpenSearch / Dedicated Data Store
- AWS ElastiCache / Redis
- Background Worker / Job Processing Container

## Relationships
- Web Application/API Gateway -> Catalog & Search Container: Routes search and browse requests [gRPC/REST over TLS]
- Catalog & Search Container -> AWS OpenSearch: Queries product index [TCP]
- Catalog & Search Container -> AWS ElastiCache: Caches high-frequency queries and exchange rates [TCP]

## Technology Stack
- AWS ECS/EKS: Container orchestration for horizontal scalability (R-05)
- AWS OpenSearch: Dedicated search engine for sub-100ms keyword queries (R-01, R-06)
- Redis / ElastiCache: In-memory read-through caching for high-frequency queries (R-06)
- Protocol Buffers / gRPC: Strict schema contracts and efficient inter-container communication

## Rationale
CQRS and regional data isolation isolate read-heavy browsing workloads to ensure sub-2-second page loads and 99.95% uptime. Read-through caching and strict query limits maintain performance and security under high global concurrency.