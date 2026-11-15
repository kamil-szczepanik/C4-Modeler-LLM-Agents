## Overview
[The system is a hybrid cloud-on-premise Insurance Claims Modernization platform that gradually replaces a 30-year-old mainframe while ensuring zero data loss and uninterrupted business operations.]

## Key Elements
- Business Operations Owner
- Integration Mediator Container
- Routing Router Component (Azure Logic Apps)
- Circuit Breaker & Retry Policy Component (Azure Function middleware)
- Copybook Mapper Component (Azure Functions, Node.js/TypeScript)
- Dead-Letter Handler Component (Azure Functions & Azure Storage Queue)
- Migration Operations Dashboard

## Relationships
- Claims Core Engine -> Routing Router: Domain Events [HTTP/REST or AMQP]
- Routing Router -> Circuit Breaker: Validated Payload [HTTP]
- Circuit Breaker -> Copybook Mapper: Throttled Transformation [Internal Function Call]
- Copybook Mapper -> Legacy Mainframe: COBOL Transaction [TCP/MQ via JSON-to-COBOL copybook mapping]
- Dead-Letter Handler -> Migration Operations Dashboard: Enriched Business Exception [REST/WebSockets with OpenTelemetry correlation ID]

## Technology Stack
- Azure Logic Apps & Azure Functions: Chosen for serverless event routing and lightweight payload transformation given the team's cloud experience level.
- Node.js/TypeScript: Used within Azure Functions for JSON-to-COBOL copybook mapping.
- Azure Service Bus: Provides persistent exponential backpressure and dead-lettering for hybrid queue sinking.
- OpenTelemetry & Azure Monitor Application Insights: Establishes unified distributed tracing across cloud and on-premise components.
- Terraform: Implements Infrastructure-as-Code and GitOps pipeline templates to reduce operational complexity.

## Rationale
[This architecture successfully isolates the fragile, expensive-to-change COBOL/DB2 mainframe behind resilient integration middleware while enabling incremental, low-risk claim type migrations. It strictly satisfies consistency, maintainability, and observability constraints within a hybrid cloud environment.]