## Overview
[System screens card-not-present payment authorizations for fraud in real-time and provides case management for fraud analysts. The architecture ensures low-latency scoring, strict auditability, and PCI-DSS compliance on AWS.]

## Key Elements
- Payment Gateway / Core Ledger (External System)
- AWS WAF (Security Service)
- API Gateway / Envoy (Container / Reverse Proxy with internal components: Listener & TLS Terminator, Path-Based Router, `ext_authz`, Redis Rate Limiter, Circuit Breaker, Access Logger)
- Fraud Scoring Engine (Container / Go gRPC service)
- Case Management Backend (Container / Java Spring Boot)
- Redis Cluster / Amazon ElastiCache (Cache / Rate Limiting)
- Amazon CloudWatch (Observability)

## Relationships
- Payment Gateway / Core Ledger -> AWS WAF: Submits payment authorizations [HTTPS/TLS]
- AWS WAF -> API Gateway / Envoy: Inspects and forwards filtered traffic [HTTPS/TLS]
- API Gateway / Envoy -> Fraud Scoring Engine: Invokes real-time fraud screening [gRPC over HTTP/2]
- API Gateway / Envoy -> Case Management Backend: Routes management requests [HTTPS/JSON]
- API Gateway / Envoy -> Redis Cluster / Amazon ElastiCache: Checks rate limits [Redis RESP / TCP]
- API Gateway / Envoy -> Amazon CloudWatch: Streams structured access logs and metrics [AWS API / HTTPS]

## Technology Stack
- Envoy: Edge routing, TLS termination, and circuit breaking for high performance
- gRPC over HTTP/2: Low-latency inter-service communication for scoring
- Amazon ElastiCache (Redis): High-speed rate limiting and quota enforcement
- AWS WAF: Layer 7 security perimeter defense for PCI-DSS compliance
- Amazon CloudWatch: Managed logging and metrics aggregation

## Rationale
[This architecture utilizes managed AWS services and lightweight Envoy patterns to meet sub-50ms P99 latency and fail-open availability requirements. It minimizes operational overhead for a 3-engineer team while strictly enforcing PCI-DSS Level 1 compliance and budget constraints.]