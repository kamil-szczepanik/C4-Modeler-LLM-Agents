## Overview
[The Online Bookstore caching layer utilizes Amazon ElastiCache (Redis) to deliver high-performance session management, catalogue searches, and recommendations while maintaining strict security compliance. It ensures low-latency operations for 1M MAU across us-east-1, eu-west-1, and ap-southeast-1 regions.]

## Key Elements
- Amazon ElastiCache (Redis) (Parent Container)
- Session & Cart Store (Component)
- Catalog Cache Manager (Component)
- Recommendation Cache Component (Component)
- Order & Checkout Service (External Client)
- Catalog Service (External Client)
- Recommendation Service (External Client)

## Relationships
- Order & Checkout Service -> Session & Cart Store: Reads and writes cart state [Redis Protocol over TLS]
- Catalog Service -> Catalog Cache Manager: Queries and updates cached catalog data [Redis Protocol over TLS]
- Recommendation Service -> Recommendation Cache Component: Fetches pre-computed recommendations [Redis Protocol over TLS]

## Technology Stack
- Amazon ElastiCache (Redis): In-memory data store chosen for sub-millisecond latency and high throughput.
- Redis 6+ RBAC: Enforces strict user access control and keyspace isolation (`cart:`, `catalog:`, `recommendation:`).
- AWS KMS: Provides encryption-at-rest for temporary PII stored in cart states.
- TLS 1.3: Secures all data in transit across services.
- AOF Persistence: Enabled every second for cart durability during failovers.

## Rationale
[This architecture guarantees high availability and sub-2-second page loads to meet 99.95% uptime and scalability requirements. It strictly enforces GDPR/CCPA compliance through encryption and logical keyspace isolation.]