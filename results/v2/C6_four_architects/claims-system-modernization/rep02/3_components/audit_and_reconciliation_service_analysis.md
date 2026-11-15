## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-based platform while maintaining uninterrupted business operations. The architecture uses a hybrid cloud approach to ensure zero data loss, strict consistency, and rapid rollback capabilities during the three-year migration window.]

## Key Elements
- **Users**: Customer & Broker, Claims Adjuster, IT Administrator
- **External Systems**: Legacy Mainframe (On-Premises COBOL/DB2), Insurer's Active Directory (Azure AD / Entra ID), Payment Gateway
- **Containers**: Web Portal (React on Azure Static Web Apps), Adjuster Workspace (React on Azure App Service), API Management Proxy (Azure API Management), Claims Processing Service (Java / Spring Boot on Azure Container Apps), Claim Routing Service (Azure Service Bus), Primary Datastore (Azure SQL Database), Claim Read Model Store (Azure Cosmos DB / Redis), Mainframe Integration Adapter (IBM MQ on-premises), Data Sync Worker (Java / Spring Boot on Azure Container Apps), Audit and Reconciliation Service (Azure Functions)
- **Audit and Reconciliation Service Components**: Reconciliation Job Scheduler (Azure Timer Trigger), Reconciliation API (HTTP Trigger), Mainframe Delta Extractor (C# .NET isolated worker), Ledger Comparison Engine (.NET Component), Reconciliation State Repository (Azure Table Storage / Azure SQL), Remediation Dispatcher (C# .NET Component), Discrepancy Notifier

## Relationships
- **Customer & Broker -> Web Portal**: Submits online claims [HTTPS]
- **Claims Adjuster -> Adjuster Workspace**: Handles claims in web application [HTTPS]
- **Web Portal & Adjuster Workspace -> API Management Proxy**: Routes API requests [HTTPS / REST]
- **API Management Proxy -> Claims Processing Service**: Forwards commands [gRPC / HTTPS]
- **Claims Processing Service -> Claim Routing Service**: Publishes claim events [AMQP]
- **Claims Processing Service -> Primary Datastore**: Persists operational state [ADO.NET over TDS / TLS]
- **Data Sync Worker -> Mainframe Integration Adapter**: Synchronizes legacy data [IBM MQ / AMQP]
- **Mainframe Delta Extractor -> Mainframe Integration Adapter**: Pulls daily transaction ledgers [IBM MQ / AMQP]
- **Ledger Comparison Engine -> Primary Datastore**: Queries system of record state [ADO.NET over TDS / TLS]
- **Remediation Dispatcher -> Claim Routing Service**: Publishes correction events [AMQP]
- **IT Administrator -> Reconciliation API**: Initiates manual spot-checks or overrides [HTTPS]
- **Discrepancy Notifier -> IT Administrator**: Escalates unresolved reconciliation failures [HTTPS / Azure Monitor]

## Technology Stack
- **Azure Functions (Serverless)**: Chosen for the Audit and Reconciliation Service to provide an isolated, highly scalable execution environment matching the team's limited cloud experience.
- **C# / .NET Isolated Worker**: Used for reconciliation components to simplify state comparison logic and leverage strong typing.
- **IBM MQ**: Chosen as the on-premises messaging protocol for secure, reliable mainframe integration without exceeding batch constraints.
- **Azure SQL Database & Azure Table Storage**: Utilized for transactional persistence and maintaining immutable reconciliation run metrics.
- **Azure Service Bus**: Implements event-driven messaging and asynchronous correction routing via AMQP.

## Rationale
[This hybrid architecture bridges the on-premises COBOL/DB2 mainframe with Azure cloud services using asynchronous messaging via IBM MQ to strictly respect mainframe constraints. Automated serverless reconciliation and remediation components guarantee zero data loss and rapid one-day claim type switchbacks while accommodating the team's limited cloud expertise.]