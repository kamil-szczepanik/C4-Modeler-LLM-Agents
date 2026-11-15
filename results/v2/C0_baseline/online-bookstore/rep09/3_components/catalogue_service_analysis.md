## Overview
The Catalogue Service is a core container of the Online Bookstore that manages product browsing, fast keyword searches, and multi-currency pricing. It ensures high performance, regional availability, and localized shopping experiences for 1M MAU.

## Key Elements
- Search & Filter Component (Node.js / Express)
- Pricing & Localization Component (Node.js / Express)
- Amazon OpenSearch
- Amazon ElastiCache (Redis)
- Tax & Localization API

## Relationships
- API Gateway -> Search & Filter Component: Routes catalogue and search requests [mTLS, gRPC]
- Search & Filter Component -> Amazon OpenSearch: Performs fast keyword lookups and queries [Internal query protocol]
- Search & Filter Component -> Pricing & Localization Component: Injects localized pricing into payloads [In-memory / Function call]
- Pricing & Localization Component -> Amazon ElastiCache (Redis): Reads cached FX rates [TCP]
- Pricing & Localization Component -> Tax & Localization API: Fetches real-time FX rates [HTTPS / REST, asynchronous background sync]

## Technology Stack
- Node.js & Express: Chosen for lightweight, high-concurrency handling of search and pricing logic.
- Amazon OpenSearch: Enables fast, scalable keyword searching and DSL query execution.
- Amazon ElastiCache (Redis): Provides low-latency caching for multi-currency pricing with cross-region global datastores.
- AWS ECS (Fargate): Containerizes the service for horizontal auto-scaling and zero-downtime deployments.

## Rationale
This architecture achieves sub-2-second page loads and 99.95% uptime by decoupling real-time search from asynchronous multi-currency updates. Caching FX rates in Redis with a USD fallback protects availability against external API degradation.