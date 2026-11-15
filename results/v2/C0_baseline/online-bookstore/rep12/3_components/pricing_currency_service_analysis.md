## Overview
The Pricing & Currency Service provides real-time multi-currency conversion, promotional pricing, and immutable audit logs for the online bookstore. It ensures low-latency, secure pricing retrieval across multiple global regions to support high-throughput browsing and checkout.

## Key Elements
- Pricing Controller (Go, Fiber)
- Currency Conversion Engine (Go)
- Rule Evaluation Engine (Go)
- Rate Syncer Worker (Go)
- Pricing Repository (Go, Amazon Aurora PostgreSQL)
- Rate Cache Manager (Go, Redis)

## Relationships
- API Gateway -> Pricing Controller: Routes requests via gRPC over mTLS
- Pricing Controller -> Rule Evaluation Engine: Passes context via gRPC metadata
- Currency Conversion Engine -> Rate Cache Manager: Queries rates via in-memory Redis TLS
- Pricing Repository -> Amazon Aurora: Persists audit logs via PostgreSQL wire protocol
- Rate Syncer Worker -> AWS Secrets Manager: Retrieves credentials via HTTPS

## Technology Stack
- Go: Chosen for high concurrency and low memory footprint to meet performance SLAs
- Amazon Aurora PostgreSQL: Provides scalable, globally replicated relational storage for audit compliance
- Redis: Delivers sub-millisecond caching for pre-computed price matrices
- AWS KMS: Secures data at rest and cryptographic signing for regional data protection

## Rationale
This architecture uses pre-computed price matrices and distributed caching to guarantee sub-millisecond lookups and sub-2-second page loads. Strict security controls, encrypted storage, and graceful degradation policies ensure regulatory compliance and high availability during third-party outages.