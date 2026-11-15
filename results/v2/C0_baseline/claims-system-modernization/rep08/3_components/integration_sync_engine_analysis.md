## Overview
This architecture establishes a hybrid integration engine to bridge a 30-year-old COBOL/DB2 mainframe with a modern Azure cloud platform. It enables gradual, risk-free migration of insurance claim types over a three-year period while maintaining strict data consistency.

## Key Elements
- Sync Orchestrator Function (Azure Functions - Durable Functions)
- Mainframe Adapter Component (C# class library with Polly circuit breaker)
- Reconciliation Worker (Azure Functions - Timer Trigger)
- Change Data Capture (CDC) Consumer (Azure Functions)
- Feature Flag Router Component (C# middleware)
- Enterprise Integration Bus (EIB)
- Azure Service Bus & Azure App Configuration

## Relationships
- Integration & Sync Engine -> Enterprise Integration Bus: Replicates hybrid data via AMQP and HTTPS/mTLS
- Sync Orchestrator -> Azure Key Vault: Retrieves secrets using Azure Managed Identities
- Feature Flag Router -> Azure App Configuration: Evaluates migration streams via in-memory caching and managed identities
- Mainframe Adapter -> Enterprise Integration Bus: Transmits cryptographically signed payloads using TLS 1.3

## Technology Stack
- Azure Functions & Durable Functions: Serverless event orchestration and stateful saga management
- Azure Service Bus: Asynchronous message brokering with dead-letter queuing for zero data loss
- Polly Library: Resilience and circuit-breaking for legacy mainframe timeouts
- Azure App Configuration & Managed Identities: Dynamic feature flag routing and credential-less authentication

## Rationale
This architecture isolates expensive mainframe dependencies while empowering incremental, low-risk claim migrations (R-03) through dynamic feature flags and robust circuit breaking. It accommodates the team's cloud inexperience via managed serverless services and GitOps configuration while guaranteeing rapid fallback capabilities within one business day (R-06).