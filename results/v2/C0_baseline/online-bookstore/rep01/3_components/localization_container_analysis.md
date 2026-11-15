## Overview
The Online Bookstore Localization Container manages multi-language translations, multi-currency conversions (USD, EUR, GBP), and regional shipping/tax rules for global book buyers. It is deployed on AWS to ensure high availability, low latency, and GDPR/CCPA compliance.

## Key Elements
- Book Buyers (International end-users)
- API Gateway (Node.js / Reverse Proxy)
- Localization Container (Node.js/Express)
- Locale Router & Middleware (Express.js)
- Translation Service Component (i18next)
- Currency Conversion Engine (Node.js/Axios)
- Geo-Resolution Adapter
- Amazon ElastiCache (Redis)
- External Third-Party FX APIs
- AWS Secrets Manager
- AWS ECS on Fargate & App Mesh

## Relationships
- API Gateway -> Locale Router: Requests localization and currency data via gRPC over mTLS using AWS App Mesh
- Currency Conversion Engine -> External Third-Party FX APIs: Fetches exchange rates via HTTPS (TLS 1.3)
- Currency Conversion Engine -> Amazon ElastiCache (Redis): Retrieves cached rates via internal TCP with TLS
- Locale Router -> Translation Service & Geo-Resolution Adapter: Internal component function calls

## Technology Stack
- Node.js & Express.js: Chosen for lightweight, high-throughput asynchronous request handling
- i18next: Selected for sub-millisecond multi-language string resolution
- Amazon ElastiCache (Redis): Used as an in-memory data store for low-latency currency and translation lookups, supporting NFR-06 (<2s page load)
- AWS ECS on Fargate & App Mesh: Provides container orchestration and secure mTLS service mesh routing across multiple regions
- AWS Secrets Manager: Ensures secure injection of third-party API credentials without hardcoding

## Rationale
This architecture uses localized in-memory caching and geo-resolution to minimize latency, protecting the sub-2-second page load requirement for global users. Multi-region ECS deployment with Redis failover guarantees 99.95% uptime and reliable multi-currency checkout during third-party outages.