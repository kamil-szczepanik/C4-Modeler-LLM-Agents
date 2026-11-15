## Overview
- Hybrid modernization platform replacing an on-premises mainframe claims system gradually over three years.
- Enables online customer submissions, low-latency adjuster workflows, and secure claim-type migration.

## Key Elements
- End Customers & Brokers (Users)
- Claims Adjusters (Users)
- Legacy Mainframe (External System / System of Record)
- Corporate Active Directory (External System)
- API Gateway (Azure API Management / NGINX)
- Customer Portal (React / Node.js)
- Adjuster Workspace including Operations Dashboard (React / .NET Core API)
- Integration & Anti-Corruption Layer (.NET Core / MassTransit)
- Claim Read Model Database (Azure Cosmos DB)
- Configuration & Feature Store (Azure App Configuration / Redis)

## Relationships
- Customer Portal to API Gateway via HTTPS/REST
- Adjuster Workspace to API Gateway via HTTPS/REST
- API Gateway to Corporate Active Directory via OIDC/OAuth2 for SSO
- API Gateway to Microservices via Internal HTTPS/gRPC with OpenTelemetry
- Integration & Anti-Corruption Layer to Legacy Mainframe via MQ/Enterprise Service Bus over mTLS
- Adjuster Workspace to Claim Read Model Database via TCP/NoSQL

## Technology Stack
- Hybrid Cloud (Azure West Europe + On-Premises Mainframe) to balance legacy retention and modern scalability
- .NET Core and React for modern, maintainable microservices and UI components
- Azure Cosmos DB for low-latency read models supporting <2s UI requirements
- Azure API Management for dynamic routing, rate-limiting, and SSO validation
- Azure App Configuration for managing feature flags and one-day claim-type fallbacks
- Terraform/Bicep and GitOps (ArgoCD/Flux) for infrastructure automation

## Rationale
- Decouples legacy dependencies through an Integration & Anti-Corruption Layer to ensure zero lost claims and support gradual migration.
- Employs a CQRS pattern with Azure Cosmos DB to guarantee sub-2-second adjuster screens despite high mainframe latency.