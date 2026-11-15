## Overview
The Insurance Claims Modernization platform is a hybrid cloud-native system gradually replacing a 30-year-old COBOL/DB2 mainframe while ensuring zero-loss claim processing. It enables customers, brokers, and adjusters to interact via modern web interfaces while managing a complex 3-year transition.

## Key Elements
- Customers & Brokers [person]
- Claims Adjusters [person]
- Web Application [container] (React / TypeScript & Next.js)
- Customer Portal [container] (React / TypeScript & Next.js)
- Claim Processing API [container] (Azure Container Apps)
- Integration Gateway / ACL [container] (Azure Container Apps)
- Feature Flag / Migration Router [container] (Azure Container Apps)
- Document & Audit Store [container] (Azure Blob Storage & Azure Cosmos DB)
- Legacy Mainframe [externalSystem]
- Azure AD (Entra ID) [externalSystem]
- Payment Gateway [externalSystem]
- Core Notification Service [externalSystem]
- Enterprise Service Bus (ESB/MQ) [externalSystem]

## Relationships
- Customers & Brokers -> Web Application (HTTPS (REST/GraphQL))
- Customers & Brokers -> Customer Portal (HTTPS (REST/GraphQL))
- Claims Adjusters -> Web Application (HTTPS)
- Web Application -> Claim Processing API (HTTPS (REST/GraphQL))
- Customer Portal -> Claim Processing API (HTTPS (REST/GraphQL))
- Claim Processing API -> Feature Flag / Migration Router (Internal gRPC / HTTPS with mTLS)
- Claim Processing API -> Integration Gateway / ACL (Asynchronous messaging via Enterprise Service Bus (ESB/MQ) over AMQP/MQTT with mTLS)
- Claim Processing API -> Document & Audit Store (HTTPS / TLS 1.3 (Azure SDK))
- Integration Gateway / ACL -> Legacy Mainframe (Hybrid ESB/MQ connection)
- Web Application -> Azure AD (Entra ID) (OpenID Connect / OAuth 2.0 via HTTPS)
- Customer Portal -> Azure AD (Entra ID) (OpenID Connect / OAuth 2.0 via HTTPS)
- Claim Processing API -> Payment Gateway (HTTPS (REST with OAuth 2.0))
- Claim Processing API -> Core Notification Service (Asynchronous Webhooks via Azure Event Grid (HTTPS))

## Technology Stack
- Azure Container Apps: Hosts microservices and routing components with low operational overhead.
- React / TypeScript & Next.js: Powers responsive, high-performance web interfaces for users.
- Azure App Configuration: Stores feature flags securely with built-in geo-replication and managed capabilities.
- Azure Blob Storage & Azure Cosmos DB: Provides secure, cloud-native document and audit data storage.
- Enterprise Service Bus (ESB/MQ): Decouples hybrid cloud messaging safely from the on-premise mainframe.
- Azure AD (Entra ID): Manages Single Sign-On and Role-Based Access Control securely.

## Rationale
The hybrid architecture allows incremental migration of claim types while keeping the legacy mainframe as the system of record to minimize expensive backend changes. Azure-native managed services reduce operational complexity for a team with limited cloud experience while guaranteeing high security and consistency.