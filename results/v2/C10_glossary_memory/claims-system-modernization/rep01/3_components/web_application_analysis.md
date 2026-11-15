## Overview
The Insurance Claims Modernization platform is a hybrid cloud-native system gradually replacing a 30-year-old on-premise mainframe with a modern Azure-hosted platform. It ensures zero-loss, continuous claim processing during a 3-year transition while supporting online submissions and adjuster workflows.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- Web Application (React / TypeScript & Next.js)
- Customer Portal (React / TypeScript & Next.js)
- Claim Processing API (Azure Container Apps)
- Integration Gateway / ACL (Azure Container Apps)
- Feature Flag / Migration Router (Azure Container Apps)
- Document & Audit Store (Azure Blob Storage & Azure Cosmos DB)
- Legacy Mainframe (COBOL/DB2)
- Azure AD (Entra ID)
- Payment Gateway
- Core Notification Service
- Enterprise Service Bus (ESB/MQ)

## Relationships
- Customers & Brokers -> Web Application: Submit claims and interact with portals [HTTPS (REST/GraphQL)]
- Claims Adjusters -> Web Application: Handle claims via UI [HTTPS]
- Web Application -> Claim Processing API: Forwards backend queries and operations [HTTPS (REST/GraphQL) with mTLS]
- Web Application -> Azure AD (Entra ID): Authenticate users and authorize access [OpenID Connect / OAuth 2.0 via HTTPS]
- Claim Processing API -> Integration Gateway / ACL: Sends messages asynchronously [Enterprise Service Bus (ESB/MQ) over AMQP/MQTT with mTLS]
- Integration Gateway / ACL -> Legacy Mainframe: Interfaces with legacy system [Hybrid ESB/MQ connection]
- Claim Processing API -> Payment Gateway: Processes automated payouts [HTTPS (REST with OAuth 2.0)]

## Technology Stack
- Next.js & React / TypeScript: Powers the Web Application and Customer Portal for responsive UI and BFF architecture.
- Azure Container Apps (ACA): Hosts microservices to abstract Kubernetes complexity for a team with limited cloud experience.
- Azure Blob Storage & Azure Cosmos DB: Provides secure, scalable document and audit data storage.
- Enterprise Service Bus (ESB/MQ): Decouples modern cloud components from the on-premise mainframe.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while delivering sub-second adjuster UI responses through caching and optimistic updates. It minimizes operational risk for a cloud-novice team by leveraging managed serverless container infrastructure on Azure.