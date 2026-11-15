## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture enforces strict EU-only data residency and high-performance requirements.

## Key Elements
* API Gateway: Nginx / Envoy deployed on Kubernetes with Pod Disruption Budget
* Edge Components: Routing & Tenant Resolver, Rate Limiter Filter, Authentication/OAuth2 Proxy, Versioning & Transformation Filter
* Supporting Services: Redis Cache (in-memory rate limiting), EU Identity Provider, Core Services API (Node.js / NestJS), Centralized SIEM / Monitoring Platform

## Relationships
* Web Application (SPA) -> API Gateway: Sends API requests with JWT [HTTPS]
* API Gateway -> Core Services API: Forwards routed requests with W3C Trace Context [REST/gRPC]
* API Gateway -> Redis Cache: Queries rate limit counters [TCP/RESP]
* API Gateway -> Centralized SIEM / Monitoring Platform: Exports Prometheus metrics and access logs [HTTPS/Prometheus scrape]

## Technology Stack
* Nginx / Envoy: Perimeter routing, TLS 1.3 termination, and edge security for WAF protection
* Redis: Sliding-window rate limiting within the EU cluster to maintain data residency
* Kubernetes: Zero-downtime deployments, hot-reloads, and multi-zone resilience

## Rationale
The API Gateway centralizes security, tenant routing, rate limiting, and auth offloading at the perimeter to protect core services. This ensures compliance with EU data residency and supports high-performance self-service portals.