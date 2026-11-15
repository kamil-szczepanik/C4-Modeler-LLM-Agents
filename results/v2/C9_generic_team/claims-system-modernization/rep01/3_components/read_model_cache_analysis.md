## Overview
[The system is a hybrid Insurance Claims Modernization platform that gradually replaces a legacy mainframe with a modern Azure-hosted application. Its core purpose is to maintain continuous claims processing while migrating claim types incrementally.]

## Key Elements
* Azure Redis Cache (Read-Model Cache component)
* Repository Abstraction Layer (.NET Core)
* Data Synchronization Worker (.NET Background Worker)
* Azure App Configuration
* Azure Monitor / Application Insights

## Relationships
* Repository Abstraction Layer -> Azure Redis Cache: Read and write claim states securely [TCP / Redis Protocol]
* Data Synchronization Worker -> Azure Redis Cache: Update claim states asynchronously with Optimistic Concurrency Control [Redis MULTI/EXEC]
* Adjuster Web Application -> Repository Abstraction Layer: Serve low-latency claim reads under 2s with Cache-Aside pattern [Internal API]
* Application Insights -> Azure Redis Cache: Track hit/miss ratios, latency, and cache metrics [Telemetry API]

## Technology Stack
* Azure Redis Cache: Provides low-latency in-memory data storage to meet the sub-2s performance requirement (R-05).
* .NET Core Repository Pattern: Encapsulates cache logic and connection management to improve maintainability for a team with limited cloud experience.
* Azure App Configuration: Externalizes cache timeouts, TTL policies, and retry limits for dynamic runtime tuning.
* Testcontainers with Redis: Enables automated integration testing of concurrency and fallback behaviors in CI/CD pipelines.

## Rationale
[This architecture uses a managed caching tier with strict concurrency controls and fallback mechanisms to guarantee data consistency and sub-2s response times. It safely decouples the modern web UI from slow legacy mainframe responses while supporting a seamless, incremental migration.]