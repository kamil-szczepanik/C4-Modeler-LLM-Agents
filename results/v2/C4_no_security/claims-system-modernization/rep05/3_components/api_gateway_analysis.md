## Overview
[The system is a modern hybrid cloud platform that gradually replaces a legacy mainframe insurance claims system. Its core purpose is to enable incremental claim migrations while maintaining business continuity.]

## Key Elements
- **API Gateway (Azure API Management)**: Managed entry point with Developer Portal, JWT Validation Policy, Dynamic Routing Policy Engine, App Config Lookup Component, and Rate Limiting.
- **Azure App Configuration**: Externalized configuration store for dynamic routing rules and feature flags.
- **Corporate Active Directory**: Identity provider for Single Sign-On.
- **Legacy Mainframe**: On-premise COBOL/DB2 system acting as the system of record.
- **Claims Core Service**: Modern backend service hosted on Azure Kubernetes Service (AKS).

## Relationships
- **Claims Web Application -> API Gateway**: Submits claims and manages workflows via [REST/HTTPS].
- **Developer Portal -> JWT Validation Policy**: Brokers authenticate for API access via [OAuth 2.0 / OpenID Connect].
- **Dynamic Routing Policy Engine -> Azure App Configuration**: Fetches claim-type routing state via [REST/HTTPS with 60s token-aware caching].
- **Dynamic Routing Policy Engine -> Claims Core Service**: Routes migrated claim types via [Internal REST/gRPC].
- **Dynamic Routing Policy Engine -> Legacy Mainframe**: Fallback routing for unmigrated claim types via [SOAP/HTTPS over VPN with Circuit Breaker and Timeout policies].

## Technology Stack
- **Azure API Management**: Selected for managed gateway, rate limiting, and built-in Developer Portal.
- **Azure App Configuration**: Selected to externalize routing rules and support one-day rollbacks without policy redeployments.
- **Azure Kubernetes Service (AKS)**: Selected to run the modern Claims Core Service.
- **OAuth 2.0 / OpenID Connect**: Selected for secure enterprise SSO integration.

## Rationale
[This hybrid architecture isolates the cloud-inexperienced team from high-risk mainframe changes by using externalized configuration for dynamic routing. It ensures seamless incremental migration and rapid one-day rollbacks while protecting system performance.]