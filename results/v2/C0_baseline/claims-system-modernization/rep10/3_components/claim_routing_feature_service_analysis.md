## Overview
The Claim Routing & Feature Service is a .NET Core API running on Azure Container Apps that orchestrates hybrid cloud claim processing. It manages the gradual migration of claim types from a legacy COBOL/DB2 mainframe to modern Azure services using feature flags.

## Key Elements
- Routing Engine Component (.NET Core / MediatR)
- Feature Flag Manager Component (.NET Core / Microsoft Feature Management)
- Context & Auth Validator Component (.NET Core Middleware)
- Telemetry Publisher Component (.NET Core / Azure Monitor & Event Hubs)
- External Systems: Azure App Configuration, Azure Service Bus, Azure Monitor, Legacy Mainframe, Active Directory

## Relationships
- Adjuster Workspace & Customer Portal -> Claim Routing & Feature Service: Routes claims and checks feature flags [gRPC over internal VNet with mTLS]
- Feature Flag Manager -> Azure App Configuration: Fetches feature states [HTTPS via Managed Identity]
- Routing Engine -> Claims Integration Service: Sends asynchronous messages for mainframe synchronization [AMQP via Azure Service Bus]
- Claim Routing & Feature Service -> Azure Monitor: Exports distributed traces, metrics, and security audit logs [OpenTelemetry / OTLP]

## Technology Stack
- .NET Core: High-performance framework matching team capabilities for containerized microservices
- Azure Container Apps: Serverless container platform minimizing infrastructure management for a low-cloud-experience team
- Azure App Configuration: Dynamic management of feature flags enabling 1-day rollbacks (R-06)
- Azure Service Bus: Asynchronous messaging guaranteeing reliable hybrid integration without extending batch windows

## Rationale
This architecture decouples the legacy mainframe from modern frontends using asynchronous messaging and dynamic routing, ensuring zero data loss and sub-2-second response times. It provides strict security controls and business visibility while allowing claim types to be migrated and rolled back independently within one day.