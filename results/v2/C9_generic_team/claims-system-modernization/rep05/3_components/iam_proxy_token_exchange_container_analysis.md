## Overview
The system is a hybrid Insurance Claims Modernization platform that gradually replaces a 30-year-old mainframe with a cloud-native architecture. Its core purpose is to enable online claims submission and adjuster web applications while maintaining operational continuity with the on-premise COBOL/DB2 system.

## Key Elements
- IAM Proxy / Token Exchange Container (Azure Container Apps)
- Active Directory (On-premise / Enterprise IDP)
- API Gateway Container (Azure Container Apps / API Management)
- Customer BFF & Adjuster BFF Containers (Azure App Service / Container Apps)
- Asynchronous Messaging & Caching Layer (Azure Service Bus and Redis)
- Configuration & Secrets Management Container (Azure Key Vault)
- Observability & Logging Container (Azure Application Insights)
- COBOL/DB2 Mainframe System of Record (On-premise)

## Relationships
- IAM Proxy / Token Exchange Container -> Active Directory: Authenticates users and exchanges tokens via SAML/OAuth2/OIDC
- IAM Proxy / Token Exchange Container -> Asynchronous Messaging & Caching Layer: Caches session states and token validations using Redis
- IAM Proxy / Token Exchange Container -> Observability & Logging Container: Reports security events using Azure Application Insights via W3C Trace Context
- API Gateway Container -> IAM Proxy / Token Exchange Container: Validates incoming requests and inspects JWT claims

## Technology Stack
- Azure Container Apps: Hosts the IAM Proxy container for simplified serverless container management given limited cloud experience
- Azure App Service Authentication (Easy Auth) / RFC 8693: Standardizes token exchange without custom protocol translation to reduce security risks
- Azure Key Vault: Dynamically supplies immutable configuration, issuer mappings, and secrets at startup to prevent configuration drift
- Redis: Caches tokens to accelerate validation checks and protect sub-2-second adjuster screen load performance
- W3C Trace Context: Propagates correlation IDs across the hybrid boundary for end-to-end observability in Application Insights

## Rationale
This architecture balances strict legacy constraints with cloud modernization by isolating authentication logic in a managed, scalable proxy. It protects an inexperienced cloud team through standard protocols and automated health checks while ensuring data consistency and sub-2-second performance across the hybrid boundary.