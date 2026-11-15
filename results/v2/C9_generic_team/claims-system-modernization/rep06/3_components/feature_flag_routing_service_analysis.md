## Overview
[The system is a Feature Flag and Routing Service that manages incremental claim type migration from a legacy COBOL/DB2 mainframe to a modern Azure platform. It ensures reliable hybrid routing, rapid rollbacks, and strict consistency without risking data loss.]

## Key Elements
- Feature Flag / Routing Service (Azure App Configuration)
- BFF (Backend-for-Frontend) and Claim Management Core (Azure App Service)
- Routing Client SDK
- Azure Service Bus
- Azure Application Insights

## Relationships
- BFF and Claim Management Core query the Feature Flag / Routing Service using HTTP/REST via the Routing SDK.
- Azure App Configuration publishes cache invalidation events to the BFF via Azure Service Bus.
- BFF and Claim Management Core emit metrics, audit logs, and distributed traces to Azure Application Insights.

## Technology Stack
- Azure App Configuration: Declarative configuration provider for managing routing states with built-in revision history.
- Consistent Hashing: Deterministic algorithm based on claim IDs to guarantee repeatable routing decisions.
- Circuit Breaker Pattern: Implemented in the SDK to enforce fallback-to-safe-default behavior targeting the mainframe during outages.
- Azure Service Bus: Event broker enabling near-instantaneous cache invalidation for emergency rollbacks.
- Azure Application Insights: Observability platform for telemetry, canary evaluation metrics, and distributed tracing.

## Rationale
[Deterministic consistent hashing and explicit overrides ensure compliance with consistency and one-day rollback requirements. Furthermore, using managed cloud configurations and built-in SDK resilience patterns minimizes operational overhead for a team with limited cloud experience.]