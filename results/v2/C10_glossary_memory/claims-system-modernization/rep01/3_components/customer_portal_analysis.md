## Overview
The Insurance Claims Modernization platform is a hybrid cloud-native system gradually replacing a 30-year-old on-premise mainframe while ensuring zero-loss claim processing during a 3-year transition. It leverages Azure Container Apps and Next.js to modernize user interfaces while maintaining compatibility with legacy COBOL/DB2 systems.

## Key Elements
- **Customers & Brokers**: External users performing online claim submissions and tracking via the portal.
- **Claims Adjusters**: Internal personnel handling claims through the web application.
- **Customer Portal**: React/TypeScript & Next.js container providing customer-facing interactions, submissions, and broker dashboards.
- **Web Application**: React/TypeScript & Next.js container for adjuster workflows.
- **Claim Processing API**: Azure Container Apps container handling business logic and orchestration.
- **Integration Gateway / ACL**: Azure Container Apps container translating modern messages for the legacy mainframe.
- **Feature Flag / Migration Router**: Azure Container Apps container dynamically routing claim types during the 3-year transition.
- **Document & Audit Store**: Azure Blob Storage & Azure Cosmos DB providing secure document and audit data storage.
- **Legacy Mainframe**: On-premise COBOL/DB2 system of record.
- **Azure AD (Entra ID)**: Identity provider for Single Sign-On and RBAC.

## Relationships
- Customers & Brokers -> Customer Portal: HTTPS (REST/GraphQL)
- Claims Adjusters -> Web Application: HTTPS
- Customer Portal -> Claim Processing API: HTTPS (REST/GraphQL)
- Claim Processing API -> Feature Flag / Migration Router: Internal gRPC / HTTPS
- Claim Processing API -> Integration Gateway / ACL: Asynchronous messaging via Enterprise Service Bus (ESB/MQ) over AMQP/MQTT with mTLS
- Integration Gateway / ACL -> Legacy Mainframe: Hybrid ESB/MQ connection
- Customer Portal -> Azure AD (Entra ID): OpenID Connect / OAuth 2.0 via HTTPS
- Document Upload Client -> Document & Audit Store: HTTPS / Pre-signed URLs (Azure SDK)

## Technology Stack
- **Frontend Framework**: React, TypeScript, and Next.js for responsive adjuster and customer web interfaces.
- **Compute & Orchestration**: Azure Container Apps for scalable microservices and APIs.
- **Database & Storage**: Azure Blob Storage and Azure Cosmos DB for document binaries and audit logs.
- **Authentication**: NextAuth.js with Azure AD (Entra ID) using OpenID Connect / OAuth 2.0.
- **Integration**: Enterprise Service Bus (ESB/MQ) with AMQP/MQTT for asynchronous mainframe decoupling.

## Rationale
The hybrid architecture allows the regional insurer to progressively migrate claim types off the expensive mainframe without disrupting the 23:00-05:00 batch window or risking data loss. Containerized Azure services isolate the legacy system while accommodating the team's low cloud experience through managed components and standard design patterns.