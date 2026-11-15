## Overview
The system incrementally modernizes a legacy regional insurance claims platform by migrating COBOL/DB2 workflows to a hybrid Azure cloud environment. It enables online customer submissions and rapid adjuster processing while keeping the mainframe as the system of record.

## Key Elements
* Customer / Broker and Claims Adjuster (External Users)
* Active Directory / Azure AD (Identity Provider)
* Mainframe COBOL/DB2 System (On-Premises System of Record)
* Customer Portal SPA (Azure Static Web Apps)
* Adjuster Web App (Azure App Service)
* Claims Core API (Azure Container Apps)
* Integration Gateway / ACL (Azure API Management / Azure Functions)
* Azure Cache for Redis (Distributed Caching)
* Azure Service Bus (Messaging with Dead-Letter Queues)
* Azure Cosmos DB / SQL Database (Modern Data Tier)

## Relationships
* Customer/Broker to Customer Portal SPA via HTTPS (R-01)
* Claims Adjuster to Adjuster Web App via HTTPS (R-02)
* Customer Portal SPA and Adjuster Web App to Claims Core API via HTTPS/REST
* Claims Core API to Azure Cosmos DB / SQL Database via TCP/TLS
* Claims Core API to Integration Gateway via HTTPS/gRPC
* Integration Gateway to Mainframe COBOL/DB2 via IBM MQ / TN3270 / TCP
* Claims Core API to Azure Service Bus via AMQP (R-04)
* Adjuster Web App to Azure Cache for Redis via TCP (R-05)
* Applications to Active Directory via OIDC / OAuth2 (R-07)

## Technology Stack
* Azure Static Web Apps / Azure App Service: Out-of-the-box PaaS hosting to accommodate the team's low cloud experience.
* Azure Container Apps: Microservices container runtime for Claims Core API and gradual claim type migration (R-03).
* Azure API Management / Azure Functions: Integration Gateway / Anti-Corruption Layer to protect the mainframe from frequent interface changes.
* Azure Cache for Redis: Distributed caching to achieve sub-2-second adjuster screen loads despite slow mainframe responses (R-05).
* Azure Service Bus: Reliable messaging with dead-letter queues to ensure zero data loss during hybrid sync (R-04).
* Azure Cosmos DB / SQL Database: Modern persistence tier for newly migrated claim types.

## Rationale
The hybrid architecture protects brittle legacy interfaces by isolating them behind an Anti-Corruption Layer, ensuring stable operations within strict batch window and change frequency constraints. Leveraging Azure PaaS solutions mitigates the team's low cloud experience while delivering high-performance adjuster workflows and seamless data consistency.