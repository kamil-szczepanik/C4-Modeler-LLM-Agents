## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-hosted platform. It ensures seamless hybrid operations while the legacy system remains the system of record.

## Key Elements
* **Actors:** Customers, Brokers, and Claims Adjusters
* **External Systems:** On-premises Active Directory and Legacy Mainframe (COBOL/DB2)
* **Modern Claims Platform (Containers):** Customer Portal (Azure App Service), Adjuster Web App (Azure App Service), Anti-Corruption Layer (Azure Functions), and State Database (Azure SQL Database)
* **Messaging:** Azure Event Hubs

## Relationships
* Customers and Brokers interact with the Customer Portal via HTTPS/REST.
* Claims Adjusters access the Adjuster Web App via HTTPS/REST.
* Adjuster Web App communicates with Azure SQL Database via TDS/TCP and the Legacy Mainframe via HTTPS/REST through the ACL to meet the sub-2s UI performance requirement.
* Modern Platform integrates with the Legacy Mainframe asynchronously via AMQP/Azure Event Hubs.
* Authentication with Active Directory utilizes OIDC/OAuth2 protocols.

## Technology Stack
* **Azure App Service:** Hosts web applications due to minimal management overhead for cloud-inexperienced teams.
* **Azure SQL Database:** Stores migrated claim data, providing reliable consistency and transactional integrity.
* **Azure Event Hubs:** Manages asynchronous messaging to decouple systems and respect the quarterly mainframe change constraint.
* **Azure Active Directory (Entra ID):** Enforces single sign-on (R-07) integrated with on-premises identity.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies through an Anti-Corruption Layer while modernizing the user experience in Azure. It guarantees strict consistency and fast UI performance despite legacy latency constraints.