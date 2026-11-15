## Overview
The Insurance Claims Modernization system gradually replaces a legacy on-premise mainframe claims platform with a modern hybrid cloud architecture in Azure West Europe. It ensures seamless claim processing and data consistency while migrating claim types incrementally over a three-year period.

## Key Elements
* **Users:** Customers, Brokers, and Claims Adjusters
* **Frontend:** Customer Portal (Azure Static Web Apps, React), Adjuster Workspace (Azure Container Apps, Node.js/React)
* **Backend & Logic:** API Gateway (Azure Container Apps), Adjuster Backend Service (Java/Spring Boot) with Anti-Corruption Layer (ACL)
* **Data & Messaging:** Azure SQL Database, Azure Redis Cache, Azure Service Bus (with Dead-Letter Queues)
* **Integration & Security:** Mainframe Integration Adapter, Identity Provider (Active Directory), Azure Key Vault

## Relationships
* **Customers/Brokers** submit claims via HTTPS/JSON to the **Customer Portal** and **API Gateway**.
* **API Gateway** validates OAuth2/OIDC tokens against the **Identity Provider** and routes traffic to backend services.
* **Adjuster Workspace** communicates via REST/HTTPS with the **Adjuster Backend Service**.
* **Adjuster Backend Service** utilizes **Azure Redis Cache** for performance and **Azure Service Bus** (AMQP) for asynchronous processing.
* **Mainframe Integration Adapter** connects securely via mTLS to the on-premise **Legacy Mainframe**.

## Technology Stack
* **Azure Container Apps:** Hosts microservices with blue-green deployment revisions for easy rollbacks (R-06).
* **Azure Service Bus:** Manages asynchronous queues and DLQs to prevent claim loss during nightly batch windows (R-04).
* **Azure Redis Cache:** Stores session and temporary data to meet adjuster screen load times under 2 seconds (R-05).
* **Azure SQL Database:** Persists migrated claim types locally using Spring Data JPA.
* **Azure Key Vault:** Centralizes secrets, mTLS certificates, and API keys securely using managed identities.
* **Terraform / Bicep:** Implements Infrastructure as Code to mitigate risks from low cloud experience.

## Rationale
This hybrid architecture isolates the fragile legacy mainframe using an Anti-Corruption Layer and asynchronous queues, ensuring zero claim loss and rapid rollback capabilities. Furthermore, it bypasses mainframe latency bottlenecks with caching and modern cloud services, meeting strict performance and maintainability requirements despite the team's limited cloud experience.