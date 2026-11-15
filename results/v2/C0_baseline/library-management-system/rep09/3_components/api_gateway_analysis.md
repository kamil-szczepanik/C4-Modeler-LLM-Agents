## Overview
The API Gateway component (Kong) acts as the single perimeter enforcement point for the Library Management System. It routes, secures, and optimizes traffic while strictly enforcing EU data residency constraints.

## Key Elements
- **API Gateway (Kong):** Perimeter proxy utilizing Lua scripts, Nginx core, and plugins.
- **Routing & Dispatcher Component:** Handles TLS termination, internal mTLS, and gRPC/HTTPS dispatch.
- **Authentication & Authorization Filter:** Validates OIDC tokens from the EU Identity Provider.
- **Claims Transformation Component:** Strips bearer tokens and injects signed internal headers.
- **Rate Limiting & Caching Component:** Redis-backed engine enforcing tiered limits and search caching.
- **WAF & Threat Protection Plugin:** Mitigates OWASP Top 10 injection risks.
- **Fluentbit Sidecar:** Streams logs asynchronously to the Centralized Log & Metrics Aggregator.

## Relationships
- *External Clients* -> *API Gateway*: Sends encrypted traffic via TLS 1.3.
- *API Gateway* -> *Redis Cache Component*: Stores and retrieves search results for low-latency access.
- *API Gateway* -> *Core Services Container*: Forwards requests with cryptographically signed claims [mTLS via gRPC/HTTPS].
- *API Gateway* -> *Centralized Log & Metrics Aggregator*: Streams access, security audit, and W3C trace-context logs [TLS via Fluentbit].

## Technology Stack
- **Kong API Gateway:** Chosen for high performance, extensibility via Lua, and robust plugin ecosystem.
- **Redis:** Selected as an in-memory datastore for low-latency search result caching and rate-limiting.
- **gRPC / HTTPS:** Employed for efficient, secure internal communication protocols.
- **TLS 1.3 / mTLS:** Mandated with forward-secret ciphers to satisfy EU security standards and data residency.
- **Fluentbit:** Utilized for lightweight, asynchronous log forwarding without local disk-fill risks.

## Rationale
This architecture uses an optimized Kong-based API Gateway with Redis caching and tiered rate-limiting to guarantee the 99th-percentile search response time remains under 800 ms. It enforces rigorous EU data residency and security constraints through strict mTLS, claims transformation, and decentralized log streaming.