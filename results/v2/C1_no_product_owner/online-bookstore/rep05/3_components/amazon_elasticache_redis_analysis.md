## Overview
The system is an Amazon ElastiCache (Redis) container providing high-performance in-memory caching for user sessions, active shopping carts, and recommendations in an online bookstore. It ensures sub-millisecond data retrieval to support high scalability and sub-2-second page load times.

## Key Elements
- **Session Store Engine**: Redis Hash managing user authentication tokens and preferences.
- **Cart Cache Engine**: Redis String/Hash persisting transient shopping carts during checkout.
- **Recommendation Cache Engine**: Redis Sorted Sets (`ZSET`) storing precomputed 'Customers also bought' data.

## Relationships
- **Order & Checkout Service -> Session Store Engine**: Reads/writes user session data via RESP protocol over TLS 1.3 [TCP 6379].
- **Order & Checkout Service -> Cart Cache Engine**: Manages active shopping cart state via RESP protocol over TLS 1.3 [TCP 6379].
- **Recommendation Service -> Recommendation Cache Engine**: Queries cached recommendations via RESP protocol over TLS 1.3 [TCP 6379].

## Technology Stack
- **Amazon ElastiCache for Redis**: In-memory data store providing sub-millisecond latency and automatic multi-AZ failover for high availability.
- **Redis ACLs & AUTH**: Enforces role-based access control, least privilege, and encrypted credentials managed via AWS Secrets Manager.
- **Terraform / AWS CDK**: Infrastructure-as-Code tooling for repeatable multi-AZ deployments.
- **Amazon CloudWatch & Datadog**: Observability stack tracking CPU utilization, swap usage, and cache metrics.

## Rationale
This architecture uses ElastiCache Cluster Mode Enabled with multi-AZ replication to meet the 99.95% uptime SLA and 1M MAU scalability targets. Strict network isolation, Redis ACLs, and automated TTL expirations ensure GDPR/CCPA compliance and robust security posture.