## Overview
[The system modernizes a 30-year-old mainframe claims system by gradually migrating claim types to a hybrid cloud platform while ensuring uninterrupted legacy operations. It enables online claim submissions, modern adjuster workflows, and strict transactional consistency.]

## Key Elements
- **End Customers & Brokers**: External users submitting claims online
- **Claims Adjusters**: Internal users managing claims via a new web application
- **Migration Operations Team**: Users monitoring data reconciliation and rollbacks
- **Azure API Management**: Single entry point handling OIDC/OAuth2 Active Directory SSO
- **Customer Portal & Adjuster Workspace**: React SPAs with a Node.js BFF for performance
- **Claims Core Engine**: Java Spring Boot application for domain logic and claim-type feature flagging
- **Integration Mediator**: Azure Logic Apps/Function App translating events for the legacy mainframe
- **Legacy Mainframe**: COBOL/DB2 on-premise system of record
- **Azure Service Bus**: Enterprise Messaging Queue with Dead-Letter Queues (DLQs)
- **Azure Cosmos DB / PostgreSQL**: Polyglot persistence layer with Change Data Capture (CDC)
- **Migration Operations Dashboard**: Dedicated monitoring and reconciliation UI

## Relationships
- **End Customers/Brokers to Customer Portal**: HTTPS (REST/JSON) via Azure API Management
- **Claims Adjusters to Adjuster Workspace**: HTTPS (REST/JSON) via Azure API Management
- **API Gateway to Node.js BFF & Claims Core**: HTTPS (REST/gRPC)
- **Claims Core to Azure Service Bus**: AMQP
- **Claims Core to Legacy Mainframe**: TCP/MQ via Integration Mediator (JSON-to-COBOL copybook mapping)
- **Persistence to Migration Operations Dashboard**: Change Data Capture (CDC)

## Technology Stack
- **Azure Container Apps (ACA)**: Abstracts infrastructure complexity for a team with low cloud experience
- **Azure API Management**: Enforces Active Directory SSO and centralized OIDC/OAuth2 token validation
- **React SPA & Node.js BFF**: Decouples UI loading times (<2s) from slow mainframe responses
- **Java / Spring Boot**: Robust core business logic execution on containerized runtimes
- **Azure Service Bus**: Ensures reliable message delivery with AMQP, DLQs, and automated replays
- **Terraform / Bicep**: Automated infrastructure provisioning for operational consistency

## Rationale
[The hybrid architecture utilizes Azure Container Apps and managed services to reduce operational overhead for a cloud-novice team while safely bridging modern cloud components to the on-premise mainframe. Decoupled SPAs, feature flagging, and CDC-driven dashboards directly fulfill stringent performance, zero data loss, and rapid rollback requirements.]