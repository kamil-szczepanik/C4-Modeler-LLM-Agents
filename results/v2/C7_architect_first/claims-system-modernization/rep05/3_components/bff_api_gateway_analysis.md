## Overview
A modern hybrid platform progressively replaces a legacy mainframe insurance claims system. It ensures business continuity and sub-2-second adjuster response times over a three-year migration window.

## Key Elements
* API Gateway Proxy (Azure API Management)
* Customer BFF & Adjuster BFF (Java Spring Boot)
* Dynamic Routing & Feature Dispatcher 
* Circuit Breaker & Fallback Manager (Resilience4j)
* Azure Redis Cache
* Insurer's Active Directory

## Relationships
* Web Frontend -> API Gateway Proxy: Proxies client traffic [HTTPS / REST]
* API Gateway Proxy -> Customer BFF & Adjuster BFF: Forwards authenticated routes [mTLS / HTTP]
* Adjuster BFF -> Azure Redis Cache: Reads UI state and cached data [Redis Protocol / TLS]
* Adjuster BFF -> Claims Processing Service & Integration & ACL: Forwards claim queries [HTTPS / REST]

## Technology Stack
* Java Spring Boot: Standardized runtime for BFFs to mitigate the team's low cloud experience
* Azure API Management: Handles edge routing, OAuth2/OIDC validation, and OpenAPI schema enforcement
* Resilience4j: Implements circuit breaking and fallback logic for slow mainframe responses
* Azure App Configuration: Stores dynamic routing rules for rapid claim-type rollbacks
* OpenTelemetry: Enforces distributed tracing with PII redaction across hybrid boundaries

## Rationale
Standardizing on Java Spring Boot and Resilience4j successfully bridges the team's cloud skill gap while guaranteeing sub-2-second performance despite high mainframe latencies. Externalized feature flags ensure compliance with the one-day rollback constraint during the hybrid migration.