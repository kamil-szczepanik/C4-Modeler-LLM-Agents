## Overview
The modern platform incrementally replaces a 30-year-old COBOL/DB2 mainframe claims system using a hybrid architecture in Azure West Europe. It ensures seamless online claim submission, real-time adjuster processing, and gradual claim-type migration with zero data loss.

## Key Elements
- **Users**: Customers, Brokers, and Claims Adjusters
- **Gateways & Routing**: Azure API Management (Strangler Fig Router), React SPA Frontend, ASP.NET Core BFF
- **Backend Services**: Claims Processing Engine on Azure Kubernetes Service (AKS) containing Claim State Orchestrator, Migration Routing Component, and Reconciliation Worker
- **Integration & Messaging**: Anti-Corruption Layer (Azure Functions & Azure Service Bus)
- **Data & Security**: Azure SQL Database, Azure Cache for Redis, Azure Active Directory, Azure Key Vault, Azure Monitor & Managed Grafana

## Relationships
- Customers/Brokers & Adjusters -> Azure API Management: HTTPS/TLS 1.3
- Adjuster Web App -> ASP.NET Core BFF -> Claim State Orchestrator: HTTPS / REST / OAuth2/OIDC
- Claim State Orchestrator & Reconciliation Worker -> Azure SQL Database: TDS / EF Core
- Claims Processing Engine -> Anti-Corruption Layer: Azure Service Bus Topics (AMQP)
- Anti-Corruption Layer -> Legacy Mainframe: Legacy batch/sync protocols
- Reconciliation Worker -> Azure Monitor / Managed Grafana: OpenTelemetry / Prometheus metrics

## Technology Stack
- **Compute**: Azure Kubernetes Service (AKS) for scalable microservices hosting
- **Backend Framework**: ASP.NET Core with MediatR for in-memory dispatching and Entity Framework Core
- **Database**: Azure SQL Database for ACID transactional persistence
- **Caching**: Azure Cache for Redis for performance optimization
- **Messaging**: Azure Service Bus for asynchronous event streaming
- **Observability**: OpenTelemetry, Azure Monitor, and Azure Managed Grafana for metrics
- **Security**: Azure Active Directory, Azure Key Vault CSI Driver, and Istio/Linkerd mTLS

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while delivering sub-2-second adjuster response times via modern cloud services. It guarantees zero claim loss and rapid one-day rollback capabilities through dedicated reconciliation and routing components.