## Overview
[The system modernizes a 30-year-old regional insurance mainframe by gradually migrating claim types to a hybrid cloud platform while ensuring zero data loss. The Operational Observability & Dead-Letter Container monitors system health and manages failed message delivery.]

## Key Elements
- Dead-Letter Consumer Component (.NET 8 Worker)
- Re-drive Engine Component (.NET 8 Minimal API)
- Metrics & Tracing Collector (OpenTelemetry / Azure Monitor exporter)
- Operations API Component (.NET 8 Minimal API)
- Payload Normalization & Enrichment Component (.NET 8)

## Relationships
- Dead-Letter Consumer Component consumes failed messages from Azure Service Bus / Event Hubs DLQs via AMQP.
- Operations API Component exposes secure HTTPS endpoints for the Claims API Gateway and Operations Managers.
- Payload Normalization & Enrichment Component stores enriched payloads in Azure Blob Storage with HTTPS.
- Metrics & Tracing Collector exports telemetry to Azure Monitor over HTTPS.

## Technology Stack
- .NET 8 on Azure Container Apps for lightweight, fast component isolation.
- Azure Blob Storage with structured JSON indexing for searchable dead-letter payloads.
- OpenTelemetry and Azure Monitor for centralized system health and distributed tracing.
- Azure Active Directory and TLS 1.3 for secure authentication and transport encryption.

## Rationale
[This architecture provides strict resilience and idempotency controls to satisfy zero-loss migration mandates (R-04) despite limited cloud team experience. It bridges deep technical errors with business-context triage to ensure operational continuity.]