## Overview
[Modern Claims Platform] gradually replaces a 30-year-old mainframe claims system using a hybrid cloud architecture. The API Gateway / BFF securely routes traffic, manages authentication, and orchestrates phased claim migrations.

## Key Elements
- API Gateway / BFF (.NET Core)
- Routing & Proxy Component (YARP)
- Authentication & Authorization Middleware
- Feature Routing & Orchestration Component with local fallback cache
- Context Propagation Middleware
- Rate Limiting & Resilience Component (Polly)
- Azure WAF and Azure Managed Identities

## Relationships
- Claims Web Application -> API Gateway / BFF: HTTPS / JSON (OIDC/JWT)
- API Gateway / BFF -> Claims Processing Service & Integration Layer: gRPC (mTLS, TLS 1.3) with OpenTelemetry trace contexts and metadata headers
- API Gateway / BFF -> Configuration & Feature Store: HTTPS / gRPC with local fallback cache

## Technology Stack
- .NET Core: Chosen for framework consistency and team familiarity despite limited cloud experience
- YARP (Yet Another Reverse Proxy): High-performance routing, load balancing, and canary rollouts
- Azure App Configuration: Dynamic feature flagging for step-by-step claim type migration
- OpenTelemetry & Azure Monitor: Distributed tracing across the hybrid cloud boundary
- Azure Managed Identities & Key Vault: Secretless infrastructure and secure credential management

## Rationale
This architecture isolates the complex hybrid migration behind a resilient, secure API gateway that protects legacy constraints while ensuring zero claim loss. Local caching and fallback mechanisms guarantee business continuity during cloud service outages.