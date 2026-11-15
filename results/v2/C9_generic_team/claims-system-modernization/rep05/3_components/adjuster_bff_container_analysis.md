## Overview
[The system is a hybrid Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with a cloud-native Azure architecture. Its core purpose is to enable seamless online claims submission and adjuster workflows while maintaining zero downtime and strict data consistency.]

## Key Elements
- Adjuster BFF Container (Azure App Service / Container Apps)
- API Gateway Container (Azure Container Apps / API Management)
- Asynchronous Messaging & Caching Layer (Azure Service Bus and Redis)
- Routing / Feature Flag Container (Container Apps)
- Observability & Logging Container (Azure Application Insights)
- Configuration & Secrets Management Container (Azure Key Vault)
- COBOL/DB2 Mainframe (On-premises system of record)

## Relationships
- Claims Adjusters -> Adjuster BFF Container: Interacts for adjuster workflows via HTTPS (TLS 1.3)
- Adjuster BFF Container -> API Gateway Container: Communicates via internal APIs using Internal HTTPS/REST
- Observability & Logging Container -> Adjuster BFF Container: Collects telemetry via Telemetry SDK

## Technology Stack
- Azure Container Apps: Chosen for hosting containers with managed ingress and scaling, matching the team's need for simplicity despite limited cloud experience.
- Redis Cache: Selected for offloading session state and pre-fetching read-models to guarantee sub-2s screen loads (R-05).
- OpenAPI & Schema Validation Middleware: Utilized for contract-first development and early payload validation to protect downstream legacy systems.
- Azure Key Vault: Implemented for centralized, secure configuration and secrets management via environment injection.
- W3C Trace Context & Structured JSON Logging: Adopted for distributed tracing and rapid incident triage across the hybrid network boundary.

## Rationale
[This architecture decouples modern user interfaces from a brittle mainframe using a stateless Backend-For-Frontend and caching layer, satisfying strict performance and rollback requirements (R-05, R-06). Furthermore, it simplifies operational complexity for a cloud-inexperienced team by leveraging managed Azure services while preserving business continuity.]