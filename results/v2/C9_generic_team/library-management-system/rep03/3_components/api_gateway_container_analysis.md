## Overview
The Library Management System is a comprehensive solution for public and academic libraries designed to catalogue items, manage circulation, and provide self-service portals. It ensures strict EU-only data residency and maintains a 99th-percentile search response time of under 800ms.

## Key Elements
- Library Users and Administrators
- Client-Side Application Container (SPA / Mobile App)
- API Gateway Container (Reverse Proxy / API Gateway)
- Core Catalog/Circulation Service Container (Microservice)
- Search Engine Container (Dedicated Indexing Engine)
- Caching Container (Redis)
- Message Broker Container
- Background Worker Container
- Configuration and Secrets Management Container
- Telemetry Sidecar/Agent Container
- External Identity Providers and Third-Party Hardware Interfaces

## Relationships
- Client-Side Application Container -> API Gateway Container via HTTPS/TLS termination [HTTPS/TLS]
- API Gateway Container -> Core Catalog/Circulation Service Container via internal routing [gRPC]
- API Gateway Container -> Search Engine Container via search routing [gRPC]
- Third-Party Hardware Interfaces -> API Gateway Container via hardware integration [Local Drivers/HTTP]
- Inter-Library Loan Networks -> API Gateway Container via state synchronization [Bi-directional APIs]

## Technology Stack
- **API Gateway Layer:** Modular, plugin-based/middleware architecture for cross-cutting concerns.
- **Internal Communication:** gRPC for low-latency communication to Core Catalog and Search Engine to meet the <800ms search performance requirement (R-05).
- **Edge Validation & Contracts:** OpenAPI/Swagger for strict API schema validation at the gateway edge.
- **Error Handling & Tracing:** RFC 7807 Problem Details for standardized error formats and W3C Trace Context propagation for distributed tracing.
- **Resilience & Caching:** Redis for stale-while-revalidate fallback caching, rate limiting, and circuit breaking.
- **Observability & Compliance:** Prometheus format metrics exposition and PII-redacted access logging routed to EU-hosted observability infrastructure.

## Rationale
This architecture uses a high-performance gRPC communication fabric and edge-based schema validation to meet the strict <800ms search performance requirement (R-05). It integrates middleware-based security, PII redaction, and declarative routing to strictly satisfy EU-only data residency constraints.