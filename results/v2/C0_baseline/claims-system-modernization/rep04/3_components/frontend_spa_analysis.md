## Overview
The Insurance Claims Modernization platform gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud architecture. It provides secure online claim submission and an adjuster workbench while maintaining the mainframe as the system of record.

## Key Elements
- **Users**: Customers (Policyholders), Brokers, Claims Adjusters, Support Agents, Migration Product Managers
- **Frontend SPA**: React / TypeScript application hosted on Azure Static Web Apps
- **SPA Internal Modules**: Routing & Shell Component, Claim Submission Module, Adjuster Workbench Module, Feature Flag & Migration Service, Auth Client Module (MSAL.js), API Client Service
- **API Gateway**: .NET Core / Envoy providing API management and CQRS routing
- **Backend Service**: Modular Monolith in .NET Core hosted on Azure App Service
- **Mainframe Integration Adapter**: Azure Functions with Polly for resilience
- **Database**: Azure SQL Database
- **External Systems**: Legacy COBOL/DB2 Mainframe, Active Directory (Identity Provider)

## Relationships
- Customers, Brokers, Adjusters, Support Agents, PMs -> Frontend SPA: Submits, tracks, and processes claims [HTTPS over TLS 1.3]
- Frontend SPA -> Identity Provider: Authenticates users [OIDC / OAuth2 SSO via MSAL.js]
- Frontend SPA -> API Gateway: Sends API requests and real-time updates [HTTPS/REST and WebSockets with OAuth2 JWT validation]
- API Gateway -> Backend Service: Routes business logic commands and queries [gRPC / HTTPS]
- Backend Service -> Mainframe Integration Adapter: Bridges hybrid cloud boundaries [Azure Service Bus / HTTPS]
- Mainframe Integration Adapter -> Legacy Mainframe: Synchronizes batch and transactional data [SNA / TCP/IP]

## Technology Stack
- **Frontend**: React, TypeScript, TanStack Query, MSAL.js for low-latency SPA rendering and in-memory state management
- **Hosting & CI/CD**: Azure Static Web Apps with GitHub Actions for automated deployment, global CDN caching, and staging-to-production swap rollbacks
- **Backend**: .NET Core Modular Monolith on Azure App Service for scalable business logic processing
- **Security**: Azure Key Vault, strict Content Security Policy (CSP), W3C Trusted Types, and HttpOnly/SameSite cookies for PII protection and XSS mitigation
- **Observability**: Azure Application Insights Real User Monitoring (RUM) for Core Web Vitals and latency tracking

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while introducing a modern, responsive Azure-hosted UI that masks legacy latency. It strictly satisfies business and migration requirements, enabling incremental claim type migration with a rapid one-day fallback capability.