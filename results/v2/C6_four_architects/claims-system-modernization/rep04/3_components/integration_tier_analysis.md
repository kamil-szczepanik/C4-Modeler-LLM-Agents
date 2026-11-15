## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims platform with a modern hybrid cloud solution in Azure. The Integration Tier ensures seamless, consistent hybrid communication between modern microservices and legacy infrastructure without extending nightly batch windows.

## Key Elements
- Event Bus Router (Azure Service Bus)
- Hybrid Tunnel Gateway (Azure Relay)
- Dead Letter & Reconciliation Manager (Azure Service Bus DLQ and Azure Functions)
- Schema Transformation Router (Azure Functions and API Management)
- Application Tier (Java/Spring Boot microservices)
- Hybrid Bridge (Spring Boot Mainframe Adapter on-premise)

## Relationships
- Application Tier -> Event Bus Router: Publishes domain events [AMQP]
- Event Bus Router -> Schema Transformation Router: Queues messages requiring legacy translation [AMQP]
- Schema Transformation Router -> Hybrid Tunnel Gateway: Forwards transformed payloads [HTTPS/AMQP]
- Hybrid Tunnel Gateway -> Hybrid Bridge: Connects securely to on-premise mainframe [Azure Relay]
- Event Bus Router -> Dead Letter & Reconciliation Manager: Captures poisoned messages [Internal Service Bus API]
- Dead Letter & Reconciliation Manager -> Application Tier: Triggers reconciliation alerts [Webhooks/HTTPS]

## Technology Stack
- Azure Service Bus: Asynchronous pub/sub messaging ensuring guaranteed message delivery and zero data loss.
- Azure Relay: Establishes secure, outbound-only hybrid connectivity respecting corporate firewall constraints.
- Azure Functions: Serverless execution for automated error reconciliation and schema mapping, reducing operational overhead for teams with low cloud experience.
- Azure API Management: Centralized API routing and legacy data formatting to avoid costly mainframe modifications.

## Rationale
This hybrid architecture isolates legacy complexity within the Integration Tier while ensuring strict transactional consistency (R-04) during the 3-year migration. Managed Azure services reduce operational risk for a team with limited cloud experience.