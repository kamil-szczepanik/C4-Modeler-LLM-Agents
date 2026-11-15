## Overview
- Hybrid modernization architecture replacing a 30-year-old COBOL/DB2 mainframe claims system.
- Gradually migrates claim types over 3 years while maintaining zero data loss and strict performance SLAs.

## Key Elements
- Azure API Management / Migration Router
- Azure Static Web Apps / React Claims Web App
- Azure Container Apps (Adjuster Backend & Mainframe Integration Adapter)
- Azure App Service & Azure Cosmos DB (Migration Control Service)
- Azure Service Bus & Azure Functions (Integration & Sync Service)
- Azure Key Vault & Legacy Mainframe (COBOL/DB2)

## Relationships
- Azure API Management -> Azure Container Apps (Mainframe Integration Adapter): Dynamically routes traffic [HTTPS]
- Azure Container Apps (Mainframe Integration Adapter) -> Legacy Mainframe (COBOL/DB2): Connects securely [TLS 1.3 with mTLS]
- Transformation & Mapping Engine -> Mapping Audit Publisher: Forwards validation errors [In-memory / Async]
- Mapping Audit Publisher -> Azure Service Bus: Publishes audit events [AMQP]

## Technology Stack
- Azure Container Apps: Chosen for scalable microservices execution with low operational complexity.
- Azure Service Bus: Enables asynchronous, reliable event messaging for auditing and sync.
- Azure Key Vault: Centralized secret management and automated certificate rotation.
- TLS 1.3 and mTLS: Secures hybrid transport between Azure and on-premises mainframe.

## Rationale
- Decouples modern web applications from legacy mainframe constraints using an adapter and message bus.
- Enforces strict security, auditability, and rollback capabilities to meet stringent migration constraints.