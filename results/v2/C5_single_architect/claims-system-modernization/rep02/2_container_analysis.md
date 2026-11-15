## Overview
Gradually replaces a 30-year-old mainframe claims system with a modern hybrid cloud platform using a strangler-fig pattern. It allows incremental claim type migration while maintaining continuity and strict performance constraints.

## Key Elements
* **Customer Portal:** Vue.js/React on Azure Static Web Apps for online claim submissions.
* **Adjuster Workspace:** Azure App Service (Node.js/Java BFF) for handling claims.
* **Migration Router / Anti-Corruption Layer:** Azure Container Apps for dynamic claim routing and rollbacks.
* **Claims Core API:** Azure Container Apps microservices backed by Azure SQL.
* **Integration Gateway & Sync Worker:** Azure Functions for mainframe mediation and batch reconciliation.
* **External Systems:** On-premise COBOL/DB2 Legacy Mainframe and Active Directory.

## Relationships
* **Customers & Brokers** -> **Customer Portal**: HTTPS for claim submission.
* **Claims Adjusters** -> **Adjuster Workspace**: HTTPS with Active Directory SSO.
* **Customer Portal & Adjuster Workspace** -> **Migration Router**: HTTPS/REST.
* **Migration Router** -> **Claims Core API**: Internal REST/gRPC for migrated claims.
* **Migration Router & Sync Worker** -> **Integration Gateway**: HTTPS/SOAP to Legacy Mainframe.
* **Integration Gateway** -> **Legacy Mainframe**: DB2/Batch protocols.

## Technology Stack
* **Azure Container Apps:** Hosts microservices and router to minimize cloud complexity for inexperienced teams.
* **Azure Static Web Apps & App Service:** Delivers fast frontend and BFF responses (<2s).
* **Azure SQL:** Provides consistent transactional storage for migrated claims.
* **Azure Service Bus:** Decouples services to handle slow mainframe responses.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies behind an anti-corruption layer while meeting strict performance, consistency, and rapid-rollback requirements. It successfully accommodates the team's limited cloud experience via managed Azure serverless and container services.