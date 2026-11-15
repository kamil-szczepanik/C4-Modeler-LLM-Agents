## Overview
The Insurance Claims Modernization platform gradually replaces an on-premises COBOL/DB2 mainframe with a cloud-native Azure architecture while maintaining legacy processing. The Claim Ingestion & Validation Module acts as the entry point, ensuring secure, idempotent, and validated processing of online claims.

## Key Elements
* API Gateway (Azure Hosted API Gateway)
* Claim Ingestion & Validation Module (.NET Core / Modular Monolith)
* Anti-Corruption Layer (ACL) (.NET Core / Modular Monolith)
* Azure Blob Storage
* Azure App Configuration
* Azure Monitor / Application Insights
* Azure Dead Letter Queue (DLQ)

## Relationships
* API Gateway -> Claim Ingestion & Validation Module: Route ingress traffic internally [HTTPS / Internal API]
* Claim Ingestion & Validation Module -> Azure Blob Storage: Store large claim attachments via Claim Check Pattern [HTTPS]
* Claim Ingestion & Validation Module -> Anti-Corruption Layer (ACL): Forward validated claim payloads [Azure Service Bus]
* Claim Ingestion & Validation Module -> Azure Monitor / Application Insights: Emit structured telemetry [HTTPS]

## Technology Stack
* .NET Core: Selected for the modular monolith implementation, balancing rapid development with the team's limited cloud experience.
* Azure Blob Storage: Used for payload offloading of large attachments via the Claim Check Pattern to prevent resource exhaustion.
* Azure App Configuration: Manages feature flags for dynamic claim type toggles and rapid rollbacks.
* Azure Service Bus: Provides asynchronous message transport to the Anti-Corruption Layer (ACL).

## Rationale
This architecture uses proven modular patterns and robust fallback mechanisms to guarantee data consistency and system reliability during incremental mainframe migration. It isolates cloud complexity, protecting downstream systems while ensuring high maintainability and performance.