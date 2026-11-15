## Overview
[The system is a hybrid cloud-native platform gradually replacing an on-premise mainframe system while ensuring continuous, zero-loss claim processing during a 3-year transition. It modernizes customer submissions and adjuster workflows while maintaining secure legacy integration.]

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Insurance Claims Modernization platform
- Web Application
- Customer Portal
- Claim Processing API
- Integration Gateway / ACL
- Feature Flag / Migration Router
- Document & Audit Store
- Legacy Mainframe
- Azure AD (Entra ID)
- Payment Gateway
- Core Notification Service
- Enterprise Service Bus (ESB/MQ)

## Relationships
- Customers & Brokers -> Insurance Claims Modernization platform: HTTPS (REST/GraphQL)
- Claims Adjusters -> Insurance Claims Modernization platform: HTTPS
- Web Application -> Claim Processing API: HTTPS (REST/GraphQL)
- Customer Portal -> Claim Processing API: HTTPS (REST/GraphQL)
- Claim Processing API -> Feature Flag / Migration Router: Internal gRPC / HTTPS
- Claim Processing API -> Integration Gateway / ACL: Asynchronous messaging via Enterprise Service Bus (ESB/MQ) over AMQP/MQTT with mTLS
- Claim Processing API -> Document & Audit Store: HTTPS / TLS 1.3 (Azure SDK)
- Integration Gateway / ACL -> Legacy Mainframe: Hybrid ESB/MQ connection
- Insurance Claims Modernization platform -> Azure AD (Entra ID): OpenID Connect / OAuth 2.0 via HTTPS
- Insurance Claims Modernization platform -> Payment Gateway: HTTPS (REST with OAuth 2.0)
- Insurance Claims Modernization platform -> Core Notification Service: Asynchronous Webhooks via Azure Event Grid (HTTPS)

## Technology Stack
- Azure Container Apps: Consolidates backend compute to simplify deployments for low-cloud-experience teams
- React / TypeScript & Next.js: Powers responsive adjuster and customer web interfaces
- Azure Blob Storage & Azure Cosmos DB: Provides secure, cloud-native document and audit data storage
- Enterprise Service Bus (ESB/MQ): Decouples modern services from the legacy mainframe for zero-loss messaging
- Azure Key Vault & Managed Identities: Secures secrets and enforces secretless authentication

## Rationale
[This hybrid architecture isolates complex cloud plumbing and legacy dependencies, ensuring fast UI performance and instant mainframe fallback. It protects business continuity and meets strict data security constraints throughout the three-year migration window.]