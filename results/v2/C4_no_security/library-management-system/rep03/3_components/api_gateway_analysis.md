## Overview
The API Gateway manages secure edge traffic for the Library Management System, ensuring strict EU data residency and low-latency self-service portals. It centralizes routing, authentication, and compliance for public and academic library patrons.

## Key Elements
- **Kong API Gateway**: Core edge container handling ingress traffic
- **TLS Termination & Geo-Filter Plugin**: Inspects client IP geolocation at the edge
- **JWT Authentication Plugin (Kong OIDC/JWT)**: Validates Identity Provider (IdP) tokens
- **Rate Limiting & Analytics Plugin**: Enforces quotas and tiered API consumption
- **Upstream Load Balancer & Router**: Directs traffic to backend services
- **OpenTelemetry Plugin**: Injects distributed tracing headers
- **Audit Logging Plugin**: Captures compliance and administrative logs
- **HashiCorp Vault / Kubernetes Secrets**: Manages dynamic credentials

## Relationships
- **Web App (SPA)** -> **Kong API Gateway**: Communicates via REST/GraphQL [HTTPS]
- **Kong API Gateway** -> **Catalogue & Search Container**: Routes internal traffic [gRPC over HTTP/2]
- **Kong API Gateway** -> **Circulation & Core Container**: Routes internal traffic [gRPC]
- **Kong API Gateway** -> **Audit Log Sink**: Streams compliance logs asynchronously [HTTPS]

## Technology Stack
- **Kong API Gateway**: Edge container platform for low-latency routing and modular plugins
- **OpenTelemetry**: Distributed tracing protocol (W3C Trace Context) to maintain <800ms search latency
- **gRPC / HTTP/2**: Internal communication protocol for high-performance backend routing
- **HashiCorp Vault / Kubernetes**: Secret management and auto-scaling infrastructure

## Rationale
This architecture satisfies EU data residency constraints by enforcing edge geo-filtering for all traffic. It guarantees high performance and 99.99% availability through Anycast load balancing, gRPC routing, and distributed tracing.