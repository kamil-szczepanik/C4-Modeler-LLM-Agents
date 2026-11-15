## Overview
[Insurance Claims Modernization platform, system, context]: A hybrid cloud-native platform gradually replacing an on-premise mainframe system while ensuring continuous, zero-loss claim processing during a 3-year transition. It bridges modern web interfaces with a legacy COBOL backend.

## Key Elements
- Web Application [container, container] (React / TypeScript & Next.js): Powers responsive adjuster and customer web interfaces.
- Customer Portal [container, container] (React / TypeScript & Next.js): Provides customer-facing interactions and claim submissions.
- Claim Processing API [container, container] (Azure Container Apps): Handles core business logic for processing claims and orchestrating workflows.
- Integration Gateway / ACL [container, container] (Azure Container Apps): Translates modern messages into legacy formats and interfaces with the mainframe.
- Feature Flag / Migration Router [container, container] (Azure Container Apps): Routes requests dynamically to support the 3-year transition strategy.
- Document & Audit Store [container, container] (Azure Blob Storage & Azure Cosmos DB): Provides secure, cloud-native document and audit data storage.
- Legacy Mainframe [externalSystem, container]: On-premise COBOL/DB2 system of record with a 3-year retention constraint.
- Azure AD (Entra ID) [externalSystem, container]: Identity provider for Single Sign-On and RBAC.

## Relationships
- Customers & Brokers -> Customer Portal: HTTPS (REST/GraphQL)
- Claims Adjusters -> Web Application: HTTPS
- Web Application -> Claim Processing API: HTTPS (REST/GraphQL)
- Claim Processing API -> Integration Gateway / ACL: Asynchronous messaging via Enterprise Service Bus (ESB/MQ) over AMQP/MQTT with mTLS
- Integration Gateway / ACL -> Legacy Mainframe: Hybrid ESB/MQ connection
- Web Application -> Azure AD (Entra ID): OpenID Connect / OAuth 2.0 via HTTPS
- Claim Processing API -> Document & Audit Store: HTTPS / TLS 1.3 (Azure SDK)

## Technology Stack
- Azure Container Apps: Chosen for microservices orchestration with minimal cloud management overhead.
- React / TypeScript & Next.js: Selected for modern, responsive, and type-safe frontend web interfaces.
- Azure Cosmos DB & Azure Blob Storage: Implemented for transactional outbox persistence and secure document storage.
- Enterprise Service Bus (ESB/MQ): Utilized for reliable, asynchronous hybrid messaging with the legacy mainframe.
- Azure AD (Entra ID): Deployed for secure Single Sign-On and role-based access control.

## Rationale
The hybrid architecture isolates the fragile on-premise Legacy Mainframe behind an Integration Gateway / ACL, ensuring uninterrupted operations during the 3-year migration. Asynchronous messaging via ESB/MQ combined with transactional outboxes satisfies strict zero-loss consistency and performance requirements.