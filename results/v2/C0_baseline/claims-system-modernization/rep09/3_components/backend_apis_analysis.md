## Overview
[Modern Claims Platform progressively replaces a legacy mainframe with a hybrid .NET application hosted on Azure Container Apps. The system ensures zero data loss and resilient claim processing during a multi-year migration.]

## Key Elements
- Claim Routing Component (.NET / MediatR / Azure App Configuration)
- Read Model & Caching Component (.NET / Redis / Azure SQL)
- Command Processing Component (.NET / FluentValidation)
- API Gateway Controller Layer (.NET / ASP.NET Core)
- Mainframe Anti-Corruption Layer (ACL) Client (.NET / Polly)
- Azure Service Bus
- Azure SQL Database

## Relationships
- Customer Portal & Adjuster Workspace -> Claim Routing Component [HTTPS/JSON]
- Claim Routing -> Read Model & Command Processing [In-Process / MediatR]
- Command Processing Component -> Azure Service Bus [AMQP]
- Claim Domain Handler -> Mainframe ACL Client [HTTPS/SOAP/MQ with mTLS]
- Backend APIs -> Azure SQL Database [Entity Framework Core / Managed Identity]

## Technology Stack
- .NET / ASP.NET Core: Core application framework for unified backend APIs
- MediatR: In-process messaging for clean command and query separation
- Redis & Azure SQL: High-performance caching and relational persistence for sub-2s response times
- Polly: Resilience policies (circuit breakers, retries) for unstable mainframe integration
- Azure Container Apps: Scalable serverless container hosting
- Azure Service Bus: Asynchronous message broker ensuring consistency

## Rationale
[This architecture isolates slow legacy mainframe dependencies through an Anti-Corruption Layer and asynchronous messaging while meeting strict sub-2s performance and consistency requirements. It enables gradual claim type migration via dynamic feature flags while mitigating the team's limited cloud experience.]