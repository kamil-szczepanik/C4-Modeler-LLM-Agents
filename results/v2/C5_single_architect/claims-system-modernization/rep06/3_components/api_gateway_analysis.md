## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old on-premises mainframe claims system with a hybrid cloud platform. It enables online claim submission and adjuster workflows while maintaining data consistency across systems.

## Key Elements
- **Users**: Customer / Broker, Claims Adjuster
- **External Systems**: Insurer's Active Directory, Legacy Mainframe (COBOL/DB2, On-Premises)
- **Containers**: API Gateway (Azure API Management), Customer Portal (Azure App Service - React/Node.js), Adjuster Workspace (Azure App Service - React/.NET Core API), Claims Anti-Corruption Layer / Core Domain Service (Azure Container Apps - .NET Core), Integration & Sync Engine (Azure Service Bus + Azure Functions)
- **API Gateway Components**: Routing & Aggregation Component, Authentication & Authorization Component, Rate Limiting & Throttling Component, Request Transformation Component, Monitoring & Analytics Component

## Relationships
- Customer / Broker -> API Gateway: Submits online claims and interacts [HTTPS]
- Claims Adjuster -> API Gateway: Processes claims and interacts [HTTPS]
- API Gateway -> Customer Portal: Routes requests to customer portal [HTTPS]
- API Gateway -> Adjuster Workspace: Routes requests to adjuster workspace [HTTPS]
- API Gateway -> Insurer's Active Directory: Authenticates users via SSO [OAuth2 / OpenID Connect]
- API Gateway -> Claims Anti-Corruption Layer: Routes direct API traffic for migrated claim types [HTTPS / REST]
- API Gateway -> Integration & Sync Engine: Forwards asynchronous event triggers [HTTPS / AMQP]

## Technology Stack
- **Azure API Management**: Acts as the API Gateway for built-in security, routing, and rate limiting with minimal custom code.
- **Azure App Service**: Hosts the Customer Portal (React/Node.js) and Adjuster Workspace (React/.NET Core API) for managed web deployment.
- **Azure Container Apps**: Runs the Claims Anti-Corruption Layer and Core Domain Services (.NET Core) for containerized flexibility.
- **Azure Service Bus & Azure Functions**: Powers the Integration & Sync Engine for reliable asynchronous messaging.
- **Azure Application Insights**: Provides monitoring and telemetry to track latency against mainframe constraints.

## Rationale
This hybrid architecture isolates the fragile legacy mainframe behind an anti-corruption layer and managed integration services while gradually migrating claim types. Azure-managed services reduce the operational burden for a team with limited cloud experience.