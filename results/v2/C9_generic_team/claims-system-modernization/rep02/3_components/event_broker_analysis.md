## Overview
This architecture establishes a hybrid cloud platform on Azure West Europe to gradually modernize a 30-year-old on-premises COBOL/DB2 mainframe claims system. It ensures zero data loss, high performance, and rapid fallback capabilities while claim types are migrated incrementally.

## Key Elements
- **Users**: Customers, Brokers, Claims Adjusters
- **External Systems**: COBOL/DB2 Mainframe (System of Record), Active Directory
- **Azure Containers**: API Gateway / Anti-Corruption Layer (ACL), Event Broker (Azure Service Bus), Caching / State Store (Azure Redis Cache), Data Synchronization (Azure Functions / WebJobs), Backend-for-Frontend (BFF) web applications, Azure Blob Storage (for large payloads), Automated Schema Registry

## Relationships
- Customers / Brokers -> API Gateway: Online claim submission [HTTPS / TLS]
- Claims Adjuster BFF -> API Gateway -> Event Broker: Asynchronous event-driven migration [AMQP / MQTT]
- Event Broker -> Azure Blob Storage: Payload offloading via Claim Check pattern [HTTPS]
- API Gateway -> Active Directory: Single sign-on authentication [OIDC / OAuth2 / SAML]
- Data Synchronization Service <-> COBOL/DB2 Mainframe: Batch data exchange [SFTP / MQ / DB2 Connect]

## Technology Stack
- **Messaging/Broker**: Azure Service Bus (enables reliable asynchronous messaging and decoupled strangler migration)
- **State/Caching**: Azure Redis Cache (ensures sub-2-second adjuster screen loads despite slow mainframe responses)
- **Storage**: Azure Blob Storage (stores large payloads via Claim Check pattern to bypass broker size limits)
- **Validation**: Azure Schema Registry (prevents payload drift and ensures maintainability during incremental migrations)
- **Identity**: Azure Identity services with Active Directory integration (satisfies SSO security requirements)

## Rationale
The hybrid architecture decouples modern Azure microservices from the legacy mainframe via an asynchronous event broker, protecting system availability and operational budgets. Robust reliability patterns (idempotency, circuit breakers, dead-letter monitoring, and schema validation) mitigate distributed system risks for a cloud-novice team while strictly enforcing data consistency and rapid fallback goals.