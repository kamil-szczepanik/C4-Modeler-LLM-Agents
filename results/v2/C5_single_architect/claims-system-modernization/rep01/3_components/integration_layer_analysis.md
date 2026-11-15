## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure platform. It uses a hybrid architecture with an Integration Layer to safely migrate claim types while maintaining consistency.

## Key Elements
- **Customers & Brokers:** External users submitting claims online.
- **Claims Adjusters:** Internal users handling claims via the new web application.
- **Legacy Mainframe:** On-premises COBOL/DB2 system of record.
- **Customer Portal:** React SPA on Azure Static Web Apps.
- **Adjuster Workspace:** Node.js Backend-for-Frontend on Azure App Service.
- **Claims Core Engine:** Java Spring Boot on Azure Container Apps.
- **Integration Layer (Azure Event Hubs & Apache Camel):** Contains Routing Mediator, Protocol Translator, Idempotency & Replay Manager (Azure Redis Cache), and Mainframe ACL.
- **Migrated Claims Database:** Azure Database for PostgreSQL.
- **Active Directory:** Insurer's identity provider for SSO.

## Relationships
- **Customers & Brokers -> Customer Portal:** Submits online claims [HTTPS]
- **Claims Adjusters -> Adjuster Workspace:** Manages claims [HTTPS via Azure Front Door]
- **Adjuster Workspace -> Claims Core Engine:** API calls [REST/HTTPS]
- **Claims Core Engine -> Integration Layer:** Publishes claim events [AMQP over Azure Event Hubs]
- **Routing Mediator -> Protocol Translator:** Transforms payload for legacy [In-memory Camel EIP]
- **Protocol Translator -> Mainframe ACL:** Maps canonical events to legacy schemas [Java / Apache Camel]
- **Mainframe ACL -> Legacy Mainframe:** Transfers records [IBM MQ / FTP]
- **Claims Core Engine -> Migrated Claims Database:** Reads/Writes claim data [JDBC over TLS]

## Technology Stack
- **Azure Event Hubs & Apache Camel:** Integration layer backbone for messaging and low operational overhead.
- **Azure Redis Cache:** State store for idempotency, ensuring zero data loss during nightly batch windows.
- **Java / Spring Boot & Azure Container Apps:** Scalable hosting for core processing and routing components.
- **Azure Database for PostgreSQL:** Modern relational database for migrated claim types.
- **Active Directory:** Enterprise identity integration for security compliance (R-07).

## Rationale
This hybrid architecture isolates rigid mainframe dependencies using an Anti-Corruption Layer and robust idempotency management, satisfying strict zero-loss consistency rules (R-04) and rapid rollback requirements (R-06). It accommodates the team's limited cloud experience through managed Azure services while safely modernizing claims processing over a 3-year migration horizon.