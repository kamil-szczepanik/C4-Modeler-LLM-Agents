## Overview
The Insurance Claims Modernization system gradually replaces a legacy COBOL/DB2 mainframe with a modern Azure cloud platform. It ensures seamless hybrid operations while maintaining legacy system of record status.

## Key Elements
- Customers & Brokers
- Claims Adjusters
- API Gateway / Edge (Azure API Management)
- Claims Web App (React on Azure Static Web Apps)
- Claims Core Service (Java / Spring Boot on Azure App Service)
- Message Broker (Azure Service Bus with Topic Router, Dead-Letter Queue Manager, Session Processor, Subscription Filter Engine, Broker Authorization Filter, Message TTL & Archival Policy Engine, Telemetry & Audit Forwarder, Partition Controller)
- Anti-Corruption Layer (Azure Functions)
- Modern Claims Database (Azure SQL Database)
- Read-Through Cache (Azure Cache for Redis)
- On-Premise Integration Agent
- Audit & Reconciliation Worker (Java / Spring Batch)
- Active Directory (On-Premises)
- Legacy Mainframe (COBOL/DB2)

## Relationships
- Customers & Brokers -> API Gateway / Edge: Submits claims [HTTPS / TLS 1.3]
- Claims Adjusters -> Claims Web App: Manages claims [HTTPS / TLS 1.3]
- API Gateway / Edge -> Claims Core Service: Routes API requests [HTTPS / REST]
- Claims Web App -> Active Directory: Authenticates users [OpenID Connect / OAuth 2.0]
- Claims Core Service -> Modern Claims Database: Persists claim data [T-SQL / JDBC over TLS]
- Claims Core Service -> Read-Through Cache: Retrieves cached claims [Redis Protocol over TLS]
- Claims Core Service -> Message Broker: Publishes and consumes asynchronous events [AMQP 1.0 over TLS]
- Message Broker -> Anti-Corruption Layer: Forwards legacy-bound events [AMQP 1.0 over TLS]
- Anti-Corruption Layer -> On-Premise Integration Agent: Transforms payloads for legacy [HTTPS / REST]
- On-Premise Integration Agent -> Legacy Mainframe: Syncs claim data [DB2 / LUW Protocols]
- Message Broker -> Audit & Reconciliation Worker: Publishes broker state metrics [AMQP 1.0 over TLS]
- Audit & Reconciliation Worker -> Modern Claims Database: Verifies data consistency [T-SQL / JDBC]

## Technology Stack
- Azure API Management: Provides edge security, rate limiting, and API routing.
- React on Azure Static Web Apps: Delivers a responsive, low-latency UI for claims adjusters.
- Java / Spring Boot on Azure App Service: Powers scalable core business logic and claims processing.
- Azure Service Bus: Manages reliable, ordered asynchronous messaging and native deduplication.
- Azure SQL Database: Provides relational storage for migrated modern claims.
- Azure Cache for Redis: Accelerates screen load times to under 2 seconds.
- Azure Functions: Implements lightweight Anti-Corruption Layer transformations.
- Java / Spring Batch: Executes audit and reconciliation tasks.

## Rationale
The hybrid architecture isolates the expensive legacy mainframe while enabling incremental claim-type migration over three years. Asynchronous messaging via Azure Service Bus guarantees strict consistency and zero data loss across the cloud-mainframe boundary.