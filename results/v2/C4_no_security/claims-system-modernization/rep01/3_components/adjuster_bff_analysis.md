## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-hosted platform while ensuring business continuity. It provides online claim submission, adjuster workstations, and a hybrid architecture maintaining legacy integration.]

## Key Elements
- Policyholders and Brokers
- Claims Adjusters
- Legacy Mainframe (COBOL/DB2, On-Premises)
- Microsoft Entra ID
- Anti-Corruption Layer (ACL) Gateway
- Azure API Management (API Gateway)
- Customer/Broker Portal (Azure App Service, Node.js, TypeScript)
- Adjuster Workstation (Azure App Service, Node.js, TypeScript)
- Adjuster BFF (.NET Core, C#)
- Core Claims Domain (.NET Core, C#)
- Operational Data Store (Azure Database for PostgreSQL)

## Relationships
- Adjuster Workstation -> Adjuster BFF: UI requests [HTTPS, gRPC]
- Adjuster BFF -> Core Claims Domain: Domain queries and commands [HTTPS, gRPC]
- Adjuster BFF -> Anti-Corruption Layer (ACL) Gateway: Legacy integration [HTTPS, gRPC]
- Adjuster BFF -> Operational Data Store (PostgreSQL): Read-model caching and state persistence [TLS]
- Customer/Broker Portal -> Azure APIM: External API requests [HTTPS]
- Adjuster BFF -> Microsoft Entra ID: Single Sign-On [OIDC, OAuth 2.0]

## Technology Stack
- Azure App Service: Hosting for BFF and portal containers due to team's cloud profile
- ASP.NET Core / C#: Backend services providing high performance and type safety
- gRPC / HTTPS: Inter-container communication protocol ensuring low latency
- Azure Database for PostgreSQL: Operational Data Store for CQRS read-models
- Polly: Resilience library for circuit breakers and retry policies
- Azure Application Insights & Prometheus: Distributed tracing and monitoring

## Rationale
[This hybrid architecture isolates legacy mainframe latencies using a CQRS-based Adjuster BFF with aggressive caching to consistently meet the sub-2-second UI performance requirement. Additionally, dynamic migration routing within the BFF enables seamless, zero-downtime claim type cutovers and one-day rollbacks.]