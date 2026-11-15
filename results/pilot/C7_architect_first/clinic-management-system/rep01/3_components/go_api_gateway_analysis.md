## Overview
The Go API Gateway provides high-performance request routing, zero-trust security enforcement, and rate limiting for the Clinic Management System. It secures and optimizes traffic between external clients and internal Java Spring Boot microservices across a hybrid cloud infrastructure.

## Key Elements
- Go API Gateway: Inbound request router and security perimeter built with Go.
- HTTP Router: `gorilla/mux` for high-speed URL pattern matching.
- Auth Middleware: JWT validator enforcing HIPAA/GDPR access controls.
- Rate Limiter & Cacher: Redis Enterprise (`go-redis`) and local `ristretto` cache with 60-second TTL.
- gRPC Client Pool: HTTP/2 client with `sony/gopher-breaker` circuit breaker and mTLS via SPIFFE/SPIRE.
- Observability: Prometheus metrics exporter and OpenTelemetry distributed tracer.

## Relationships
- Next.js Single Page Application -> Go API Gateway: Routes inbound client traffic [HTTPS/JSON, TLS 1.3]
- Go API Gateway -> Java Spring Boot Microservices: Forwards internal requests [gRPC, mTLS]
- Go API Gateway -> Redis Enterprise: Throttling and cache invalidation [TCP/Redis Protocol]
- Go API Gateway -> Identity Provider: Cryptographic signature validation [HTTPS]

## Technology Stack
- Go: Chosen for high-throughput concurrency and low memory overhead.
- Gorilla Mux (`gorilla/mux`): Provides fast, expressive URL routing.
- Redis Enterprise & Ristretto: Delivers distributed multi-tenant rate limiting and low-latency local caching.
- gRPC / Protocol Buffers: Ensures low-latency, strongly-typed internal service communication.
- OpenTelemetry & Prometheus: Enables comprehensive distributed tracing and real-time metric collection.

## Rationale
This architecture ensures 99.99% availability and sub-second performance through efficient connection pooling, circuit breaking, and local caching. It rigorously satisfies HIPAA and GDPR mandates by enforcing strict JWT authentication, mTLS, and secure audit logging at the gateway perimeter.