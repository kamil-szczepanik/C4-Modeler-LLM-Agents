## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. The system achieves a 99th-percentile search response under 800 ms using an optimized API Gateway architecture.

## Key Elements
- **Library Patron & Librarian / Library Staff**: External human users.
- **Payment Gateway & Digital Content Provider**: External systems.
- **Web Application**: React / TypeScript frontend hosted on an EU CDN.
- **API Gateway Containers (Spring Cloud Gateway)**: Composed of Routing & Load Balancer, Authentication & Authorization Filter, Rate Limiting & Throttling, and Caching & Response Transformation components.
- **Core Domain Service**: Spring Boot / Java backend handling business logic.
- **Search Service**: Elasticsearch / OpenSearch for fast catalogue queries.
- **Redis Instances**: EU-deployed, AES-256 encrypted cache and rate limiter backends.
- **Async Event Bus**: Managed Kafka.
- **Database**: PostgreSQL.

## Relationships
- Web Application -> API Gateway: Makes API requests [HTTPS / TLS 1.3].
- API Gateway -> Core Domain Service: Routes requests and validates roles [gRPC with mTLS].
- API Gateway -> Search Service: Routes search queries [gRPC with mTLS].
- Routing Component -> Redis Cache: Evaluates cached responses [Redis RESP / TLS].

## Technology Stack
- **Spring Cloud Gateway & Spring Security**: Selected for native OAuth2 token validation, resilient circuit breaking, and Java ecosystem consistency.
- **Redis**: Deployed in EU-only regions with AES-256 encryption at rest for rate limiting and response caching.
- **gRPC with mTLS**: Protocol for secure, high-performance internal microservice communication.
- **Prometheus & Grafana/Tempo**: Observability stack utilizing W3C Trace Context headers.
- **Kubernetes**: Multi-zone deployment platform with HPA and PDB.

## Rationale
This architecture meets EU-only data residency requirements while ensuring high performance through edge caching and gRPC routing. Native Spring Security integration at the gateway provides robust zero-trust security without sacrificing the strict 800ms search latency threshold.