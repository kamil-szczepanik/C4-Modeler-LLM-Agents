## Overview
[The Online Bookstore system provides a scalable e-commerce platform for purchasing books with integrated recommendations and reviews. The Recommendation Service delivers personalized and curated book suggestions to maximize user engagement and average order value.]

## Key Elements
[
- Shoppers and Store Administrators
- Recommendation API Container (Node.js / Express)
- Background Worker Container (Python / FastAPI)
- Amazon ElastiCache (Redis)
- Amazon Kinesis
- Amazon RDS (PostgreSQL)
]

## Relationships
[
- API Gateway to Recommendation API: Fetches recommendations [HTTPS / REST]
- Recommendation API to Amazon ElastiCache (Redis): Reads pre-computed or fallback lists [Redis protocol, <50ms]
- Background Worker to Amazon Kinesis: Consumes clickstream events [TCP]
- Background Worker to Amazon RDS (PostgreSQL): Manages promotional rules and audit logs [TCP / SQL]
- Background Worker to Amazon ElastiCache (Redis): Writes merged recommendation payloads [Redis protocol]
]

## Technology Stack
[
- Node.js / Express: Powers the lightweight Recommendation API for high-throughput reads.
- Python / FastAPI: Implements the background worker for scoring, ranking, and merchandising logic.
- Amazon ElastiCache (Redis): Provides sub-50ms cache lookups and multi-region Global Datastores.
- Amazon Kinesis: Ingests real-time shopper clickstream events.
- Amazon RDS (PostgreSQL): Stores promotional overrides and audit logs securely.
]

## Rationale
[Asynchronous pre-computation of recommendations directly to Redis eliminates compute dependencies on the critical request path, guaranteeing sub-50ms lookups. Regional isolation via ElastiCache Global Datastores and in-memory fallbacks ensure high availability and strict adherence to performance NFRs.]