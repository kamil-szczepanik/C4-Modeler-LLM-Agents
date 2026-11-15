## Overview
The Library Management System provides cataloging, circulation, and self-service portals for academic and public libraries. The architecture enforces strict EU data residency while maintaining high-performance search capabilities.

## Key Elements
- **Library Patrons & Librarians/Staff**: End users accessing portals via the SPA.
- **Single Page Application (SPA)**: React/TypeScript frontend served via Nginx.
- **API Gateway**: Spring Cloud Gateway handling edge routing, security, and policies.
- **Core Domain Container**: Java/Spring Boot handling circulation and cataloging with PostgreSQL (EU-hosted).
- **Search Container**: Elasticsearch handling catalog queries.
- **Integration Container**: Node.js/TypeScript handling external integrations.
- **Redis Cluster**: In-memory store for rate limiting.

## Relationships
- **SPA -> API Gateway**: Sends user requests over HTTPS/REST.
- **API Gateway -> Core Domain / Search / Integration**: Forwards traffic via gRPC or REST over TLS using mutual TLS (mTLS) within an EU-isolated VPC.
- **API Gateway -> Redis Cluster**: Evaluates traffic quotas and rate limits.

## Technology Stack
- **Spring Cloud Gateway**: Selected for native JVM ecosystem integration, security filters, and circuit breaker support.
- **Redis**: Deployed as an EU-isolated cluster for distributed rate limiting.
- **PostgreSQL & Elasticsearch**: Backend data stores restricted to EU data residency.
- **OpenTelemetry**: Used for distributed tracing and latency tracking to meet SLAs.

## Rationale
The Spring Cloud Gateway architecture centralizes security, rate limiting, and request normalization at the edge. This protects backend services, ensures strict EU compliance, and supports the required <800ms search performance SLA.