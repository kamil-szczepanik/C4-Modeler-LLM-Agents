## Overview
[The system is a hybrid Insurance Claims Modernization platform that gradually replaces a 30-year-old mainframe claims system with a modern cloud architecture. Its core purpose is to enable online claims submission and adjuster workflows while maintaining zero downtime and continuous data consistency.]

## Key Elements
* Customers and Brokers
* Claims Adjusters
* API Gateway / Backend-for-Frontend (.NET 8 Web API)
* Routing & Feature Flag Router Component
* Aggregator / Composition Service Component
* Authentication & Token Exchange Middleware Component
* Resilience & Telemetry Component
* Legacy Mainframe
* Claims Domain Services (.NET 8, Azure Container Apps)
* Integration & Sync Engine (Azure Functions, Azure Service Bus)
* Corporate Active Directory & Azure Entra ID
* Azure Redis Cache
* Azure App Configuration
* Azure Key Vault

## Relationships
* Customer Portal -> API Gateway / Backend-for-Frontend: Makes API requests [HTTPS / REST over TLS 1.3]
* Adjuster Workspace -> API Gateway / Backend-for-Frontend: Makes API requests [HTTPS / REST over TLS 1.3]
* API Gateway / Backend-for-Frontend -> Claims Domain Services: Invokes domain services [gRPC with strict mTLS]
* Authentication & Token Exchange Middleware -> Corporate Active Directory & Azure Entra ID: Validates tokens [OpenID Connect / OAuth2]
* Routing & Feature Flag Router -> Azure App Configuration: Fetches feature flags [HTTPS with local memory fallback]
* API Gateway / Backend-for-Frontend -> Azure Redis Cache: Reads and writes encrypted response data [TLS with field-level encryption]
* API Gateway / Backend-for-Frontend -> Azure Key Vault: Retrieves secrets using Azure Managed Identities [HTTPS]

## Technology Stack
* .NET 8 Web API: Chosen for high performance and strong enterprise support in building the Backend-for-Frontend.
* Azure Container Apps: Used to host containerized components with KEDA auto-scaling based on HTTP concurrency.
* OpenID Connect / OAuth2 & Azure Entra ID: Implements single sign-on and strict token exchange security.
* gRPC with mTLS: Provides secure, high-performance internal communication between the BFF and domain services.
* Polly & OpenTelemetry: Implements circuit breakers, resilience policies, and distributed tracing.
* Azure Redis Cache: Provides distributed caching with field-level encryption to meet performance and security requirements.

## Rationale
[This hybrid architecture decouples modern user interfaces from the legacy mainframe while isolating complex migration logic inside the BFF and domain services. It guarantees high performance, strict security, and operational resilience despite the team's limited initial cloud experience.]