## Overview
This system provides real-time fraud screening for card-not-present payment authorizations within an AWS-hosted infrastructure. It evaluates transactions to return approval decisions while ensuring PCI-DSS compliance and high availability.

## Key Elements
- **Envoy Sidecar Proxy**: Manages mTLS termination, routing, and circuit breaking.
- **Listener & TLS Termination Component**: Handles incoming traffic using BoringSSL.
- **Routing & Load Balancing Component**: Forwards gRPC/HTTP2 traffic to scoring containers.
- **Circuit Breaker & Retry Component**: Provides outlier detection and active health checks.
- **Telemetry & Tracing Component**: Emits metrics and distributed trace headers.

## Relationships
- **API Gateway** sends HTTPS traffic to **Envoy Sidecar Proxy**.
- **Envoy Sidecar Proxy** routes gRPC/HTTP2 traffic to **Scoring Engine** containers.
- **Envoy Sidecar Proxy** exports metrics to **Prometheus** via `/stats/prometheus`.

## Technology Stack
- **Envoy C++**: Chosen for low-latency sidecar proxy operations.
- **BoringSSL**: Utilized for secure TLS termination and mTLS enforcement.
- **HTTP/2 & gRPC**: Selected for low-latency upstream communication with scoring engines.
- **Prometheus**: Used for lightweight metric scraping and observability.

## Rationale
This architecture uses Envoy filters and gRPC pooling to maintain sub-50ms P99 latency while adhering to strict PCI-DSS security boundaries. The design minimizes operational complexity to support a three-engineer team within budget.