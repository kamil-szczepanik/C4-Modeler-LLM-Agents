## Overview
The Feature Flag / Routing Service dynamically directs claim traffic between a modern Azure platform and an on-premise mainframe. It ensures seamless incremental migration and rapid rollbacks for the Insurance Claims Modernization system.

## Key Elements
* Routing Engine Component (.NET Core)
* Configuration Cache Component (Azure App Configuration SDK with local JSON fallback)
* Audit & Telemetry Component (.NET Core / Application Insights)
* Circuit Breaker Component (.NET Polly)

## Relationships
* Claims API Gateway / BFF -> Routing Engine: Invokes routing via gRPC/HTTPS
* Routing Engine -> Configuration Cache: Reads dynamic rules via in-memory lookup
* Routing Engine -> Audit & Telemetry Component: Emits telemetry asynchronously via .NET Channel/Queue
* Routing Engine -> Core Claims Service / Integration & Sync Service: Directs claim traffic via gRPC/HTTPS
* Circuit Breaker -> Legacy Mainframe System: Reroutes traffic on failure via HTTPS

## Technology Stack
* .NET Core: Ensures team alignment and high-performance execution.
* Azure App Configuration with local JSON fallback: Guarantees fast flag evaluation and offline resilience.
* .NET Polly: Provides automated circuit breaking and failover.
* Application Insights: Tracks routing audit trails and telemetry.

## Rationale
This component architecture enforces the 1-day rollback and zero-data-loss constraints by decoupling routing logic from business services. It mitigates cloud inexperience and latency risks through robust local caching and automated circuit breaking.