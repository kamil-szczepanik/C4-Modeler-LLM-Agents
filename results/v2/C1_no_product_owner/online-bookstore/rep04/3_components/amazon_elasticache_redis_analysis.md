## Overview
The Online Bookstore system uses Amazon ElastiCache Redis for high-performance in-memory session management and shopping cart persistence. It provides low-latency data access to support global scaling requirements and fast page loads.

## Key Elements
- Session Store Module
- Distributed Shopping Cart Module
- Cache-Aside / Eviction Management Module
- Core E-Commerce Service
- Amazon CloudWatch & AWS KMS

## Relationships
- Core E-Commerce Service -> Session Store Module: Read/Write user sessions via Redis RESP protocol over TLS
- Core E-Commerce Service -> Distributed Shopping Cart Module: Read/Write cart items via Redis RESP protocol over TLS
- Core E-Commerce Service -> Cache-Aside / Eviction Management Module: Configure TTLs and invalidations via Redis RESP protocol over TLS
- Amazon ElastiCache Redis -> Amazon S3: Automated daily snapshots and AOF persistence
- Amazon ElastiCache Redis -> Amazon CloudWatch: Metrics monitoring (EngineCPUUtilization, DatabaseMemoryUsagePercentage, Slow Log)

## Technology Stack
- Amazon ElastiCache Redis: Clustered mode with Multi-AZ replication for 99.95% availability
- Redis RESP over TLS: Secure network protocol for application-to-cache communication
- AWS KMS: Customer Managed Keys for encryption at rest
- Redis ACLs: Granular keyspace authorization (`session:*`, `cart:*`)
- `cache.m6g.xlarge`: Node instance type supporting ElastiCache Auto-Scaling

## Rationale
This architecture uses an in-memory cluster to guarantee sub-millisecond data retrieval, satisfying the requirement for page loads under two seconds on 3G networks. Multi-AZ replication and automated snapshot policies provide high availability and disaster recovery across AWS regions.