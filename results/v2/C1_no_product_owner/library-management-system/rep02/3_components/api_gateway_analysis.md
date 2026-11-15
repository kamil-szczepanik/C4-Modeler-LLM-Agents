## Overview
The Library Management System is a EU-compliant solution for public and academic libraries to catalogue items and manage circulation. The API Gateway container ensures secure ingress, traffic management, and low-latency performance.

## Key Elements
- **API Gateway Container**: Spring Cloud Gateway / Envoy deployed across 3 availability zones.
- **Ingress Listener & TLS Termination Component**: Handles inbound HTTPS (TLS 1.3) and IP geolocation.
- **Security & Authentication Filter**: Validates OAuth2/OIDC JWTs locally using Spring Cloud Security.
- **Rate Limiter Component**: Coordinates rate-limiting via Redis Cache.
- **Routing & Resilience Mediator**: Applies Resilience4j circuit breakers.
- **gRPC Upstream Client**: Forwards requests downstream.
- **Redis Cache**: Stores rate-limiting counters and JWT blacklists.
- **Core Domain, Search, & Notification Services**: Internal Java and Node.js microservices.

## Relationships
- **Web Application -> API Gateway**: Makes API requests [HTTPS/REST]
- **Identity Provider -> API Gateway**: Issues and validates OIDC tokens [HTTPS/OIDC]
- **API Gateway -> Redis Cache**: Stores rate-limiting counters and revoked tokens [TCP/RESP]
- **API Gateway -> Core Domain / Search / Notification Services**: Routes internal service requests [gRPC over mTLS]

## Technology Stack
- **Spring Cloud Gateway**: Selected for native Spring Boot ecosystem integration and perimeter OIDC validation.
- **Redis**: Provides low-latency caching for rate-limiting and JWT blacklists within the EU region.
- **Resilience4j**: Implements circuit breakers to prevent cascading failures.
- **gRPC over mTLS**: Secures east-west service-to-service communication with propagated metadata.

## Rationale
This architecture ensures strict EU-only data residency and meets the <800ms search latency requirement through multi-AZ deployment, localized Redis caching, and efficient gRPC routing. Perimeter security offloads authentication while internal mTLS and circuit breakers guarantee fault tolerance.