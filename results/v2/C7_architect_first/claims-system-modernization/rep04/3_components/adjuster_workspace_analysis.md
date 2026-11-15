## Overview
The Adjuster Workspace is a modern web container built with ASP.NET Core on Azure App Service that enables claims adjusters to process insurance claims efficiently. It acts as a hybrid bridge, interfacing with legacy on-premises mainframe systems while supporting the gradual migration of claim types.

## Key Elements
- **UI Controller / Razor Pages**: ASP.NET Core MVC component handling user interaction and rendering views [HTTPS].
- **Claim Processing Facade**: C# service orchestrating workflow, caching, business metrics emission, and audit logging.
- **Local Claim Cache**: `IMemoryCache` component mitigating 5-second mainframe latency via short-TTL cached claim states.
- **Integration Client**: gRPC client communicating securely with backend services.
- **Auth Handler**: ASP.NET Core Security Middleware integrating with Microsoft Entra ID via OpenID Connect (OIDC).
- **Claims Integration Service**: Downstream .NET Core Worker Service hosted in Azure Container Apps.

## Relationships
- Claims Adjuster -> UI Controller / Razor Pages: Interacts to process claims [HTTPS/REST]
- UI Controller / Razor Pages -> Claim Processing Facade: Invokes business logic [In-Process]
- Claim Processing Facade -> Local Claim Cache: Reads and writes cached claim states [In-Process]
- Claim Processing Facade -> Integration Client: Requests backend data [In-Process]
- Integration Client -> Claims Integration Service: Fetches claim data [gRPC over HTTP/2 with TLS 1.3]
- Auth Handler -> Microsoft Entra ID: Authenticates users [OpenID Connect (OIDC)]

## Technology Stack
- **ASP.NET Core (.NET Core)**: Chosen for high performance and robust web application scaffolding.
- **Azure App Service**: Provides scalable managed hosting for the web container with blue-green deployment slots.
- **gRPC over HTTP/2**: Ensures high-performance binary communication with backend integration services.
- **`IMemoryCache`**: Selected over Azure Redis Cache to minimize operational overhead and avoid external connection secrets for a team with low cloud experience.
- **OpenTelemetry**: Mandated for distributed tracing and custom business metrics across hybrid boundaries.

## Rationale
This architecture achieves sub-2-second adjuster screen loads despite slow 5-second mainframe responses by implementing an in-memory caching layer and async workflow orchestration. It ensures seamless hybrid connectivity and strict security controls while accommodating the team's limited cloud expertise.