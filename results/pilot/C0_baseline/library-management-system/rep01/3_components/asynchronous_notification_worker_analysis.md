## Overview
- The Asynchronous Notification Worker is a Python-based container component responsible for processing and dispatching automated alerts to library patrons and staff.
- It ensures reliable multi-channel communications while enforcing strict EU data residency and zero-PII-leakage constraints.

## Key Elements
- Asynchronous Notification Worker (Python container)
- Queue Consumer Component (`asyncio`, HMAC-SHA256 validation)
- Template Engine Component (Jinja2)
- Gateway Dispatcher Component (TLS 1.3, circuit breakers)
- Redis Cache Tier (Redis, RESP3 deduplication/rate-limiting)
- Core Circulation & Catalog Service (Java/Spring Boot)
- External SMTP Relays and SMS Gateways (EU-region)

## Relationships
- Core Circulation & Catalog Service -> Asynchronous Notification Worker: Triggers events via mTLS [gRPC over TLS] with HMAC-SHA256 payload signing
- Asynchronous Notification Worker -> Redis Cache Tier: Deduplicates messages and manages retry states [RESP3]
- Asynchronous Notification Worker -> External SMTP Relays / SMS Gateways: Dispatches messages [TLS 1.3 with certificate pinning]

## Technology Stack
- Python with `asyncio`: High-throughput asynchronous event loop processing
- Jinja2: Ephemeral memory template rendering with zero PII logging
- Redis: Rate-limiting, deduplication, and durable retry state machine
- Kubernetes: Stateless container orchestration with HPA and egress network policies
- OpenTelemetry: Distributed tracing with enforced PII scrubbing in span attributes

## Rationale
- Decouples background communications from core circulation workflows to maintain sub-800ms search performance and high availability.
- Enforces rigorous cryptographic verification, egress restrictions, and ephemeral memory handling to comply with EU data residency mandates.