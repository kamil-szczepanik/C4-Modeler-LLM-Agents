## Overview
Modernizes a regional insurer's legacy mainframe claims system via a hybrid cloud platform while preserving core operations. It gradually migrates claim types over three years without extending nightly batch windows.

## Key Elements
- Users: Customers, Brokers, Claims Adjusters
- Frontend: Customer Portal (React SPA), Adjuster Workspace (React SPA)
- Gateway & Routing: Azure API Management, Outbound Topic Router
- Core Services: Claims Core Container (.NET), Read Model Projector (Azure Functions), Integration & ACL Container
- Messaging & Storage: IBM MQ (Message Broker), Azure Cosmos DB (Adjuster Read Database)
- Security & Infrastructure: Azure Active Directory, Azure Key Vault, Azure Monitor / Sentinel

## Relationships
- Customer Portal / Adjuster Workspace -> Azure API Management: Handles HTTPS/REST traffic [REST/TLS]
- Claims Core Container -> Outbound Topic Router: Publishes domain events [IBM MQ / AMQP]
- Outbound Topic Router -> Integration & ACL Container: Forwards legacy sync events [IBM MQ]
- Message Broker -> Azure Monitor / Sentinel: Streams security audit logs [HTTPS]

## Technology Stack
- Cloud Platform: Azure West Europe & On-Premise Hybrid (for low cloud-experience team transition)
- Backend Compute: Azure Container Apps, Azure Functions (.NET)
- Messaging: IBM MQ (enables hybrid on-premise mainframe to Azure bridging)
- Database: Azure Cosmos DB (supports <2s adjuster screen loads)
- Security: OAuth 2.0 / JWT, Mutual TLS (mTLS), Azure Key Vault (for zero-loss and strict access control)

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while enabling gradual claim migration within strict consistency constraints. Standardized Azure and IBM MQ technologies mitigate the team's low cloud experience risks.