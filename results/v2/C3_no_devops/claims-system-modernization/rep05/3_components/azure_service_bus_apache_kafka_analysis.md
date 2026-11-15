## Overview
This hybrid system gradually replaces a legacy COBOL/DB2 mainframe claims system with a modern Azure cloud platform over a three-year period. It ensures zero data loss, secure online claim submission, and high-performance adjuster workflows while maintaining seamless integration with the legacy system.

## Key Elements
- Customers, Brokers, Claims Adjusters, and Migration Operations Managers
- Web Application (React/Next.js on Azure App Service)
- Claims API Gateway / Backend-for-Frontend (.NET Core on Azure Container Apps)
- Claims Processing Service (.NET Core Web API on Azure Container Apps)
- Operations BFF & Admin Portal (.NET Core / React)
- Anti-Corruption Layer (ACL) (Azure Container Apps / On-Prem VM)
- Azure Service Bus (Premium Tier) with topics (`claim-events`), subscriptions (`claims-processing-sub`, `acl-sync-sub`), and Dead-Letter Queues (DLQ)
- Azure SQL Database and Azure Key Vault with Managed Identities
- On-premises COBOL/DB2 Legacy Mainframe
- Azure Monitor / Application Insights

## Relationships
- Web Application -> Claims API Gateway: Forwards online claim submissions [HTTPS/REST]
- Claims Processing Service -> Azure Service Bus: Publishes and consumes asynchronous event streams [AMQP 1.0]
- Anti-Corruption Layer (ACL) -> On-Premises Mainframe: Bridges hybrid data synchronization [TCP/IP / MQ]
- Azure Service Bus -> Azure Monitor: Streams operational metrics and dead-letter logs [HTTPS]

## Technology Stack
- **Azure Service Bus (Premium Tier):** Chosen over Apache Kafka to reduce operational complexity for a low-cloud-experience team while providing AMQP 1.0 support, duplicate detection, and dead-lettering.
- **Azure Container Apps & App Service:** Provides managed, scalable hosting for microservices and frontend applications.
- **.NET Core:** Standardized backend framework for high performance and rapid feature delivery.
- **Azure Monitor & Application Insights:** Enables telemetry, metric alerts, and dead-letter queue monitoring for operational compliance.
- **Managed Identities & Azure Key Vault:** Secures inter-service authentication and manages encryption keys without hardcoded credentials.

## Rationale
Standardizing on Azure Service Bus minimizes operational risk for a team with limited cloud experience while satisfying strict consistency (R-04) and one-day rollback (R-06) requirements. The hybrid architecture securely bridges on-premises mainframe operations with modern cloud scalability using robust Azure security controls.