## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure-based hybrid platform. It enables online claim submission and adjuster workflows while ensuring continuous synchronization with the legacy system of record.

## Key Elements
* Claim Aggregate Store (PostgreSQL tables with JSONB)
* Migration Sync Ledger (PostgreSQL relational tables)
* Audit & Fallback Log (PostgreSQL append-only tables)
* Outbox Event Publisher (PostgreSQL Debezium / Logical Decoding)
* Claims Core Engine (Java Spring Boot on Azure Container Apps)
* Integration Layer (Azure Event Hubs with Apache Camel)
* Legacy Mainframe (COBOL/DB2)
* Active Directory

## Relationships
* Claims Core Engine -> Claim Aggregate Store: Persisting claims data [JDBC over TLS]
* Claims Core Engine -> Migration Sync Ledger: Managing sync state [JDBC over TLS]
* Outbox Event Publisher -> Integration Layer (Azure Event Hubs): Publishing domain events [AMQP over TLS]
* Integration Layer -> Legacy Mainframe: Synchronizing claims data [Batch/Interface]
* System -> Active Directory: Single sign-on authentication [OIDC/SAML]

## Technology Stack
* Azure Database for PostgreSQL: Provides relational and JSONB storage for flexible claim types and transactional consistency.
* Debezium / Logical Decoding: Implements the Transactional Outbox pattern for reliable asynchronous event publishing.
* Java Spring Boot on Azure Container Apps: Powers the scalable core business logic engine.
* Azure Event Hubs with Apache Camel: Handles decoupled asynchronous messaging with the on-premise mainframe.

## Rationale
This hybrid architecture isolates the expensive legacy mainframe while modernizing workflows on Azure, satisfying strict constraints for zero data loss and rapid rollbacks. The component design ensures maintainability during the three-year gradual migration phase.