## Overview
[System: Insurance Claims Modernization]
[Core Purpose: Gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern Azure cloud platform while maintaining uninterrupted business operations.]

## Key Elements
- Users: Customers, Brokers, Claims Adjusters, External Active Directory
- Systems: Legacy Mainframe Claims System, Modern Claims Platform
- Containers: API Gateway / Edge (Azure API Management), Claims Web App (React), Claims Core Service (Java / Spring Boot), Anti-Corruption Layer (Azure Functions), Audit & Reconciliation Worker (Java), On-Premise Integration Agent, Modern Claims Database (Azure SQL), Read-Through Cache (Azure Redis), Message Broker (Azure Service Bus)
- Components (API Gateway): JWT Validation Policy Engine, Path-Based Routing Router, Rate Limiting & Throttling Policy, Response Caching Policy Component, SSL/TLS Termination & WAF Component, Telemetry & Audit Logging Component
- Components (Claims Core Service): Claims REST Controllers, Claim Domain Service, Database Persistence Adapter, Messaging Publisher Adapter, Mainframe Anti-Corruption Adapter

## Relationships
- Customers, Brokers, Adjusters -> SSL/TLS Termination & WAF Component: Ingress traffic entry point [HTTPS]
- Claims Web App -> JWT Validation Policy Engine: Authenticates and submits requests [HTTPS / OpenID Connect]
- Path-Based Routing Router -> Claims Core Service: Forwards validated modern requests [HTTPS over internal VNet]
- Path-Based Routing Router -> Anti-Corruption Layer: Routes hybrid/legacy-bound requests [HTTPS over internal VNet]
- Claim Domain Service -> Messaging Publisher Adapter: Publishes domain events [AMQP / Azure Service Bus SDK]
- Mainframe Anti-Corruption Adapter -> Integration & Anti-Corruption Layer: Forwards integration payloads [HTTPS/gRPC over VNet]
- JWT Validation Policy Engine -> Active Directory: Validates security tokens [OIDC/JWT]

## Technology Stack
- Cloud Provider: Hybrid (Azure West Europe & On-Premises Mainframe)
- Edge / Gateway: Azure API Management (APIM) for routing, security, and throttling
- Web Frontend: React on Azure Static Web Apps for <2s adjuster screen loads
- Backend Services: Java / Spring Boot using Hexagonal Architecture on Azure App Service
- Database & Caching: Azure SQL Database and Azure Cache for Redis
- Messaging & Integration: Azure Service Bus and Azure Functions
- Security: OAuth2 / OpenID Connect integrated with enterprise Active Directory

## Rationale
[This hybrid architecture isolates expensive mainframe changes behind an Anti-Corruption Layer while incrementally migrating claim types to Azure.]
[It guarantees zero data loss and compliance with strict consistency, security, and performance constraints despite the team's limited cloud experience.]