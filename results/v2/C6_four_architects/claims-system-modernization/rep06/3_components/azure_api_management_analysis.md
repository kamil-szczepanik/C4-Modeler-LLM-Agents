## Overview
[A hybrid cloud architecture for Insurance Claims Modernization that gradually migrates claims types from a legacy mainframe to an Azure-hosted modern platform using Azure API Management as the unified gateway. It ensures business continuity and strict system consistency while mitigating the team's limited cloud experience.]

## Key Elements
- **Users**: Customers and Brokers, Claims Adjusters
- **External Systems**: Legacy Mainframe (COBOL/DB2), Active Directory / Azure AD, Notification Service, Payment Gateway, Document Management System, Audit & Compliance System
- **Containers**: Customer Portal & Adjuster Workspace SPAs (React, Azure Static Web Apps), Azure API Management (Azure API Management), Claims Core Service (.NET 8, Azure Container Apps), Mainframe Integration Adapter (.NET 8, Azure Container Apps), Audit & Compliance Worker (.NET 8, Azure Container Apps), Azure Service Bus, Azure SQL Database, Azure Data Factory
- **APIM Components**: JWT Validation Policy, Response Caching Component (Azure Redis Cache), Rate Limiting & Quota Policy, Transformation & Request Routing Policy

## Relationships
- Customer Portal / Adjuster Workspace -> Azure API Management: Send API requests with OIDC/OAuth2 authentication [HTTPS (OIDC/OAuth2)]
- JWT Validation Policy -> Azure Active Directory: Fetch OpenID Connect metadata and JSON Web Keys (JWKS) [HTTPS / OIDC]
- Response Caching Component -> Azure Redis Cache: Cache read-only claim lookup data [TCP / Redis Protocol]
- Transformation & Request Routing Policy -> Claims Core Service: Route modern claim type requests [HTTP/2]
- Transformation & Request Routing Policy -> Mainframe Integration Adapter: Route legacy fallback requests [HTTP/2]
- Azure API Management -> Azure Application Insights: Emit metrics, tracing headers, and logs [HTTPS / OpenTelemetry]

## Technology Stack
- Azure API Management: Unified managed API Gateway reducing operational overhead for cloud-inexperienced teams
- Azure Container Apps & .NET 8: Modern microservices runtime for containerized core services
- Azure SQL Database & Entity Framework Core: Relational data store for modern claim types
- Azure Service Bus: Asynchronous messaging backbone for reliable claim processing
- Azure Static Web Apps & React: Frontend hosting and UI implementation
- Azure Redis Cache: In-memory caching layer to protect the legacy mainframe from performance degradation

## Rationale
[This hybrid architecture decouples the modern web applications from the 30-year-old mainframe via Azure API Management, enabling gradual one-by-one claim type migration without breaking the strict nightly batch window or exceeding expensive mainframe interface limits. By leveraging fully managed Azure services and declarative APIM policies, it minimizes custom infrastructure code to successfully accommodate a team with limited cloud experience.]