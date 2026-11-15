## Overview
[The system is a modern insurance claims platform API Gateway that unifies hybrid routing between a new Azure-hosted service and a legacy mainframe. Its core purpose is to securely manage external traffic while enabling gradual, zero-loss claim type migration.]

## Key Elements
* Azure Front Door / Azure API Management (API Gateway container)
* Authentication & WAF Component (APIM Policies)
* Routing Configuration Loader (Azure App Configuration)
* Transformation & Caching Component (APIM Liquid Templates / Response Cache)
* Circuit Breaker Policy Engine (APIM native policies)
* Azure Key Vault
* Azure Application Insights

## Relationships
* Policyholders and Brokers -> API Gateway: Online claim submission [HTTPS/REST via TLS 1.3]
* API Gateway -> Claims Core Service: Dynamic routing of requests [gRPC / HTTPS with mTLS]
* API Gateway -> Legacy Mainframe Proxy: Fallback routing [HTTPS with mTLS]
* API Gateway -> Azure App Configuration: Fetch routing definitions [HTTPS]
* API Gateway -> Azure Key Vault: Retrieve backend credentials [Managed Identity / HTTPS]
* API Gateway -> Azure Application Insights: Forward telemetry and W3C Trace Context headers [HTTPS]

## Technology Stack
* Azure API Management & Azure Front Door: Chosen for WAF protection, rate-limiting, and native routing policies.
* Azure App Configuration: Stores version-controlled routing rules to support rapid one-day fallback (R-06).
* Azure Key Vault: Secures mainframe credentials and API keys via Managed Identities.
* Bicep / Terraform: Infrastructure as Code for automated, drift-free deployments.
* Azure Application Insights: Provides distributed tracing and observability.

## Rationale
[This architecture enforces strict security boundaries while abstracting legacy complexity to meet strict data consistency and performance mandates. It specifically accommodates the team's low cloud experience through managed Azure services and externalized configuration.]