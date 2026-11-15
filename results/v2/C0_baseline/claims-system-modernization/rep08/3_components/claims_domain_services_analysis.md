## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-based cloud architecture. It ensures seamless claim processing, zero data loss, and rapid rollbacks during the multi-year migration.

## Key Elements
*   Claim Processing Controller (.NET 8 Web API)
*   Idempotency Filter & Middleware (Azure Cache for Redis)
*   Feature Flag Evaluator (Azure App Configuration)
*   Claim Domain Model & Handlers (.NET 8)
*   Data Access Repository (Azure SQL Database, Entity Framework Core)
*   Audit & Telemetry Interceptor (Azure Application Insights)
*   Integration Publisher (Azure Service Bus)

## Relationships
*   API Gateway -> Claim Processing Controller: Invokes domain logic via gRPC over mTLS in Azure VNet
*   Idempotency Filter -> Azure Cache for Redis: Validates idempotency keys [TCP/TLS]
*   Feature Flag Evaluator -> Azure App Configuration: Reads feature flags and routing rules [HTTPS / Managed Identities]
*   Data Access Repository -> Azure SQL Database: Persists claim data securely [TLS 1.3 / Entra ID Authentication]
*   Integration Publisher -> Azure Service Bus: Publishes encrypted claim events [AMQP / Managed Identities]
*   Audit Interceptor -> Azure Monitor: Writes tamper-evident audit logs [HTTPS]

## Technology Stack
*   **C# / .NET 8:** Core runtime for high-performance microservices and domain logic.
*   **gRPC:** High-performance RPC protocol for secure inter-container communication.
*   **Azure Container Apps:** Serverless container hosting supporting progressive delivery and VNet isolation.
*   **Azure SQL Database:** Relational data store with Always Encrypted for PII protection.
*   **Azure Service Bus:** Reliable message broker for asynchronous hybrid synchronization.
*   **Azure App Configuration:** Dynamic configuration store enabling one-day claim-type rollbacks.

## Rationale
This architecture balances the strict constraints of a legacy hybrid environment with cloud-native resilience through isolated microservices and strict idempotency. It guarantees zero data loss, rapid rollback capabilities, and secure integration with corporate Active Directory while accommodating the team's limited cloud experience.