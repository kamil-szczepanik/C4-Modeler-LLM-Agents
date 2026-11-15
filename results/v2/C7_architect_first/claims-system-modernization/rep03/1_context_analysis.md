## Overview
Gradually replaces a 30-year-old mainframe claims system with a modern hybrid cloud platform while ensuring uninterrupted legacy processing. The architecture decouples real-time user experiences from mainframe batch constraints using asynchronous integration messaging.

## Key Elements
- **Users**: Customers, Brokers, and Claims Adjusters.
- **New Claims Platform**: Azure West Europe hosted system utilizing Azure App Service for microservices.
- **Legacy Mainframe System**: On-premise COBOL/DB2 system of record.
- **Corporate Active Directory**: On-premise identity provider for authentication.
- **Integration Middleware**: Azure Service Bus featuring Dead-Letter Queues (DLQ) and Replay Management.
- **Network Infrastructure**: Hybrid Network Gateway via Azure ExpressRoute/VPN.

## Relationships
- **Users to New Claims Platform**: HTTPS via TLS 1.3, utilizing OpenID Connect (OIDC) and OAuth 2.0 for SSO.
- **New Claims Platform to Active Directory**: LDAPS / SAML for identity federation.
- **New Claims Platform to Legacy Mainframe**: Encrypted asynchronous messaging via Azure Service Bus over ExpressRoute/VPN using mTLS and AES-256 payload encryption.

## Technology Stack
- **Azure App Service**: Selected for containerized microservices to reduce operational overhead given the team's low cloud experience.
- **Azure Service Bus**: Chosen over Kafka for lower operational complexity in managing asynchronous claim state replication.
- **Azure Managed Databases with Customer-Managed Keys (CMK)**: Ensures encrypted PII storage via Azure Key Vault.
- **Azure ExpressRoute/VPN**: Establishes resilient hybrid connectivity with IPsec encryption.

## Rationale
The hybrid architecture isolates expensive mainframe changes and rigid batch windows behind an asynchronous integration broker, satisfying strict consistency and performance rules. Managed Azure services simplify operations for a cloud-inexperienced team while supporting incremental claim-type migrations and rapid rollbacks.