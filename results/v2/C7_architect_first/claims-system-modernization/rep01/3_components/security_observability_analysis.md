## Overview
[The system modernizes a 30-year-old mainframe claims system via a hybrid cloud platform while ensuring business continuity. It provides secure online claim submission and adjuster processing while bridging Azure and on-premise components.]

## Key Elements
* Token Validator Component (.NET Core Middleware, OpenID Connect)
* Secret Manager Client (Managed Identities, Azure Key Vault)
* Telemetry Aggregator (OpenTelemetry SDK, gRPC, Azure Monitor)
* Audit Logger Component (.NET Core library, Azure Log Analytics)
* mTLS Termination Proxy (Azure Container Apps Ingress)
* Automated Rotation Service (Azure Event Grid, Azure Functions)

## Relationships
* Users to API Gateway: HTTPS / TLS 1.3
* Token Validator to Azure AD (Entra ID): OpenID Connect / HTTPS
* Secret Manager Client to Azure Key Vault: Managed Identities / HTTPS / REST
* Telemetry Aggregator to Azure Monitor: gRPC / OpenTelemetry
* Azure Container Apps to On-Premise Mainframe: mTLS / HTTPS

## Technology Stack
* .NET Core: For secure, standardized middleware and shared security/observability libraries
* Azure Active Directory (Entra ID): For single sign-on, RBAC, and Continuous Access Evaluation (CAE)
* Azure Key Vault: For centralized secret management and automated credential rotation
* Azure Monitor / Log Analytics: For distributed tracing, metrics, and immutable audit logging
* Azure Container Apps: For hosting cloud containers with native ingress mTLS and local disk buffering

## Rationale
[This architecture secures hybrid claims processing and bridges low cloud experience through managed Azure services and reusable templates. It enforces strict zero-trust and compliance without exceeding the immutable mainframe constraints.]