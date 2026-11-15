## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-hosted platform while ensuring seamless coexistence. It enables online claim submissions and adjuster processing with zero data loss and rapid rollback capabilities.

## Key Elements
- **Users**: Customers, Brokers, Claims Adjusters, Customer Support Agents, Migration Product Managers
- **Frontend**: React/TypeScript Single Page Application (SPA) hosted in Azure Static Web Apps
- **API Gateway**: .NET Core / Envoy Backend-for-Frontend (BFF) implementing CQRS
- **Backend**: Modular monolith .NET Core service running on Azure App Service
- **Integration**: Azure Functions acting as the Mainframe Integration Adapter with Polly-based circuit breakers
- **Storage**: Azure SQL Database with temporal tables and a feature-flag table for dynamic claim routing
- **Security & Identity**: Azure Active Directory integrated via OIDC/OAuth2 and Azure Key Vault

## Relationships
- **Users to SPA**: HTTPS over TLS 1.3
- **SPA to API Gateway**: HTTPS/REST with OAuth2 JWT validation
- **API Gateway to Backend Services**: HTTPS and internal VNet routing
- **Integration Adapter to Mainframe**: Secured site-to-site VPN/ExpressRoute with TLS 1.3
- **Platform to Identity Provider**: OIDC/OAuth2 Single Sign-On (SSO)

## Technology Stack
- **Azure App Service**: PaaS hosting for backend containers to reduce operational overhead for teams with low cloud experience
- **Azure SQL Database**: Relational storage providing temporal tables for auditability and consistency (R-04)
- **Azure Functions**: Serverless integration layer handling mainframe protocol translation and retry logic
- **Azure Static Web Apps**: Hosting for the React/TypeScript frontend
- **Azure Application Insights**: Distributed tracing and monitoring for latency tracking across Azure and the legacy mainframe
- **Azure Key Vault**: Centralized management for secrets, connection strings, and certificates

## Rationale
The hybrid PaaS architecture minimizes operational complexity for a team with low cloud experience while fulfilling the strict 3-year migration window. Modular monolith services combined with dynamic feature flags guarantee rapid one-day rollbacks per claim type (R-06) and reliable data consistency (R-04).