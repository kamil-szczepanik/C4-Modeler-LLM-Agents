## Overview
[The system is a hybrid cloud insurance claims modernization platform that gradually replaces a 30-year-old mainframe while ensuring continuous legacy claim processing.]

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- Legacy Mainframe (COBOL/DB2)
- Azure API Management
- Customer Portal & Adjuster Workspace (React SPA & Node.js BFF)
- Claims Core Engine (Java Spring Boot)
- Integration Mediator (Azure Logic Apps / Function App)
- Azure Service Bus with Claims Topic, Migration Routing Filters, and Dead-Letter Subscriptions
- Polyglot Persistence Layer (Azure Cosmos DB / PostgreSQL)
- Active Directory / Identity Provider
- Migration Operations Dashboard

## Relationships
- End Customers & Brokers -> Azure API Management: Online claim submission [HTTPS / OIDC]
- Claims Adjusters -> Azure API Management: Adjuster claim handling [HTTPS / OAuth2]
- Azure API Management -> Customer Portal & Adjuster Workspace: Routes frontend traffic [HTTPS]
- Customer Portal & Adjuster Workspace -> Claims Core Engine: API requests [REST / HTTPS]
- Claims Core Engine -> Azure Service Bus: Publishes claims and handles sessions [AMQP over TLS]
- Integration Mediator -> Azure Service Bus: Mediates legacy routing [AMQP over TLS]
- Claims Core Engine & Integration Mediator -> Legacy Mainframe: Data synchronization and batch processing [DB2 / SNA / Batch]

## Technology Stack
- Azure Service Bus: Enterprise messaging backbone chosen for managed reliability, duplicate detection, and Dead-Letter Queues (DLQs).
- React SPA & Node.js BFF: Modern frontend and backend-for-frontend powering adjuster screens and customer portals.
- Java Spring Boot: Core business logic processing container.
- Azure Cosmos DB / PostgreSQL: Polyglot persistence layer for modern data storage.
- Infrastructure as Code (Bicep/Terraform): Automated deployments to mitigate risks from low cloud experience.

## Rationale
[This hybrid architecture isolates the legacy mainframe behind managed integration layers while modernizing the user-facing platform with cloud-native components. It guarantees transactional consistency and rapid rollback capabilities necessary for a phased, low-risk migration.]