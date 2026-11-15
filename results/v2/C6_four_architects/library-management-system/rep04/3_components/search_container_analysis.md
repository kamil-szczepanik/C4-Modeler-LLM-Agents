## Overview
The Library Management System provides catalogue and circulation management for public and academic libraries. This architecture focuses specifically on the Search Container to ensure rapid item retrieval under strict regional constraints.

## Key Elements
* Search API Handler (Java, Spring WebFlux)
* Query Sanitizer & Metrics Interceptor (Middleware)
* Search Query Cache (Redis)
* Search Index Engine (Elasticsearch 8.x)
* Index Management Service (Python sidecar)
* API Gateway
* Search Worker Container

## Relationships
* API Gateway -> Search API Handler: Forwards search queries via `gRPC`
* Search API Handler -> Search Query Cache: Checks cached result sets via `RESP/TCP`
* Search Query Cache -> Search Index Engine: Fallback query on cache miss via `Transport Client / TCP`
* Search Worker Container -> Search Index Engine: Ingests delta updates via `HTTPS/REST`
* Index Management Service -> Search Index Engine: Admin operations via loopback `HTTPS`

## Technology Stack
* Java with Spring WebFlux: Enables non-blocking I/O for low-latency request handling
* Elasticsearch 8.x: Provides high-performance indexing and full-text search with EU node pinning
* Redis: Caches frequent search queries to reduce index load
* Python: Implements sidecar index management operations
* TLS 1.3: Secures all internal transport traffic

## Rationale
The reactive API handler, Redis query cache, and optimized Elasticsearch engine collectively ensure the 99th-percentile search response remains under 800 ms (R-05). Data residency constraints are strictly met by pinning Elasticsearch nodes and management services exclusively to EU infrastructure using TLS 1.3.