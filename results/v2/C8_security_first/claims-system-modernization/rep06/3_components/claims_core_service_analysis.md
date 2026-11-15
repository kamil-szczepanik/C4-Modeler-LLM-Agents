## Overview
[The system is a modern hybrid Claims Platform that gradually replaces a 30-year-old COBOL/DB2 mainframe claims system while maintaining uninterrupted processing. Its core purpose is to enable online claim submission and adjuster management while ensuring zero data loss and seamless 3-year migration.]

## Key Elements
- Users: Policyholders, Brokers, Claims Adjusters
- External Systems: Legacy Mainframe System of Record, Insurer Active Directory (Entra ID), Enterprise Notification System
- Containers: API Gateway (Azure Front Door / Azure API Management), Claims Web Application (React / Azure App Service), Audit & Reporting Dashboard (React / Azure App Service), Claims Core Service (Node.js/TypeScript on Azure Container Apps), Integration/Sync Service & Read-Model Sync Worker (Azure Service Bus, Azure Functions / .NET)
- Components (Claims Core Service): Command Router & Validation Component, Aggregate Root & Business Logic Engine, Event Store Repository (Azure Cosmos DB), Outbox Publisher Worker, Saga & Compensation Coordinator

## Relationships
- API Gateway -> Claims Core Service: Dynamic routing of requests [gRPC / HTTPS with mTLS and JWT]
- Claims Core Service -> Legacy Mainframe System: Hybrid data sync [MQ/AMQP and mTLS over IPsec VPN / Azure ExpressRoute]
- Claims Core Service -> Integration/Sync Service & Read-Model Sync Worker: Event streaming [AMQP via Azure Service Bus]
- Command Router -> Aggregate Root: Dispatches validated commands [In-memory]
- Aggregate Root -> Event Store Repository: Appends immutable domain events [HTTPS via Azure Cosmos DB SDK]
- Event Store Repository -> Outbox Publisher: Streams uncommitted events [Database Change Feed]
- Outbox Publisher -> Saga Coordinator: Triggers compensation flows on integration failure [Async callback]
- Saga Coordinator -> Azure Service Bus (DLQ): Routes failed business events [AMQP]

## Technology Stack
- Node.js / TypeScript: Core runtime for Claims Core Service for rapid development given limited cloud experience.
- Azure Container Apps: Hosting containerized microservices with built-in revision management for canary deployments.
- Azure Cosmos DB: Event store persistence with customer-managed keys (CMK) for immutability and zero data loss.
- Azure Service Bus: Asynchronous event messaging and Dead-Letter Queue (DLQ) for reliable claim processing.
- Azure Key Vault: Centralized secret management and envelope encryption for PII/financial event payloads.
- Bicep / Terraform: Automated Infrastructure-as-Code (IaC) templates to mitigate team cloud inexperience.
- OpenTelemetry: Distributed tracing across hybrid boundaries for latency diagnostics.

## Rationale
[This hybrid architecture isolates expensive mainframe dependencies while using CQRS, Event Sourcing, and Azure Cosmos DB to guarantee zero data loss and sub-second UI performance. It empowers a low-cloud-experience team with managed cloud services, automated IaC, and robust fallback mechanisms to meet strict migration and security constraints.]