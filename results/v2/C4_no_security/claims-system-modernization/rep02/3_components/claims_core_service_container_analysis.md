## Overview
[The hybrid Azure and on-premises Claims Core Service incrementally replaces a 30-year-old mainframe by migrating claim types one by one while ensuring zero claim loss. It delivers sub-2-second adjuster response times through asynchronous orchestration and caching despite slow legacy dependencies.]

## Key Elements
• Claims Core Service Container (Java / Spring Boot on Azure Container Apps)
• Claim Orchestration Component (Spring State Machine)
• Migration Router Component (with Resilience4j Circuit Breaker)
• Domain Service Components (Spring Data JPA)
• Audit & Reconciliation Component (Spring Batch / Spring Integration)
• Mainframe Adapter Container (Azure Service Bus)
• Data & Caching Container (Azure Cosmos DB + Redis)
• Configuration (Azure App Configuration)

## Relationships
• Migration Router Component -> Mainframe Adapter Container: Forwards unmigrated claim traffic [AMQP / Azure Service Bus]
• Claim Orchestration Component -> Data & Caching Container: Reads/writes transactional data and read models [TCP/TLS]
• Audit & Reconciliation Component -> Data & Caching Container: Persists audit logs and reconciliation state [TCP/TLS]
• Audit & Reconciliation Component -> Mainframe Adapter Container: Reconciles modern records against legacy batch exports [AMQP / REST]

## Technology Stack
• Java 17 / Spring Boot: Robust enterprise foundation for domain logic and integration
• Azure Container Apps & KEDA: Simplifies cloud deployment and autoscaling for a team with low cloud experience
• Spring State Machine: Manages complex claim lifecycles asynchronously
• Resilience4j: Protects against legacy mainframe outages during batch windows
• Spring Integration / Batch: Handles reliable asynchronous ledger checks and reconciliation
• Azure Managed Grafana & Application Insights: Provides distributed tracing and operational dashboards via OpenTelemetry

## Rationale
[This architecture uses containerized microservices and asynchronous patterns to decouple modern web UI performance from slow mainframe responses, meeting strict 2-second UI SLAs. Feature flagging and reconciliation components enable risk-free, incremental claim-type migration with a one-day rollback capability.]