## Overview
- Hybrid insurance claims platform modernizing a 30-year-old COBOL/DB2 mainframe system.
- Gradually migrates claim types over 3 years while maintaining zero loss and zero duplicate processing.

## Key Elements
- **Users**: Customers, Brokers, Claims Adjusters
- **External Systems**: Legacy Mainframe System, Corporate Active Directory
- **Containers**: Customer Portal (Azure App Service, React), Adjuster Workspace (Azure App Service, React, Node.js BFF), API Gateway (Azure API Management), Integration / ACL Service (Azure Container Apps, .NET), Claims Read/Write Database (Azure Database for PostgreSQL)
- **Azure Service Bus Components**: Claim Submission Topic & Subscriptions, Dead-Letter Queue (DLQ) Handler, Session State Manager, Partitioned Topic Engine, Duplicate Detection Filter

## Relationships
- Customer Portal / Adjuster Workspace -> API Gateway: Routes HTTP/REST traffic [HTTPS over TLS 1.3]
- API Gateway -> Integration / ACL Service: Forwards validated requests [gRPC / HTTPS]
- Integration / ACL Service -> Azure Service Bus: Publishes and consumes messages [AMQP 1.0 over TLS 1.3, Azure Managed Identities]
- Integration / ACL Service -> Claims Read/Write Database: Persists modern claims [ADO.NET / TLS]

## Technology Stack
- **Compute**: Azure App Service, Azure Container Apps for scalable containerized workloads.
- **Messaging**: Azure Service Bus (Premium Tier) with Managed Identities for secure, reliable, partitioned asynchronous messaging.
- **Database**: Azure Database for PostgreSQL for modern transactional storage.
- **Frontend**: React with Node.js BFF for responsive adjuster and customer UI.
- **Infrastructure & Security**: Bicep/Terraform for declarative deployment; Azure Active Directory (Entra ID) for SSO.

## Rationale
- The hybrid cloud architecture isolates expensive mainframe changes while allowing iterative claim type migration within 3 years.
- Azure Service Bus Premium with session management and duplicate detection guarantees strict consistency and zero data loss without extending batch windows.