## Overview
The system is a modern hybrid insurance claims platform that gradually replaces a legacy mainframe system. Its core purpose is to enable online claim submission and adjuster workflows while maintaining seamless data consistency during a phased migration.

## Key Elements
- **API Gateway**: Azure API Management
- **BFF Orchestrator**: Node.js / Express
- **Edge Security Proxy**: Node.js / TypeScript
- **Edge Configuration Component**: Node.js with Redis Cache
- **Frontend**: React via Azure Static Web Apps
- **Application Tier**: Azure Container Apps (Java/Spring Boot, Python/C# Azure Functions)
- **Integration Tier**: Azure Service Bus and Azure Relay

## Relationships
- **Frontend** -> **API Gateway**: `HTTPS / REST / OIDC (Entra ID)`
- **API Gateway** -> **BFF Orchestrator**: `HTTP / JSON`
- **BFF Orchestrator** -> **Edge Configuration Component**: `Redis Cache lookup`
- **BFF Orchestrator** -> **Edge Security Proxy**: `gRPC`
- **Edge Security Proxy** -> **Integration Tier (Azure Relay)**: `HTTPS / mTLS`
- **BFF Orchestrator** -> **Application Tier**: `gRPC`

## Technology Stack
- **Azure API Management**: For rate limiting, TLS termination, and JWT validation against Active Directory.
- **Node.js / TypeScript**: For high-performance, asynchronous BFF and security proxy implementation.
- **Redis Cache**: For sub-millisecond dynamic claim-type routing lookups supporting instant fallbacks.
- **gRPC**: For low-latency internal communication between edge and application tiers.
- **Azure Relay with mTLS**: For secure, encrypted hybrid transit to the on-premise mainframe bridge.

## Rationale
This architecture hides high legacy mainframe latency behind an optimized BFF and caching layer to achieve required adjuster screen performance. It also provides dynamic routing to safely support gradual claim type migration and rapid one-day fallback switches.