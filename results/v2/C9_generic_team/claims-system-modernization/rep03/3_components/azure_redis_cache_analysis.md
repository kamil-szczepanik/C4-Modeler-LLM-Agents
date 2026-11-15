## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-hosted modular monolith. It enables online claim submissions and adjuster workflows while maintaining transactional consistency during the migration.

## Key Elements
*   Customers and Brokers
*   Claims Adjusters
*   COBOL/DB2 On-Premises Mainframe System of Record
*   Azure Active Directory
*   Azure API Gateway
*   Azure App Service (PaaS)
*   Azure SQL Database
*   Azure Service Bus
*   Azure Redis Cache
*   Azure Application Insights

## Relationships
*   Customers & Brokers -> Azure API Gateway: Submits claims online [HTTPS/TLS]
*   Claims Adjusters -> Azure API Gateway: Manages claims via web app [HTTPS/TLS]
*   Azure App Service -> Azure SQL Database: Reads and writes persistent data [TDS/TCP]
*   Azure App Service -> Azure Redis Cache: Retrieves and caches read models using a cache-aside pattern [Redis Protocol]
*   Azure App Service -> Azure Service Bus: Publishes and consumes domain events [AMQP]
*   Azure App Service -> COBOL/DB2 Mainframe: Synchronizes legacy claim records [Batch/MQ]
*   Azure App Service -> Azure Active Directory: Authenticates users [OpenID Connect/OAuth 2.0]

## Technology Stack
*   **Azure Redis Cache:** Stores transient read models to ensure sub-2-second UI response times.
*   **Azure App Service:** Hosts the modular monolith application logic and shared repository layers.
*   **Azure SQL Database:** Acts as the primary transactional data store for migrated claims.
*   **Azure Service Bus:** Handles asynchronous event-driven messaging and cache invalidation.
*   **Infrastructure as Code (Bicep/Terraform):** Automates secure and consistent cloud provisioning.

## Rationale
This hybrid architecture uses a modular monolith on Azure App Service with Azure Redis Cache to overcome slow mainframe latencies and meet strict performance goals. It minimizes cloud complexity for an inexperienced team while keeping the legacy system functional during the three-year migration.