## Overview
[The system modernizes a 30-year-old regional insurance claims platform by gradually migrating claim types to a new cloud-based architecture while keeping the mainframe as the system of record. It enables online claims submission and adjuster management with zero data loss or downtime.]

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Frontend SPA (React / TypeScript, Azure Static Web Apps)
- API Gateway (.NET Core / Envoy)
- Backend Service (Modular Monolith .NET Core, Azure App Service)
- Mainframe Integration Adapter (Azure Container Apps / App Service, Polly)
- Legacy Mainframe (COBOL/DB2)
- Azure SQL Database
- Azure Service Bus Queue
- Azure Key Vault
- Azure Application Insights
- Identity Provider (Active Directory)

## Relationships
- Customers/Brokers -> Frontend SPA [HTTPS / TLS 1.3]
- Frontend SPA -> API Gateway [HTTPS / REST]
- API Gateway -> Backend Service [Internal VNet routing]
- Backend Service -> Mainframe Integration Adapter [Internal VNet routing]
- Mainframe Integration Adapter -> Azure Service Bus Queue [AMQP]
- Mainframe Integration Adapter -> Legacy Mainframe [mTLS over Site-to-Site VPN/ExpressRoute, TLS 1.3]
- Mainframe Integration Adapter -> Azure SQL Database [T-SQL via VNet]
- Mainframe Integration Adapter -> Azure Key Vault [HTTPS via Managed Identity]

## Technology Stack
- Azure Container Apps / App Service: Containerized runtime eliminating serverless cold starts for developers with low cloud experience
- Polly Pipeline: Handles circuit breaking and exponential backoff for unstable legacy connections
- Azure Service Bus Queue: Buffers traffic and prevents data loss during mainframe unresponsiveness
- Azure Key Vault: Secures mTLS certificates and credentials via Managed Identities
- Azure Application Insights: Provides distributed tracing and observability

## Rationale
[This hybrid architecture abstracts fragile mainframe dependencies behind a resilient, containerized integration adapter to ensure strict consistency and performance. It minimizes costly legacy changes while empowering a team with low cloud experience to deliver a secure, modern web platform.]