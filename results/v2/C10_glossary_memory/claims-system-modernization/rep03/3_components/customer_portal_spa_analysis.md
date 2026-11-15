## Overview
This system modernizes a 30-year-old regional insurance claims platform by gradually migrating claim types from an on-premise mainframe to a modern Azure cloud environment. It provides a secure online portal for customers and brokers while maintaining legacy system integration for up to three years.

## Key Elements
- Customers
- Brokers
- Claims Adjusters
- New Insurance Claims Platform
- Legacy Mainframe (COBOL/DB2)
- Identity Provider (Active Directory / Azure AD)
- Notification Service (SendGrid/Twilio)
- Customer Portal SPA (Azure Static Web Apps, React/TypeScript)
- API Gateway (Azure API Management)
- Claims Processing Core & BFF (Azure Kubernetes Service)
- Routing & Reconciliation Service (Azure Kubernetes Service + Azure Cosmos DB)

## Relationships
- Customers -> Customer Portal SPA (HTTPS/WSS)
- Brokers -> Customer Portal SPA (HTTPS/WSS)
- Claims Adjusters -> New Insurance Claims Platform (HTTPS/WSS)
- New Insurance Claims Platform -> Identity Provider (OpenID Connect / OAuth 2.0)
- New Insurance Claims Platform -> Legacy Mainframe (Azure Service Bus over Azure ExpressRoute/VPN)
- New Insurance Claims Platform -> Notification Service (HTTPS REST API)
- Customer Portal SPA -> API Gateway (HTTPS REST/GraphQL)
- API Gateway -> Claims Processing Core & BFF (HTTPS / mTLS)
- Claims Processing Core & BFF -> Routing & Reconciliation Service (Internal gRPC/REST)
- Routing & Reconciliation Service -> Legacy Mainframe (Azure Service Bus over Azure ExpressRoute/VPN)

## Technology Stack
- Azure Static Web Apps: Hosts the React/TypeScript Customer Portal SPA with global CDN and automated GitHub Actions CI/CD to mitigate low cloud experience.
- Azure API Management: Acts as API Gateway enforcing OAuth 2.0 validation, rate limiting, and circuit breaking.
- Azure Kubernetes Service: Runs Claims Processing Core & BFF and Routing & Reconciliation Service to standardize backend compute.
- Azure Cosmos DB: Stores reconciliation data for zero-loss claims tracking.
- Azure SignalR Service: Manages real-time claim status updates without raw WebSocket operational overhead.

## Rationale
This hybrid architecture isolates expensive mainframe interactions while gradually migrating workloads to Azure over three years. It ensures zero data loss during migration, maintains sub-two-second adjuster screen performance, and satisfies strict security and maintainability requirements.