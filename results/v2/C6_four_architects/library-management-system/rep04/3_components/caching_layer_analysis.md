## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals with strict EU data residency constraints. The caching layer optimizes high-speed metadata retrieval and search performance to meet sub-800ms response targets.

## Key Elements
* **Caching Layer**: Redis-based container for high-speed metadata caching.
* **Cache Router Component**: Manages incoming TCP connections and client authentication.
* **In-Memory Store Component**: Handles key-value data storage and LRU eviction policies for item catalogues.
* **Core Services Container**: Java Spring Boot backend for core business logic.
* **Search Container**: Elasticsearch container for item searches.
* **Async Worker Container**: Background workers for cache warming and bulk invalidation.

## Relationships
* **Core Services Container / Search Container -> Cache Router Component**: Uses **RESP (Redis Serialization Protocol)** over **TCP** [Network] for session and metadata caching.
* **Cache Router Component -> In-Memory Store Component**: Uses **RESP Execution Engine** [In-Process] for atomic command processing.
* **Async Worker Container -> In-Memory Store Component**: Uses **RESP** over **TCP** [Network] for background cache warming and batch eviction.

## Technology Stack
* **Redis OSS / Enterprise**: In-memory data store chosen for microsecond-level response times and native single-threaded RESP execution engine.
* **Infrastructure-Level EU Subnets & VPCs**: Ensures EU-only data residency without introducing performance penalties to the caching loop.

## Rationale
The Redis-based caching layer offloads Elasticsearch and PostgreSQL to consistently achieve 99th-percentile search response times under 800ms. Infrastructure-level network boundaries enforce strict EU data residency without adding custom application overhead.