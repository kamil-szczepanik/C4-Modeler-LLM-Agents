## Overview
The Core Claims Service gradually modernizes a legacy insurance platform using a hybrid cloud architecture. It handles online submissions, adjuster workflows, and incremental claim type migrations while maintaining zero data loss.

## Key Elements
- Claim Orchestrator Component (Java / Spring Boot)
- Claim Domain Model Component (Java / DDD)
- ACL Publisher Component (Apache Kafka Client)
- Validation & Policy Engine Component (Spring Validation / Drools)
- SLA & Metrics Telemetry Component (Micrometer / OpenTelemetry)

## Relationships
- Core Claims Service -> Mainframe Anti-Corruption Layer: Publishes asynchronous events [Apache Kafka / Azure Event Hubs]
- Core Claims Service -> Azure Key Vault & Active Directory: Retrieves secrets and validates tokens [Managed Identities / OAuth2 / HTTPS]
- Internal Components -> Internal Components: Executes direct in-process method calls [In-Memory]

## Technology Stack
- Java / Spring Boot: Chosen for robust enterprise ecosystem and team familiarity
- Azure Container Apps: Provides managed container orchestration with low operational overhead
- Spring Security & OAuth2: Enforces zero-trust token validation and RBAC/ABAC
- Micrometer & OpenTelemetry: Captures distributed traces and business metrics without leaking PII

## Rationale
This component-based architecture isolates modern business logic from rigid legacy constraints, enabling a one-day rollback per claim type. It mitigates the team's low cloud experience through managed Azure services and automated scaling.