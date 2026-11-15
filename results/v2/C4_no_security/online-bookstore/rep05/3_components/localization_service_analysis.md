## Overview
The Localization Service provides multi-region regional adaptation, formatting, and dynamic multi-currency conversion (USD, EUR, GBP) for the online bookstore. It ensures low-latency operations and graceful degradation to protect global conversion rates and checkout flows.

## Key Elements
- Localization Controller
- Currency Exchange Engine
- Locale Policy & Compliance Provider
- Amazon ElastiCache (Redis)
- Amazon S3
- AWS API Gateway & Application Load Balancer
- Amazon ECS on Fargate
- CloudWatch Canaries

## Relationships
- API Gateway & Load Balancer -> Localization Controller: Routes requests via [gRPC / REST]
- Currency Exchange Engine -> Amazon ElastiCache (Redis): Queries cached exchange rates via [Redis Protocol]
- Currency Exchange Engine -> Upstream Rate APIs: Fetches updates via [HTTPS] with [Circuit Breaker]
- Locale Policy & Compliance Provider -> Amazon S3: Reads regional rules via [HTTPS / AWS SDK]

## Technology Stack
- Node.js / TypeScript: Core runtime for ECS container components ensuring rapid development and async I/O.
- gRPC: Internal communication protocol for low-latency retrieval of locale and conversion data.
- Amazon ElastiCache (Redis): In-memory caching for live exchange rates supporting stale-while-revalidate patterns.
- Amazon S3: Static key-value store for fast regional compliance and tax-display JSON assets.
- AWS CloudWatch Canaries: Synthetic monitoring tools for multi-region availability probing.

## Rationale
Decomposing the Localization Service into specialized sub-components backed by Redis ensures sub-50ms global response times without blocking checkout. Implementing stale-while-revalidate caching and circuit breakers guarantees high availability and zero dropped transactions during upstream API failures.