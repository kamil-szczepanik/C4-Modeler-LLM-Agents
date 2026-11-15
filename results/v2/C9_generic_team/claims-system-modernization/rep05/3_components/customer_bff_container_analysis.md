## Overview
- Hybrid insurance claims modernization platform replacing a 30-year-old COBOL/DB2 mainframe.
- Enables online claim submissions and adjuster web applications while maintaining legacy continuity.

## Key Elements
- Customers and Brokers (External users)
- Customer BFF Container (Azure App Service / Container Apps)
- API Gateway Container (Azure Container Apps / API Management)
- Routing / Feature Flag Container (Container Apps)
- Modular Monolith Container (Azure App Service / Container Apps)
- Anti-Corruption Layer (ACL) Container (Azure Container Apps)
- Observability & Logging Container (Azure Application Insights)
- Configuration & Secrets Management Container (Azure Key Vault)

## Relationships
- Customers and Brokers -> Customer BFF Container: Online claim submission [HTTPS (TLS 1.3)]
- Customer BFF Container -> API Gateway Container: Internal API routing [Internal HTTPS/REST]
- Customer BFF Container -> Routing / Feature Flag Container: Dynamic routing checks [Internal REST]
- Customer BFF Container -> Configuration & Secrets Management Container: Secret retrieval [Azure SDK / HTTPS]
- Observability & Logging Container -> Customer BFF Container: Telemetry collection [Telemetry SDK]

## Technology Stack
- Azure App Service / Container Apps: Provides scalable, stateless hosting suitable for limited cloud experience.
- Azure Key Vault: Externalizes configuration and secrets for secure management.
- Azure Application Insights: Centralizes telemetry with strict PII scrubbing and correlation IDs.
- OpenAPI/Swagger: Standardizes API contracts between the BFF and API Gateway.

## Rationale
- The architecture isolates complex cloud dependencies in the BFF while enabling rapid feature flag rollbacks to the mainframe.
- Stateless scaling, circuit breakers, and presigned URLs ensure high availability and performance despite legacy latency.