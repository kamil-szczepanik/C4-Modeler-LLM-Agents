## Overview
The hybrid system modernizes a regional insurer's claims platform by gradually migrating claim types from a 30-year-old mainframe to Azure while preserving legacy batch windows and data consistency. It enables online claims submission and adjuster workflows through a secure cloud frontend.

## Key Elements
- Policyholders and Insurance Brokers
- Claims Adjusters
- Azure API Gateway & WAF (Azure Web Application Firewall)
- Azure Container Apps / App Service
- Azure SQL Database
- On-Premise COBOL/DB2 Mainframe
- Azure Active Directory / Entra ID
- Azure Application Insights and Azure Key Vault

## Relationships
- Policyholders, Brokers -> Azure API Gateway & WAF: Online claim submission [HTTPS (TLS 1.3), OAuth 2.0 / OIDC]
- Azure API Gateway & WAF -> Azure Container Apps: Ingress routing and reverse proxy [mTLS / Private VNet]
- Azure Container Apps -> Azure SQL Database: Data persistence [TLS]
- Azure Container Apps -> On-Premise COBOL/DB2 Mainframe: Legacy data processing and fallback [Secure VPN / Dedicated Interconnect]
- Azure API Gateway & WAF -> Entra ID: Single sign-on token validation [OAuth 2.0, OIDC]

## Technology Stack
- Azure API Gateway & WAF: Edge routing, rate-limiting, and OWASP Top 10 prevention for hybrid entry
- Azure Container Apps: Backend microservices execution ensuring low-latency adjuster screens (<2s)
- Azure SQL Database: Modern relational data store for migrated claim types
- Entra ID: Identity management providing SSO and OAuth 2.0 / OIDC token validation
- Azure Application Insights: Distributed tracing and telemetry to isolate latency across hybrid boundaries
- Azure Key Vault: Centralized secret and certificate management

## Rationale
The hybrid architecture enables incremental claim-type migration off the expensive mainframe without exceeding quarterly change limits or extending batch windows. It bridges the team's low cloud experience with managed Azure services while meeting strict security, performance, and 1-day fallback requirements.