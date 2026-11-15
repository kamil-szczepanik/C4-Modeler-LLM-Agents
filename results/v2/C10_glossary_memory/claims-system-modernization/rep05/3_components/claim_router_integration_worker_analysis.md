## Overview
The Claim Router & Integration Worker is an asynchronous .NET service that routes and integrates claims between the cloud platform and the legacy mainframe. It ensures seamless, secure hybrid operations while claim types are gradually migrated over a three-year period.

## Key Elements
- Claim Router & Integration Worker (.NET Worker Service)
- Routing Engine Component (.NET class library)
- Mainframe Adapter Component (.NET HttpClient/gRPC)
- Outbox Processor Component (.NET Hosted Service)
- Audit & Telemetry Component (Application Insights)
- Azure Service Bus (Azure Messaging Service)
- Legacy Mainframe System (On-premises DB2/COBOL)
- Azure Key Vault (Secret Management)

## Relationships
- Claim Router & Integration Worker -> Azure Service Bus (AMQP)
- Claim Router & Integration Worker -> Legacy Mainframe System (mTLS and signed JWT over hybrid IPsec VPN)
- Claim Router & Integration Worker -> Azure Key Vault (HTTPS/Managed Identity)
- Routing Engine Component -> Claims Core API Service Database (HTTPS/SQL)

## Technology Stack
- .NET Worker Service: Chosen for robust asynchronous processing and native integration with Azure services.
- Azure Container Apps: Provides simple, scalable container hosting suitable for teams with limited cloud experience.
- Azure Service Bus: Manages messaging, backpressure, and reliable queueing to prevent duplicate or lost claims.
- Azure Key Vault: Secures sensitive mTLS certificates and signing keys using managed identities.

## Rationale
This architecture guarantees zero data loss and supports rapid one-day rollbacks through an outbox pattern and dynamic routing rules. It safely bridges the cloud and the legacy mainframe while accommodating the team's limited cloud experience.