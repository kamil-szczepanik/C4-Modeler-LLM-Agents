## Overview
[The Anti-Corruption Layer & Integration container bridges the modern Azure platform and the legacy mainframe during the hybrid migration. Its core purpose is translating data, handling failures, and securing communications to protect legacy stability.]

## Key Elements
- Route Mediator (Apache Camel)
- Mainframe Adapter (JCA/MQ Client)
- Dead-Letter & Audit Handler (Azure Functions & Azure SQL Ledger)
- Operations/Migration Managers (Internal Users)
- Legacy Mainframe System

## Relationships
- Route Mediator -> Mainframe Adapter: Internal Reactive Streams / In-memory Queue
- Mainframe Adapter -> Legacy Mainframe System: IBM MQ (AMQP/JMS) over mTLS with circuit breakers
- Route Mediator -> Dead-Letter & Audit Handler: Azure Service Bus Dead-Letter Queues and Azure Event Grid
- Operations/Migration Managers -> Dead-Letter & Audit Handler: Azure AD SSO (R-07) and RBAC for failure metrics

## Technology Stack
- Apache Camel: Content-based routing and domain event translation
- IBM MQ: Secure asynchronous transport to the legacy system
- Azure SQL Ledger: Tamper-resistant, immutable audit logging for compliance and consistency (R-04)
- Azure Key Vault: Manages mTLS certificates and credentials with automatic rotation
- Azure Service Bus: Decoupled message ingestion and dead-letter queue management

## Rationale
[This architecture shields the brittle mainframe from unstable traffic while preventing modern cloud services from failing due to legacy latency. It enforces strict consistency (R-04) and operational visibility to ensure seamless, gradual claim-type migrations.]