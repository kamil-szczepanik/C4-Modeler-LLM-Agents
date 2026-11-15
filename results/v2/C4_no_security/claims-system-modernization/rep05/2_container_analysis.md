## Overview
The system is a hybrid cloud insurance claims modernization platform that gradually migrates claim types from a 30-year-old mainframe to Azure. It ensures business continuity and zero data loss during a mandatory 3-year dual-run period.

## Key Elements
- **End Customers & Brokers**: External users submitting online claims via the web interface.
- **Claims Adjusters**: Internal users managing claims in the new web application.
- **Claims Web Application**: React Single Page Application hosted on Azure Static Web Apps.
- **API Gateway**: Azure API Management enforcing SSO via Corporate Active Directory.
- **Claims Core Service**: .NET 8 / C# containerized application running on Azure Kubernetes Service (AKS), implementing domain logic and the Inbox/Outbox pattern.
- **Anti-Corruption Layer (ACL)**: Component within the Claims Core Service managing incremental claim-type routing to the mainframe.
- **Integration & Sync Engine**: Azure Service Bus bridging modern event flows with the legacy batch window.
- **Modern Claims Database**: Azure SQL Database / Cosmos DB providing ACID compliance and dual-run state persistence.
- **Legacy Mainframe**: COBOL/DB2 on-prem system acting as the system of record.

## Relationships
- End Customers & Brokers interact with the Claims Web Application via HTTPS.
- Claims Web Application communicates with the API Gateway via REST/HTTPS.
- API Gateway routes requests to the Claims Core Service on AKS via internal REST/gRPC.
- Claims Core Service persists data in the Modern Claims Database using SQL/Cosmos protocols.
- Claims Core Service publishes asynchronous events to Azure Service Bus via AMQP.
- Integration & Sync Engine synchronizes data with the Legacy Mainframe via batch file transfers and secure file protocols during the 23:00–05:00 window.

## Technology Stack
- **Frontend**: React via Azure Static Web Apps for sub-2-second UI responsiveness.
- **API Management**: Azure API Management for managed entry points and Active Directory SSO integration.
- **Backend**: .NET 8 / C# running on Azure Kubernetes Service (AKS) to unify the runtime stack for a team with low cloud experience.
- **Messaging**: Azure Service Bus with dead-letter queues for reliable hybrid message delivery.
- **Database**: Azure SQL Database / Cosmos DB for transactional consistency and inbox/outbox state persistence.

## Rationale
The hybrid architecture decouples modern web experiences from the legacy mainframe via an Anti-Corruption Layer and Inbox/Outbox pattern, guaranteeing zero lost claims (R-04) and rapid one-day rollbacks (R-06). Standardizing on .NET and managed Azure services minimizes operational complexity for a team with limited cloud expertise while meeting strict performance (R-05) and security (R-07) constraints.