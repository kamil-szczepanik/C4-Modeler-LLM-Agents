## Overview
[The Claim Processing Core modernizes a regional insurer's legacy claims platform using a hybrid cloud architecture. It gradually migrates claim types from a COBOL/DB2 mainframe to a scalable Azure-based microservices platform.]

## Key Elements
- Claim Intake Router (Azure Functions)
- Workflow Orchestrator (Azure Durable Functions)
- Integration Adapter (C# Class Library with Polly)
- Domain Model Engine (DDD Class Library)
- Azure Service Bus
- Azure Cosmos DB
- Azure Key Vault
- Azure Container Apps

## Relationships
- Azure API Management -> Claim Intake Router [mTLS / HTTPS]
- Claim Intake Router -> Azure Service Bus [AMQP]
- Workflow Orchestrator -> Azure Cosmos DB [HTTPS / TLS 1.3]
- Integration Adapter -> Legacy Mainframe [mTLS via VPN/ExpressRoute]
- Claim Processing Core -> Azure Key Vault [Managed Identities / HTTPS]

## Technology Stack
- Azure Container Apps: Container hosting platform reducing day-2 operational overhead for cloud-inexperienced teams
- Azure Durable Functions: Serverless state orchestration ensuring idempotent claim processing and preventing duplicate payouts
- Azure Service Bus: Asynchronous message broker handling ingestion spikes without impacting the 23:00-05:00 batch window
- Azure Cosmos DB: Multi-model database providing state storage and WORM ledger mode for immutable audit events
- Polly: Resilience library implementing circuit breakers and retries to handle mainframe latency

## Rationale
[This architecture balances strict consistency and security requirements by utilizing managed Azure PaaS services to mitigate the team's limited cloud experience. It decouples the modernization effort from the legacy mainframe while guaranteeing a one-day rollback capability and zero data loss.]