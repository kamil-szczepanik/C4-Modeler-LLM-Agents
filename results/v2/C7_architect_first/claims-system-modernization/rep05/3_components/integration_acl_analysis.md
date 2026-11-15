## Overview
This architecture establishes a hybrid integration layer for modernizing an insurance claims platform while preserving the 30-year-old mainframe. It ensures seamless data synchronization, zero claim loss, and rapid rollbacks during the multi-year migration.

## Key Elements
- **ACL Router & Circuit-Breaker Component**: Java Spring Boot, Resilience4j
- **Data Mapper & Sanitizer Component**: Java Spring Boot, MapStruct, JSON Schema/XML
- **Outbox/Inbox Processor Component**: Java Spring Boot, JDBC/JPA, Azure SQL Database
- **Messaging Infrastructure**: Azure Service Bus topics, Azure Dead-Letter Queues
- **External Systems**: COBOL/DB2 Legacy Mainframe System, Azure Key Vault, Azure Monitor

## Relationships
- **Claims Processing Service -> Outbox/Inbox Processor**: Sends asynchronous domain events via JDBC/JPA
- **Outbox/Inbox Processor -> Azure Service Bus**: Publishes and consumes reliable messages using AMQP protocol
- **ACL Router -> Legacy Mainframe System**: Dynamically routes traffic and synchronizes data via mTLS over restricted interface protocols
- **Outbox/Inbox Processor -> Azure Key Vault**: Retrieves database credentials and certificates using Azure Managed Identities

## Technology Stack
- **Java Spring Boot**: Chosen for team familiarity given limited cloud experience and complex domain mapping requirements.
- **Resilience4j**: Provides circuit-breaking and rate-limiting to protect the fragile legacy mainframe during high loads.
- **Azure Service Bus**: Ensures durable, reliable message queuing and at-least-once delivery during the strict 23:00-05:00 batch window.
- **MapStruct**: Enforces payload schema validation and PII sanitization between modern and legacy data structures.

## Rationale
The architecture guarantees consistency and compliance (R-04, R-07) without losing claims or extending the rigid mainframe batch window. Custom Java components provide the necessary domain logic to achieve rapid, feature-flagged rollbacks of migrated claim types within one day (R-06).