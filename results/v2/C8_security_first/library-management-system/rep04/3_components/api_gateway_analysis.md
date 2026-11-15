## Overview
[The system is a Library Management System providing cataloging, circulation, and self-service portals for public and academic libraries. Its core purpose is to deliver secure, highly performant access while strictly enforcing EU data residency constraints.]

## Key Elements
- Library Patron
- Library Staff / Librarian
- API Gateway (Kong / NGINX, OAuth 2.0 / OIDC, Edge Router, Auth Filter, Rate Limiter, Telemetry Exporter, Schema Validator)
- Search & Catalog Service (Java / Spring Boot, Elasticsearch)
- Core Circulation Service (Node.js / Go, PostgreSQL)
- Analytics Service (Python / FastAPI, ClickHouse)
- Redis Cluster (High-availability caching and rate-limiting counters)
- Audit Logging Sidecar (Fluentbit / Vector)
- EU Cloud Provider's HSM

## Relationships
- Library Patron -> API Gateway: Accesses self-service portals [HTTPS / TLS 1.3]
- Library Staff / Librarian -> API Gateway: Manages cataloging and circulation [HTTPS / TLS 1.3 with OAuth 2.0 / OIDC]
- API Gateway -> Search & Catalog Service: Routes catalog queries [Internal mTLS and gRPC]
- API Gateway -> Core Circulation Service: Routes circulation operations [Internal mTLS and gRPC]
- API Gateway -> Analytics Service: Publishes telemetry metrics [Internal mTLS and gRPC]
- API Gateway -> Redis Cluster: Manages rate-limiting and token caching [TCP]
- API Gateway -> Audit Logging Sidecar: Forwards security events [Local IPC / Unix Socket]
- API Gateway -> EU Cloud Provider's HSM: Fetches TLS certificates and OIDC keys [gRPC / mTLS]

## Technology Stack
- Kong / NGINX: Selected for edge routing, WAF, and geo-blocking to enforce EU data residency.
- OAuth 2.0 / OIDC: Provides secure authentication and SSO for patrons and staff.
- Redis Cluster: Enables stateless gateway scaling and high-availability rate limiting.
- gRPC & mTLS: Ensures low-latency (< 800 ms search SLA) and secure internal communication.
- EU Cloud Provider's HSM: Secures TLS certificates and token validation keys.

## Rationale
[This architecture utilizes a stateless API Gateway backed by Redis and HSM to meet stringent EU data residency and sub-800ms search performance requirements. Decoupled internal services communicate via gRPC/mTLS, ensuring both system security and horizontal scalability under heavy patron traffic.]