## Overview
The Envoy Service Mesh Container acts as the secure, high-performance data plane for the Clinic Management System, managing intra-service traffic routing, zero-trust security, and observability. It ensures HIPAA/GDPR compliance and 99.99% availability across hybrid Kubernetes and cloud environments.

## Key Elements
- Envoy Listener Subsystem
- xDS Dynamic Configuration Client
- RBAC & Authorization Filter Engine
- Rate Limit Filter Component
- Health Checking & Outlier Detection Component
- Access Logging Service (ALS)
- Envoy Tracing Filter Component
- Envoy WASM Extension Host
- Envoy Cluster Manager Component
- Envoy Circuit Breaker Component
- Envoy Ext_Authz Filter Component
- Envoy DNS Resolver Component

## Relationships
- Envoy Listener establishes bi-directional mTLS 1.3 tunnels over TCP with upstream and downstream microservices.
- RBAC Filter communicates locally with the Tenant Context & Authorization Proxy via Unix domain sockets.
- Rate Limit Filter connects asynchronously via gRPC with a Redis caching tier.
- Access Logging Service streams JSON audit telemetry via gRPC to the Observability Collector Container.
- Tracing Filter exports OpenTelemetry data via gRPC over Unix domain sockets to the Observability Collector.
- Ext_Authz Filter maintains persistent HTTP/2 gRPC connections with the Authorization Proxy.
- DNS Resolver interacts with the Cluster Manager for endpoint resolution.

## Technology Stack
- Envoy C++ Core: High-performance data plane foundation for low latency.
- BoringSSL: Provides strict TLS 1.3 cryptographic routines for secure communication.
- gRPC: Used for efficient xDS synchronization, rate limiting, and telemetry streaming.
- OpenTelemetry: Native integration for distributed tracing across clinical transactions.
- WasmEdge & Rust: Executes lightweight WebAssembly plugins for HIPAA payload inspection.
- c-ares DNS: Handles asynchronous DNS resolution and TTL caching.

## Rationale
This architecture guarantees sub-millisecond data plane overhead and strict zero-trust isolation required for sensitive clinical workflows. It provides the fault tolerance and telemetry tracing necessary to maintain 99.99% availability and full regulatory audit compliance.