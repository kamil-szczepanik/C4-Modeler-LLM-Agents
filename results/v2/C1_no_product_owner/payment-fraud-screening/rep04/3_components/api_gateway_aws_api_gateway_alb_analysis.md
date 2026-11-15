## Overview
Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for a mid-size payment processor and manages analyst reviews. It achieves sub-50ms latency at 3,000 TPS under PCI-DSS constraints.

## Key Elements
- Payment Gateway / Core Ledger
- AWS Application Load Balancer (ALB) with AWS WAF
- Envoy Sidecar Proxy
- Scoring Engine (Go)
- Case Management (Node.js / Spring Boot)
- Model Registry (Python / MLflow / Amazon S3)
- Redis / Amazon ElastiCache
- Aurora PostgreSQL (Amazon Aurora PostgreSQL)
- Amazon MSK / Kafka
- Fraud Analyst

## Relationships
- Payment Gateway / Core Ledger -> AWS ALB: Sends payment authorizations via HTTPS/REST (3,000 TPS)
- AWS ALB -> Envoy Sidecar Proxy: Forwards traffic via TLS 1.3 and gRPC over HTTP/2
- Envoy Sidecar Proxy -> Scoring Engine: Enforces internal mTLS and routes requests
- Scoring Engine -> Aurora PostgreSQL: Reads/writes audit logs and rules
- Scoring Engine -> Redis / Amazon ElastiCache: Fetches low-latency features

## Technology Stack
- AWS Application Load Balancer: Edge routing and TLS 1.3 termination
- AWS WAF: L7 DDoS and injection protection
- Envoy Sidecar Proxy: Zero-trust service mesh mTLS enforcement
- Go: High-performance low-latency scoring execution
- Amazon Aurora PostgreSQL: Tamper-evident 7-year audit storage
- Amazon ElastiCache Redis: Sub-millisecond feature caching

## Rationale
AWS ALB and Go meet the strict <50ms P99 latency and 3,000 TPS targets within budget. Envoy and Aurora PostgreSQL ensure PCI-DSS compliance and 7-year auditability.