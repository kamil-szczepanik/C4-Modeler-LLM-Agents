## Overview
[The Routing / Feature Flag Container manages dynamic request routing and feature flag evaluations to support the gradual migration of insurance claim types. It ensures high-performance, resilient traffic splitting between the legacy mainframe and the modern platform.]

## Key Elements
- Routing / Feature Flag Container (Azure Container Apps)
- In-memory LRU cache backed by Redis
- Azure App Configuration store
- Observability & Logging Container (Azure Application Insights)
- Anti-Corruption Layer (ACL) Container

## Relationships
- API Gateway Container -> Routing / Feature Flag Container: Forwards incoming traffic via internal REST/gRPC
- Routing / Feature Flag Container -> Modular Monolith Container: Routes live traffic via internal REST/gRPC
- Routing / Feature Flag Container -> Azure App Configuration: Fetches dynamic routing rules
- Routing / Feature Flag Container -> Redis: Backs local in-memory flag cache
- Routing / Feature Flag Container -> Observability Container: Emits asynchronous audit logs and telemetry via OpenTelemetry

## Technology Stack
- Azure Container Apps: Hosts the routing service for scalability and simplified container management
- OpenFeature standard: Adopts an open specification for feature flag and routing evaluations to avoid proprietary lock-in
- Redis and In-Memory LRU Cache: Caches evaluated flags locally to achieve sub-millisecond evaluation latencies
- Azure App Configuration: Provides a declarative configuration schema for managing migration flags and fast rollbacks
- Azure Application Insights: Collects structured telemetry, evaluation latency metrics, and audit logs

## Rationale
[Separating routing and feature flag logic into a dedicated container decouples migration switching from core application code, ensuring rapid one-day rollbacks. Caching evaluations and implementing strict timeouts protect system performance and meet the sub-2-second adjuster screen requirement despite limited team cloud experience.]