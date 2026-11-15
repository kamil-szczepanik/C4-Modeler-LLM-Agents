## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-hosted platform while ensuring business continuity. It provides online claim submissions for customers and brokers and a high-performance web workspace for claims adjusters.

## Key Elements
- Web Portal (SPA)
- Adjuster Workspace (Web Application)
- API Gateway / Router (YARP reverse proxy on Azure Container Apps)
  - Dynamic Route Dispatcher
  - Circuit Breaker & Fallback Handler
  - Token Validation Middleware
  - Audit Interceptor
  - Error Translation Middleware
- Claims Core Service (Spring Boot)
- Legacy Mainframe (COBOL/DB2)
- Azure App Configuration
- Azure Front Door with WAF
- Audit & Activity Trail Service

## Relationships
- Web Portal -> API Gateway / Router: Sends API requests [HTTPS / TLS 1.3 / OAuth 2.0 / OIDC]
- Adjuster Workspace -> API Gateway / Router: Sends API requests [HTTPS / TLS 1.3 / OAuth 2.0 / OIDC]
- Dynamic Route Dispatcher -> Claims Core Service: Routes migrated claim traffic [gRPC / HTTPS]
- Dynamic Route Dispatcher -> Legacy Mainframe: Routes unmigrated traffic [HTTPS / mTLS]
- Dynamic Route Dispatcher -> Audit Interceptor: Dispatches routing telemetry [In-process]
- Error Translation Middleware -> Web Portal / Adjuster Workspace: Returns standardized error payloads [HTTPS / RFC 7807]

## Technology Stack
- YARP (Yet Another Reverse Proxy): .NET-native, lightweight, and easily maintainable for a team with low cloud experience.
- Azure App Configuration: Real-time dynamic feature flag management for zero-downtime claim-type routing and rollbacks.
- Azure Front Door & WAF: Perimeter security and global load balancing against DDoS and OWASP Top 10 threats.
- W3C Trace Context: Distributed tracing headers to debug hybrid latency bottlenecks between Azure and on-premise infrastructure.

## Rationale
This architecture uses a YARP-based hybrid gateway to route traffic dynamically, enabling incremental claim migration without extending the mainframe batch window. It isolates complex cloud infrastructure behind simple, manageable .NET components tailored to the team's skillset.