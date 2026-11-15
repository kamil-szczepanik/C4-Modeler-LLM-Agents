## Overview
The hybrid system modernizes a 30-year-old regional insurer mainframe by gradually migrating claim types to a cloud-native platform. It maintains uninterrupted legacy operations while ensuring zero data loss and robust multi-system consistency.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Customer Portal & Adjuster Workspace (SPA React)
- API Gateway (Azure API Management)
- Claims Core Container (.NET / Azure Container Apps)
- Integration & ACL Container (Azure Container Apps)
- Read Model Projector (Azure Functions / .NET)
- Adjuster Read Database (Azure Cosmos DB)
- Message Broker (IBM MQ)
- Legacy Mainframe (COBOL/DB2)
- Azure Active Directory & Azure Key Vault

## Relationships
- Customer Portal & Adjuster Workspace -> API Gateway: HTTPS/REST
- API Gateway -> Claims Core Container: HTTPS/gRPC
- Claims Core Container -> Message Broker (IBM MQ): AMQP
- Integration & ACL Container -> Message Broker (IBM MQ): AMQP
- Mainframe Adapter -> Legacy Mainframe: IBM MQ with mTLS over Azure ExpressRoute/VPN
- Integration & Adjuster Workspace -> Azure Active Directory: OpenID Connect / OAuth 2.0

## Technology Stack
- Azure Container Apps: Standardizes runtime and reduces cognitive load for low-cloud-experience teams.
- .NET / C#: Powers core services and internal ACL components for domain modeling.
- IBM MQ: Ensures reliable asynchronous messaging during migrations and legacy batch windows.
- Azure Cosmos DB: Provides low-latency storage for the adjuster read model (<2s UI load requirement).
- Azure Key Vault & Managed Identities: Secures mTLS certificates and eliminates hardcoded credentials.

## Rationale
This hybrid architecture isolates expensive legacy mainframe touchpoints behind an Anti-Corruption Layer while modernizing the user-facing experience. It guarantees zero data loss and enables 1-day rollbacks per claim type using proven enterprise patterns and unified container runtimes.