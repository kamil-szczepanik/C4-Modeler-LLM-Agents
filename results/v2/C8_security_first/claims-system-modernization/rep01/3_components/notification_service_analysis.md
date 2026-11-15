## Overview
The Notification Service is a secure, asynchronous Azure Container Apps microservice within a hybrid insurance claims modernization platform. Its core purpose is to reliably dispatch multi-channel notifications and maintain audit logs for customers, brokers, and adjusters.

## Key Elements
- Notification API Controller (ASP.NET Core / C#)
- Notification Dispatcher Worker (ASP.NET Core Background Service)
- Template Engine (Fluid / C#)
- Provider Adapter Layer
- Notification Repository (Entity Framework Core)
- Preference Manager Component
- Audit & Telemetry Component
- Azure Service Bus with Dead-Letter Queues (DLQs)
- Azure SQL Database
- Azure Key Vault
- External Gateways (Twilio, SendGrid)

## Relationships
- Claims API Gateway -> Notification API Controller: Routes requests [HTTPS / JSON] using validated JWTs / mTLS
- Notification Dispatcher Worker -> Azure Service Bus: Consumes outbound events [AMQP]
- Notification Dispatcher Worker -> Provider Adapter Layer: Internal invocation [C#]
- Provider Adapter Layer -> External SMS/Email Gateways (Twilio/SendGrid): Outbound API calls [HTTPS / TLS 1.3]
- Notification Repository -> Azure SQL Database: Persists audit logs and states [T-SQL / TDS]

## Technology Stack
- Azure Container Apps: Hosts the microservice with KEDA autoscaling and revision traffic-splitting for cloud simplicity
- ASP.NET Core / C#: Provides a robust, enterprise-standard framework for APIs and background workers
- Azure Service Bus: Ensures asynchronous, reliable message delivery with DLQs to prevent message loss
- Azure SQL Database: Stores structured audit data using in-memory caching to avoid operational overhead
- Azure Key Vault: Manages external provider API secrets securely via managed identities
- OpenTelemetry: Centralizes distributed tracing and structured JSON logging across services

## Rationale
This architecture ensures secure, highly reliable communication without overburdening a team with limited cloud experience by utilizing managed Azure services. Asynchronous messaging via Azure Service Bus guarantees zero message loss and graceful handling of third-party gateway outages.