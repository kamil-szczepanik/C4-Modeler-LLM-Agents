## Overview
• High-performance distributed caching layer implemented via Amazon ElastiCache (Redis) to ensure sub-millisecond cart persistence and rapid catalog queries.
• Directly supports the 1M MAU scalability, sub-2-second page load performance, and 99.95% availability requirements.

## Key Elements
• Session & Cart Engine (In-memory Hashes/Strings)
• Catalog Query Cache (String/JSON cache with TTL)
• Pub/Sub Notification Manager (Cache eviction and invalidation)
• Order & Checkout Service (Node.js)
• Catalog & Search Service (Java Spring Boot, Elasticsearch)
• Recommendations Service (Python FastAPI)
• AWS EventBridge

## Relationships
• Order & Checkout Service -> Session & Cart Engine: Persists cart data via Encrypted TCP (RESP over TLS) with strict Redis ACLs
• Catalog & Search Service -> Catalog Query Cache: Caches search and catalog data via Encrypted TCP
• Recommendations Service -> Catalog Query Cache: Reads/writes pre-computed recommendations via Encrypted TCP (RESP over TLS)
• AWS EventBridge -> Pub/Sub Notification Manager: Triggers cache eviction via Redis PUBLISH

## Technology Stack
• Amazon ElastiCache (Redis) Cluster Mode Enabled: Chosen for sub-millisecond in-memory performance, multi-AZ replication, and automatic failover.
• Redis volatile-lru Maxmemory Policy: Prioritizes active user shopping carts over volatile cache entries under high memory pressure.
• AWS KMS & TLS: Enforces encryption at rest and in transit for GDPR/CCPA compliance and data privacy.
• Amazon CloudWatch: Provides continuous observability, slow log streaming, and resource utilization monitoring.

## Rationale
• The Redis cluster architecture delivers sub-millisecond latency and high availability to satisfy performance and uptime requirements under heavy e-commerce traffic loads. 
• Integrated security controls, automated backups, and circuit-breaking fallback strategies ensure regulatory compliance, data durability, and system resilience.