## Overview
[The system is an Insurance Claims Modernization Platform that gradually replaces a 30-year-old mainframe claims system with a modern hybrid cloud architecture while maintaining continuous claims processing.]

## Key Elements
- [Customers, Brokers, Claims Adjusters (Users)]
- [Legacy Mainframe & Active Directory Identity Provider (External Systems)]
- [Frontend SPA (React / TypeScript)]
- [API Management Gateway (Azure API Management)]
- [Backend Service (Modular Monolith .NET Core)]
- [Mainframe Integration Adapter (Azure Functions)]
- [Azure SQL Database, Azure Key Vault, Azure Application Insights]

## Relationships
- [Frontend SPA -> API Management Gateway: Sends API requests via HTTPS/REST with OAuth2 JWT validation]
- [API Management Gateway -> Backend Service: Routes modern traffic via HTTPS over mTLS/VNet]
- [API Management Gateway -> Mainframe Integration Adapter: Routes legacy traffic via HTTPS over mTLS/VNet]
- [API Management Gateway -> Azure Application Insights: Streams telemetry via HTTPS]

## Technology Stack
- [Azure API Management (APM): Managed API gateway for policy routing, rate limiting, and TLS termination, mitigating low cloud experience risks]
- [React / TypeScript: Modern web framework for customer and adjuster interfaces]
- [.NET Core: Backend modular monolith framework ensuring high maintainability]
- [Azure SQL Database: Modern relational data store for migrated claim types]
- [Azure Key Vault: Secure storage for secrets, API keys, and certificates]

## Rationale
- [The hybrid architecture uses Azure API Management for dynamic traffic routing and canary deployments, enabling seamless, risk-free migration of claim types one by one while keeping the legacy mainframe as the system of record.]
- [Managed Azure services reduce operational overhead for a team with low cloud experience while meeting strict performance, security, and fallback requirements.]