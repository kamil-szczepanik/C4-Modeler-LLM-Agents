## Overview
The Online Bookstore system is a scalable e-commerce platform for physical and electronic books, featuring recommendations, reviews, and secure checkout. It utilizes a containerized microservices architecture hosted on AWS across multiple global regions.

## Key Elements
- Session Store Component
- Product Catalog Cache Component
- Distributed Rate Limiter Component
- Cart Persistence Component
- Idempotency & Deduplication Component
- AWS ElastiCache Cluster Nodes
- Order & Checkout Service
- Catalog & Search Service
- Customer SPA & AWS API Gateway
- Amazon Aurora PostgreSQL
- AWS Distro for OpenTelemetry (ADOT Sidecar)

## Relationships
- Order & Checkout Service -> Session Store Component: Manages user sessions [Redis Protocol via AWS VPC Private Subnets]
- Catalog & Search Service -> Product Catalog Cache Component: Reads/writes hot catalogue items [Redis Protocol]
- Customer SPA via AWS API Gateway -> Cart Persistence Component: Reads/updates active carts [Redis Protocol / gRPC]
- Product Catalog Cache Component -> Amazon Aurora PostgreSQL: Cache-aside fallback [PostgreSQL Wire Protocol]
- Order & Checkout Service -> Idempotency & Deduplication Component: Checks/sets transaction tokens [Redis Protocol]
- Redis ElastiCache -> AWS Distro for OpenTelemetry (ADOT Sidecar): Exports Redis metrics [OpenTelemetry Protocol / Prometheus]

## Technology Stack
- AWS ElastiCache for Redis (Cluster Mode Enabled): In-memory data store for sub-second caching and session management
- Redis Data Structures (Strings, Hashes, Sorted Sets, `SETNX`): Enables atomic operations and distributed lock safety
- AWS ElastiCache Multi-AZ with Automatic Failover: Ensures high availability and cross-region low latency (<10ms)
- Amazon Aurora PostgreSQL: Primary relational database utilizing cache-aside fallback
- AWS Distro for OpenTelemetry (ADOT): Provides enhanced monitoring and metrics collection

## Rationale
This architecture ensures sub-second page loads and high scalability to handle 1 million MAU without degradation. Multi-AZ deployment and Redis clustering guarantee 99.95% availability while protecting core databases during peak traffic.