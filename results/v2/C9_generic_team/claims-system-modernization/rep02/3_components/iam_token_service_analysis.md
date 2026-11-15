## Overview
The system is an Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe claims system using a hybrid Azure architecture. Its core purpose is to enable online claim submission and modernized adjuster workflows while maintaining seamless data consistency and zero downtime during the 3-year migration.

## Key Elements
- Users: Customers, Brokers, Claims Adjusters
- External Systems: COBOL/DB2 Mainframe, Corporate Active Directory
- Containers: API Gateway / Anti-Corruption Layer (ACL), Event Broker (Azure Service Bus), Caching / State Store (Azure Redis Cache), Data Synchronization (Azure Functions / WebJobs), Backend-for-Frontend (BFF), Centralized Logging (Azure Monitoring), IAM / Token Service (Azure Identity services), Configuration & Secret Management (Azure Key Vault / App Configuration), Worker Processing (Azure Functions / WebJobs)

## Relationships
- Customers / Brokers -> API Gateway / Anti-Corruption Layer (ACL): Online claim submission [HTTPS / REST]
- Claims Adjuster -> Backend-for-Frontend (BFF): Adjuster application workflows [HTTPS / REST]
- API Gateway / Anti-Corruption Layer (ACL) -> Event Broker (Azure Service Bus): Message publishing [AMQP / MQTT]
- Event Broker (Azure Service Bus) -> Worker / Background Processing (Azure Functions / WebJobs): Asynchronous event consumption [AMQP]
- Backend-for-Frontend (BFF) -> IAM / Token Service (Azure Identity services): Authentication and token exchange [OIDC / OAuth 2.0]
- IAM / Token Service (Azure Identity services) -> Corporate Active Directory: Single Sign-On and directory synchronization [OIDC / SAML / LDAP]
- Worker / Background Processing (Azure Functions / WebJobs) -> COBOL/DB2 Mainframe: Batch data synchronization and legacy integration [SFTP / MQ / DB2 Connect]

## Technology Stack
- Cloud Provider: Azure (Region: West Europe) paired with on-premise mainframe infrastructure for hybrid deployment.
- Identity & Security: Azure AD / Entra ID, Azure Key Vault, and Azure App Configuration for SSO, secrets management, and externalized role-to-permission mapping.
- Integration & Compute: Azure Service Bus for messaging, Azure Functions and WebJobs for serverless worker processing and data synchronization.
- Data & Caching: Azure Redis Cache for state management and high-performance caching.
- Observability: Azure Monitoring for centralized logging, audit trails, and health probes.

## Rationale
This hybrid architecture isolates the expensive-to-change COBOL/DB2 mainframe behind an Azure-based Anti-Corruption Layer while incrementally migrating claim types without disrupting operations. Leveraging managed Azure cloud services minimizes operational complexity for a team with limited cloud experience while satisfying strict hybrid security and performance requirements.