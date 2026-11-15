## Overview
The Online Bookstore Pricing & Localization Service manages global multi-currency pricing, taxes, and localization rules across multiple AWS regions. It ensures high availability and sub-10ms performance to support secure international checkouts and compliance.

## Key Elements
- **Pricing API Controller**: Node.js/TypeScript (Fastify) component handling gRPC/HTTP requests.
- **Currency Exchange Engine**: Translates base prices into USD, EUR, and GBP using cached rates.
- **Localization Rule Resolver**: Fetches regional tax and compliance rules.
- **Price Cache Manager**: Manages caching logic and cache invalidation.
- **Exchange Rate Sync Worker**: Background worker fetching third-party currency rates.
- **Audit & Compliance Logger**: Captures administrative pricing updates.
- **AWS ElastiCache (Redis)**: Regional cache and session store with read-replicas.
- **AWS RDS PostgreSQL**: Relational database for persistent pricing and rules.
- **AWS EventBridge**: Pub/sub event bus for cache invalidation.
- **AWS Secrets Manager**: Secure storage for external API credentials.

## Relationships
- API Gateway -> Pricing API Controller: Routes localization requests [gRPC over HTTP/2, mTLS]
- Pricing API Controller -> Price Cache Manager: Reads localized pricing [Redis protocol over TCP/TLS]
- Price Cache Manager -> AWS ElastiCache: Populates and invalidates cache [TCP/TLS with Encryption at Rest/Transit]
- Localization Rule Resolver -> AWS RDS PostgreSQL: Fetches fallback rules on cache miss [TCP/TLS]
- AWS EventBridge -> Price Cache Manager: Triggers instant cache invalidation on admin updates [Pub/Sub]
- Exchange Rate Sync Worker -> AWS Secrets Manager: Retrieves API keys [IAM-authenticated task roles]

## Technology Stack
- **Node.js/TypeScript (Fastify)**: Powers the API controller and sync worker for low-latency handling.
- **AWS ECS Fargate**: Deploys containerized services across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
- **AWS ElastiCache (Redis)**: Provides sub-10ms localized pricing reads.
- **AWS RDS PostgreSQL**: Stores persistent pricing records and regional tax rules.
- **AWS EventBridge**: Facilitates real-time cache invalidation across regions.
- **AWS Secrets Manager**: Secures third-party feed credentials.

## Rationale
Decomposing the service into localized ElastiCache layers and asynchronous workers ensures sub-10ms performance and 99.95% availability under high traffic. Multi-region deployments with secure secret management and fallback mechanisms satisfy strict global compliance and uninterrupted checkout requirements.