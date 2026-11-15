## Overview
The system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern Azure-hosted platform while maintaining dual-system processing. It provides online claim submission, adjuster management, and incremental claim-type migration with rapid rollback capabilities.

## Key Elements
- End Customers & Brokers
- Claims Adjusters & Migration Product Owners
- Web Frontend (SPA)
- Claims API Gateway
- Core Claims Service
- Mainframe Anti-Corruption Layer (ACL)
- Integration & Transformation Worker
- Operational Observability & Dead-Letter Container
- Legacy COBOL/DB2 Mainframe
- Azure Key Vault & Active Directory (Entra ID)

## Relationships
- End Users to Web Frontend: HTTPS / REST / WebSockets
- Web Frontend to Claims API Gateway: HTTPS / REST
- Claims API Gateway to Core Claims Service: gRPC / internal HTTPS
- Core Claims Service to Mainframe ACL: Azure Event Hubs (Kafka)
- Mainframe ACL to Legacy Mainframe: IPsec VPN / Azure ExpressRoute (SFTP, MQ, Batch)
- Services to Azure Key Vault: Managed Identities (HTTPS)

## Technology Stack
- Azure Static Web Apps: Hosts the Web Frontend SPA for low operational overhead
- Azure API Management: Acts as the Claims API Gateway enforcing AD authentication
- Azure Container Apps: Runs containerized microservices due to team's cloud experience
- Azure Event Hubs (Kafka): Powers the Mainframe ACL for asynchronous decoupling
- Azure Key Vault: Secures Customer-Managed Keys and service credentials

## Rationale
This hybrid architecture isolates expensive mainframe changes using an asynchronous event-driven anti-corruption layer, protecting business continuity. Utilizing managed serverless Azure services minimizes complexity for a team with limited cloud experience while guaranteeing strict consistency, performance, and rollback requirements.