## Overview
[The system modernizes a regional insurer's 30-year-old mainframe claims platform through a hybrid cloud architecture. The API Gateway / BFF container handles secure ingress, protocol translation, and performance optimization for web and mobile frontends.]

## Key Elements
- Azure API Management: External ingress and rate limiting
- Customer BFF: Node.js / Express service for Web Portal
- Adjuster BFF: Node.js / Express service for Adjuster Web Application
- BFF Response Cache: Redis caching coordinator for sub-2s response times
- Token Exchange Middleware: Node.js Active Directory JWT validation
- Circuit Breaker Proxy: Opossum-based resilience layer
- API Composition & Transformation Engine: Payload shaping orchestrator
- API Metrics & Telemetry Exporter: OpenTelemetry SDK

## Relationships
- Web Portal -> Azure API Management: Public HTTPS traffic [HTTPS]
- Adjuster Web Application -> Azure API Management: Public HTTPS traffic [HTTPS]
- Azure API Management -> Customer BFF: Routes public traffic [HTTPS]
- Azure API Management -> Adjuster BFF: Routes internal adjuster traffic [HTTPS]
- Token Exchange Middleware -> Customer & Adjuster BFFs: Passes enriched security context [In-Memory]
- Adjuster BFF -> BFF Response Cache: Queries cached claims data [TCP/Redis]
- Customer & Adjuster BFFs -> Claim Routing Service: Forwards domain commands/queries [gRPC]
- All BFF Internal Components -> API Metrics & Telemetry Exporter: Emits telemetry metrics [In-Memory]
- API Metrics & Telemetry Exporter -> Observability & Audit Container: Exports traces and metrics [OpenTelemetry/HTTPS]

## Technology Stack
- Azure API Management: Offloads enterprise-grade security and rate limiting from application code
- Node.js / Express: Efficient I/O-bound request aggregation and BFF implementation
- Redis: Read-through caching to meet strict sub-2s adjuster screen load constraints against 5s mainframe responses
- Opossum: Code-level circuit breaking to prevent cascading failures from legacy backend latency
- OpenTelemetry: Vendor-agnostic telemetry collection for hybrid cloud latency tracking

## Rationale
[This architecture isolates legacy mainframe latency through aggressive Redis caching and circuit breaking within the BFF layer. Centralized API management and token middleware enforce robust Active Directory security while keeping downstream domain services maintainable.]