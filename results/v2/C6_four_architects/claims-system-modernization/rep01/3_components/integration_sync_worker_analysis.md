## Overview
- Hybrid modern platform gradually replacing a 30-year-old COBOL/DB2 mainframe claims system while maintaining data consistency.
- Integrates cloud-native Azure services with an on-premise mainframe infrastructure for a regional insurer.

## Key Elements
- Users: Customer & Broker, Adjusters
- Containers: Customer Portal (React/SPA), Web Frontend (React/SPA), API Gateway / BFF (Node.js/Express), Claims Core Service (.NET 8/C#), Integration & Sync Worker (C# Azure Function), Claims Database (Azure SQL), Integration Event Broker (Azure Service Bus), Distributed Cache (Azure Redis), Configuration Store (Azure App Configuration)
- Worker Components: Event Consumer, Sync Orchestrator (Durable Functions), Transformation & Mapping Engine, Mainframe Adapter, Resiliency & Retry Policy (Polly), Reconciliation & Audit Logger, Configuration & Feature Flag
- External Systems: Legacy Mainframe (COBOL/DB2), Active Directory / Entra ID Connect

## Relationships
- Customer Portal / Web Frontend -> API Gateway / BFF: HTTPS / REST
- API Gateway / BFF -> Claims Core Service: gRPC / Internal HTTPS
- Claims Core Service -> Integration Event Broker (Azure Service Bus): AMQP
- Integration & Sync Worker -> Legacy Mainframe: Secure SFTP / MQ
- Integration & Sync Worker -> Claims Database (Azure SQL): Entity Framework Core

## Technology Stack
- Frontend: React / TypeScript SPA for user interfaces
- Backend Services: .NET 8 / C# for core services and Azure Functions
- Database: Azure SQL Database Managed Instance for relational persistence
- Messaging: Azure Service Bus for asynchronous event-driven architecture
- Resiliency & Config: Polly for fault tolerance, Azure App Configuration for dynamic feature toggles

## Rationale
- Shared .NET 8 stack minimizes cognitive load for a team with limited cloud experience while ensuring high maintainability.
- Decoupled architecture and strict hybrid boundaries protect the expensive mainframe from frequent modifications while guaranteeing zero data loss.