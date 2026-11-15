## Overview
[The system is the Claims Integration Service within a hybrid Insurance Claims Modernization platform, designed to gradually migrate legacy COBOL/DB2 mainframe claim types to a modern Azure cloud environment without data loss or downtime.]

## Key Elements
• Routing & Translation Component (.NET Core / JSON-based Rules)
• Mainframe Adapter Component (.NET Core / MQ Client with Polly Circuit Breaker)
• Synchronization & State Worker (.NET Core Background Service)
• Integration API Controller (.NET Core Minimal API)
• State & Outbox Store (Azure Database for PostgreSQL - Flexible Server)
• Configuration Store (Azure App Configuration)
• Secret Management (Azure Key Vault with Managed Identities)

## Relationships
• Azure Service Bus -> Synchronization & State Worker: Receives asynchronous claim messages [AMQP]
• Mainframe Adapter Component -> Legacy Mainframe: Synchronizes data [Secure FTP / MQ over ExpressRoute/IPSec VPN with mTLS]
• Integration API Controller -> Adjuster Workspace: Serves synchronization health and routing status [HTTPS / REST with Azure AD RBAC]
• Synchronization & State Worker -> State & Outbox Store: Persists transactional outbox data [Entity Framework Core with TDE]
• Routing & Translation Component -> Azure App Configuration: Retrieves dynamic claim routing rules [HTTPS with Azure RBAC]

## Technology Stack
• .NET Core: Standardizes development within team skill constraints
• Azure Container Apps: Hosts integration container components with minimal operational overhead
• Azure Database for PostgreSQL (Burstable tier): Provides reliable relational storage for the transactional outbox pattern
• Azure App Configuration: Stores dynamic routing rules securely with zero-code fallback triggers
• Polly: Implements circuit breaker policies to handle mainframe latency and outages

## Rationale
[This architecture enforces strict consistency and zero data loss via an outbox pattern while accommodating low team cloud experience through managed Azure services and standard .NET tech. It guarantees business continuity and compliance with rigid mainframe constraints via modular components and dynamic routing.]