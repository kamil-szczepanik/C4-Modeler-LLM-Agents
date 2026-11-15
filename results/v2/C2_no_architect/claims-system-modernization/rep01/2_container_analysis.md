## Overview
[The system is a hybrid cloud insurance claims modernization platform that gradually replaces a legacy on-premises mainframe while maintaining core operations. Its primary purpose is to enable online claim submission and adjuster workflows in Azure while ensuring seamless synchronization with the legacy system.]

## Key Elements
- **Users:** Customers, Brokers, Claims Adjusters, Business Operations Managers, System Administrators
- **Azure Containers:** Customer/Broker Web App, Claims Adjuster Web App, API Gateway, Integration/Messaging Container, Operations Portal Container, Audit & Reconciliation Container
- **External Systems:** On-Premises COBOL/DB2 Mainframe System of Record, Azure Active Directory (Entra ID)
- **Azure Data Stores:** Azure SQL (with Transparent Data Encryption and column-level PII encryption)

## Relationships
- Customers and Brokers access the Customer/Broker Web App and API Gateway via HTTPS using OpenID Connect/OAuth2.
- Claims Adjusters interact with the Claims Adjuster Web App via HTTPS with identity delegated to Azure AD.
- Azure Containers communicate internally via mTLS and authenticate using Azure Entra Managed Identities.
- The Integration/Messaging Container (Azure Service Bus) synchronizes data asynchronously with the On-Premises COBOL/DB2 Mainframe via Azure ExpressRoute with IPSec encryption.
- The Audit & Reconciliation Container continuously verifies state consistency against the DB2 mainframe.

## Technology Stack
- **Cloud Provider:** Hybrid deployment utilizing Azure West Europe and on-prem-mainframe
- **Compute:** Azure Container Apps (managed PaaS to offset low cloud team experience)
- **Messaging:** Azure Service Bus (asynchronous integration to decouple UI from mainframe latency)
- **Database:** Azure SQL (managed relational storage with TDE and column-level encryption)
- **Security & Identity:** Azure Active Directory / Entra ID with Managed Identities and Azure Policy (Policy-as-Code)
- **Infrastructure & Observability:** Terraform/Bicep for Infrastructure-as-Code, OpenTelemetry for distributed tracing

## Rationale
- [Decoupling the Azure UI via an asynchronous messaging container and read model ensures sub-2-second adjuster screen loads despite sluggish 5-second mainframe responses.]
- [Employing fully managed Azure PaaS services, automated compliance guardrails, and a dedicated audit container mitigates risks from low cloud experience while guaranteeing data consistency and rapid mainframe rollback capabilities.]