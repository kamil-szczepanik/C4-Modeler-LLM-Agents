## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a secure, cloud-based platform on Azure West Europe. It ensures seamless hybrid operations while maintaining legacy compatibility for unmigrated claim types.

## Key Elements
- **Users**: Customers, Brokers, Claims Adjusters, Migration Operations Managers.
- **External Systems**: Legacy Mainframe, Anti-Corruption Layer (ACL), Active Directory, Payment Gateway, Notification Service.
- **Containers**: React Web Application, .NET Core Operations BFF & Admin Portal, .NET Core Claims API Gateway, .NET Core Claims Processing Service, Azure SQL Database, Azure Service Bus / Apache Kafka, Azure Key Vault.
- **Components (Claims Processing Service)**: Claim State Machine & Orchestrator, Idempotency & Deduplication Filter, Payment & Notification Integrator, Mainframe Sync Adapter, Claim Type Policy Engine.

## Relationships
- **Claims API Gateway -> Claims Processing Service**: Forwards verified business requests via gRPC with mTLS.
- **Claims Processing Service -> Azure SQL Database**: Persists claim state and deduplication hashes using TDS/SQL over TLS 1.3.
- **Claims Processing Service -> Azure Service Bus / Apache Kafka**: Publishes and consumes asynchronous event streams using AMQP over TLS 1.3.
- **Claims Processing Service -> Anti-Corruption Layer**: Synchronizes hybrid state using AMQP and message-level signing.
- **Claims Processing Service -> Payment Gateway**: Executes financial transactions via HTTPS/REST.
- **Claims Processing Service -> Notification Service**: Triggers alerts via Azure Service Bus and HTTPS.

## Technology Stack
- **Azure Container Apps / App Service**: Hosts microservices and web frontends for scalable cloud deployment.
- **.NET Core (C#)**: Powers backend microservices, leveraging MediatR for in-process CQRS messaging and MassTransit for distributed orchestration.
- **Azure SQL Database**: Stores relational claim data and idempotency hashes with application-layer PII encryption.
- **Azure Service Bus**: Handles reliable, asynchronous event-driven messaging with retry policies.
- **Azure Key Vault & Managed Identities**: Secures runtime secrets, API keys, and certificate management without hardcoding.

## Rationale
This hybrid architecture decouples modern claim types from the legacy mainframe via a policy-driven orchestration engine, fulfilling incremental migration (R-03) and one-day rollback (R-06) requirements. Robust idempotency filters, Azure AD authentication, and TLS 1.3 encryption guarantee transactional consistency (R-04) and enterprise security (R-07) without exceeding the quarterly mainframe change constraint.