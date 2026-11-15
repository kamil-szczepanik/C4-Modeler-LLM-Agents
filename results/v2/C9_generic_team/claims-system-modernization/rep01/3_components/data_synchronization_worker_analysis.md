## Overview
- This system incrementally modernizes a legacy insurance claims platform by migrating claim types from an on-premises mainframe to an Azure-hosted cloud environment.
- The architecture guarantees data consistency, zero data loss, and seamless hybrid integration while the legacy system remains the system of record.

## Key Elements
- Customers and Brokers: External users submitting online claims.
- Claims Adjusters: Internal users managing claims via the web application.
- On-Premises COBOL/DB2 Mainframe: Legacy system of record processing unmigrated claims.
- API Gateway: Azure Hosted API Gateway managing incoming traffic.
- Claim Ingestion & Validation Module: .NET Core / Modular Monolith handling online submissions.
- Anti-Corruption Layer (ACL): .NET Core / Modular Monolith translating messages between Azure and the mainframe.
- Read-Model Cache: Azure Cache / In-Memory Database providing fast read access for adjusters.
- Data Synchronization Worker: .NET Background Worker executing asynchronous state updates.
- Azure Service Bus: Messaging broker for asynchronous communication.
- Azure App Configuration: Centralized feature flag and configuration management.
- Azure Monitor / Application Insights: Centralized observability and audit logging.

## Relationships
- Customers and Brokers -> API Gateway: Submit claims via HTTPS/REST.
- API Gateway -> Claim Ingestion & Validation Module: Forward requests via gRPC/REST.
- Claim Ingestion & Validation Module -> Azure Service Bus: Publish claim events via AMQP.
- Data Synchronization Worker -> Azure Service Bus: Consume and process synchronization messages via AMQP.
- Data Synchronization Worker -> Read-Model Cache: Update claim states via TCP/Redis Protocol.
- Anti-Corruption Layer (ACL) -> On-Premises Mainframe: Bridge legacy protocols via TCP/IP.

## Technology Stack
- Azure Service Bus: Asynchronous message broker chosen for reliable decoupled communication and dead-letter queue support.
- .NET Background Worker: Core processing technology selected for implementing the Data Synchronization Worker with native async/await support.
- Azure Cache / In-Memory Database: High-performance caching layer used to meet sub-2-second adjuster screen load requirements.
- Azure App Configuration: Centralized store selected to manage feature flags for rapid claim-type rollbacks.
- Application Insights / Azure Monitor: Observability suite utilized for distributed tracing with correlation IDs and PII scrubbing.

## Rationale
- The hybrid architecture uses an Anti-Corruption Layer and asynchronous background workers to isolate the fragile legacy mainframe from modern cloud components.
- Proven patterns like the Outbox Pattern, idempotency keys, and circuit breakers ensure strict data consistency and fault tolerance despite limited team cloud experience.