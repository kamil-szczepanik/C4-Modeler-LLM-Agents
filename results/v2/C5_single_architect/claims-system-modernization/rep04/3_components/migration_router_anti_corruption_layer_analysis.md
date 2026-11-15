## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure cloud platform while maintaining hybrid operations. The architecture uses a dedicated Anti-Corruption Layer to ensure zero data loss, fast rollbacks, and seamless claim routing.

## Key Elements
* **Claim Routing Engine**: Evaluates incoming claims to determine target processing pathways.
* **Translation Service**: Translates domain models to legacy COBOL-compatible formats.
* **Dual-Write & Reconciliation Manager**: Prevents double-processing and guarantees transactional consistency.
* **Fallback & Feature Flag Manager**: Handles dynamic routing rules and rapid rollback configurations.

## Relationships
* **API Gateway / BFF** -> **Claim Routing Engine**: [HTTPS/REST]
* **Claim Routing Engine** -> **Translation Service**: [In-Process]
* **Claim Routing Engine** -> **Fallback & Feature Flag Manager**: [In-Process]
* **Translation Service** -> **Mainframe Integration Adapter**: [AMQP via Azure Service Bus]
* **Dual-Write & Reconciliation Manager** -> **Azure SQL Database**: [TDS]

## Technology Stack
* **.NET Core / C#**: Selected for core component implementation to align with the BFF and address the team's limited cloud experience.
* **Azure Container Apps**: Hosts the containerized microservices for scalable hybrid deployment.
* **Azure Service Bus**: Manages messaging between cloud and on-premise mainframe integration layers via AMQP/HTTPS.
* **Azure SQL Database**: Stores modern platform claims data via TDS protocol.
* **Azure App Configuration**: Stores dynamic routing rules and feature flags for rapid rollbacks.

## Rationale
This component-level architecture isolates brittle legacy mainframe dependencies within an Anti-Corruption Layer, satisfying strict consistency and one-day rollback requirements. Utilizing managed Azure services and .NET Core minimizes cloud complexity for an inexperienced team.