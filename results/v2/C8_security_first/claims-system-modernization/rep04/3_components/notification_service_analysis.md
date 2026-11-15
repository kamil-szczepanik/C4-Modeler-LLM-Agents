## Overview
[The Notification Service is a microservice built on Azure Container Apps that delivers multi-channel communications (Email, SMS, Push) to customers, brokers, and adjusters.]
[It ensures reliable, secure, and auditable status updates during the hybrid insurance claims modernization process.]

## Key Elements
* Node.js/TypeScript Runtime (Azure Container Apps)
* API Controller / Event Consumer Component
* Preference Manager Component
* Template Engine Component
* Dispatch Adapter Component with Opossum Circuit Breaker
* Notification State Repository (Azure Cosmos DB NoSQL)
* Azure Service Bus (AMQP with DLQ)
* External Gateways (SendGrid, Twilio via HTTPS)
* Azure Key Vault & Managed Identities
* Azure Monitor / OpenTelemetry

## Relationships
* Claim Processing Core interacts with Notification Service via Azure Service Bus (AMQP)
* Backend-for-Frontend (BFF) interacts with Notification Service via Internal HTTPS REST
* Dispatch Adapter connects to SendGrid and Twilio via HTTPS (TLS 1.3)
* Notification Service reads and writes to Azure Cosmos DB via HTTPS SDK
* Service pulls secrets from Azure Key Vault using Managed Identities

## Technology Stack
* Azure Container Apps: Chosen for serverless container hosting, aligning with the team's cloud experience level.
* Node.js / TypeScript: Selected for lightweight asynchronous I/O performance in event-driven messaging.
* Azure Service Bus: Provides reliable asynchronous queuing, dead-letter routing, and decoupled processing.
* Azure Cosmos DB (NoSQL): Stores notification metadata and delivery status for auditability without heavy relational overhead.
* SendGrid & Twilio: Industry-standard external APIs for reliable email and SMS delivery.
* Azure Key Vault & Managed Identities: Ensures secure, credential-free secret management for third-party integrations.

## Rationale
[This architecture guarantees high delivery reliability (99.9%) and strict PII data protection while accommodating the team's limited cloud experience through managed Azure services.]
[It decouples external communication failures from core claim processing using resilient circuit breakers and asynchronous messaging patterns.]