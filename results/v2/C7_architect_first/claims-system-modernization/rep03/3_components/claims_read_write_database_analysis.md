## Overview
The system is a modern hybrid claims platform that gradually replaces a 30-year-old mainframe claims system for a regional insurer. Its core purpose is to enable online claim submission and adjuster workflows while maintaining synchronization with the legacy system.

## Key Elements
- **Users**: Customers, Brokers, Claims Adjusters
- **External Systems**: Legacy Mainframe System, Corporate Active Directory
- **Containers**: Customer Portal, Adjuster Workspace, API Gateway, Integration / ACL Service, Claims Read/Write Database, Azure Service Bus
- **Database Components**: Claim Operational Store, Sync State Manager, Audit & Fallback Log, Claim State Machine Tables, Outbox Pattern Table

## Relationships
- Customer Portal -> Claims Read/Write Database: Reads and writes claim data [Azure Managed Identities, SQL over TLS 1.3]
- Adjuster Workspace -> Claims Read/Write Database: Reads and writes claim data [Azure Managed Identities, SQL over TLS 1.3]
- Integration / ACL Service -> Claims Read/Write Database: Synchronizes claim data [Azure Managed Identities, SQL over TLS 1.3]
- Claims Read/Write Database -> Azure Service Bus: Publishes domain events via Outbox Pattern Table [AMQP / HTTPS]

## Technology Stack
- **Azure Database for PostgreSQL (Flexible Server)**: Provides robust ACID compliance, high availability, and automated backups.
- **PostgreSQL 15+**: Utilizes JSONB for flexible attributes, Row-Level Security (RLS), and column-level masking.
- **PgBouncer**: Manages connection pooling for low-latency queries.
- **Azure Key Vault**: Manages Customer-Managed Keys (CMK) for Transparent Data Encryption (TDE).
- **Azure Defender for PostgreSQL & Azure Sentinel**: Provides database activity monitoring and audit logging.

## Rationale
This architecture uses a hybrid database design with local caching and transactional stores to achieve sub-2-second adjuster screen loads despite slow mainframe responses. It incorporates robust outbox patterns and fallback logs to guarantee zero data loss and enable rapid one-day rollback per migrated claim type.