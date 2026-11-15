## Overview
[The system is a hybrid cloud insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe while maintaining continuous operations. Its core purpose is to migrate claim types incrementally via an Anti-Corruption Layer while ensuring zero data loss and unified user experiences.]

## Key Elements
- End Customers, Brokers, Claims Adjusters, Business Operations Managers, and Migration Admins
- Single Sign-On / Identity Provider: Azure Entra ID (Active Directory)
- Frontend: Angular/React Single Page Application hosted in Azure Static Web Apps
- API Gateway / Router: Azure API Management (APIM)
- Core Platform: Node.js/Java microservices on Azure Kubernetes Service (AKS)
- Integration & ACL: Azure Service Bus
- Storage: Azure SQL Database
- Analytics: Azure Event Hubs, Stream Analytics, Azure Synapse Analytics, and Power BI Embedded
- Legacy System: On-Premises COBOL/DB2 Mainframe

## Relationships
- End Users to Azure Static Web Apps via HTTPS for UI access
- APIM to Azure Static Web Apps and AKS via HTTPS / REST APIs
- AKS to Azure SQL Database via TDS / SQL protocols
- AKS / APIM to Azure Service Bus via AMQP for asynchronous messaging
- Azure Service Bus / APIM to On-Premises Mainframe via mTLS over IPsec VPN / ExpressRoute
- AKS / Azure SQL to Azure Event Hubs via internal event streaming
- Business Operations Managers to Dashboard Container via HTTPS

## Technology Stack
- Azure Static Web Apps: Hosts the SPA frontend for fast global delivery
- Azure API Management (APIM): Enforces OIDC/OAuth2 authentication and dynamic routing for claim-type migration
- Azure Kubernetes Service (AKS): Runs containerized microservices and backend-for-frontend (BFF) components
- Azure Service Bus: Provides reliable asynchronous messaging for the Anti-Corruption Layer (ACL)
- Azure SQL Database: Stores modern claim types with encryption at rest (Customer-Managed Keys)
- Azure Event Hubs & Synapse Analytics: Ingests CDC streams and operational metrics for auditing and reporting
- Azure Entra ID: Handles Single Sign-On and Role-Based Access Control (RBAC)

## Rationale
[This hybrid architecture uses an Anti-Corruption Layer and API Gateway to decouple modern cloud services from the legacy mainframe, satisfying the strict 3-year migration constraint and max one-per-quarter interface limit. It leverages Azure managed services to provide high availability, robust security via mTLS and zero-trust principles, and a one-day rollback capability without extending the rigid nightly batch window.]