## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform. It enables online claim submission, adjuster workflows, and incremental claim type migration while maintaining data consistency.

## Key Elements
* Customer / Broker
* Claims Adjuster
* Legacy Mainframe (COBOL/DB2)
* Identity Provider (Azure Active Directory)
* Customer Portal (Azure Static Web Apps / React)
* Adjuster Workspace (Azure Container Apps / .NET Core)
* API Gateway (Azure Container Apps / .NET YARP)
* Claims Core Service (Azure Container Apps / .NET Core)
* Integration Message Broker (Azure Service Bus)
* Database (Azure SQL Database / EF Core)
* Anti-Corruption Layer (ACL)
* API Gateway Components: Routing Engine, Authentication & Authorization Filter, Rate Limiting & Resiliency Policy Middleware, Transformation & Protocol Bridge

## Relationships
* Customer Portal -> API Gateway: API requests [HTTPS/WSS]
* Adjuster Workspace -> API Gateway: API requests [HTTPS/WSS]
* API Gateway -> Claims Core Service: Routes claims requests [gRPC/HTTP]
* API Gateway -> Identity Provider: Authenticates users [OpenID Connect]
* Customer Portal -> Authentication & Authorization Filter: Validates tokens [HTTPS]
* Routing Engine -> Transformation & Protocol Bridge: Passes raw requests [In-memory]
* Transformation & Protocol Bridge -> Claims Core Service: Forwards gRPC commands [gRPC/HTTP2]

## Technology Stack
* Azure Container Apps: Hosting containerized microservices to accommodate team's limited cloud experience.
* .NET YARP (Yet Another Reverse Proxy): High-performance routing integrated natively with .NET.
* gRPC/HTTP2: Inter-service communication for low latency and efficient serialization.
* Azure Active Directory / OpenID Connect: Secure single sign-on satisfying security requirements.
* Polly (.NET): Transient fault handling and circuit breakers for slow mainframe responses.

## Rationale
This hybrid architecture isolates expensive mainframe changes behind an Anti-Corruption Layer while enabling incremental migration of claim types. The cloud-native Azure and .NET stack balances modern performance needs with the team's existing skill set.