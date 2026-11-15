## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a legacy mainframe with a cloud-native architecture. Its core purpose is to enable uninterrupted, modern claim processing while ensuring strict consistency and zero data loss during the 3-year migration.

## Key Elements
- **Users**: Customers, Brokers, Claims Adjusters, Business Operations Managers, System Administrators
- **Systems**: Modern Azure-Hosted Claims Platform, On-Premises COBOL/DB2 Mainframe System of Record, Azure AD (Entra ID)
- **Containers**: Customer/Broker Web App (Azure Container Apps), Claims Adjuster Web App (Azure Container Apps), API Gateway (Azure Container Apps), Integration/Messaging Container (Azure Service Bus), Operations Portal Container (Azure Container Apps), Audit & Reconciliation Container (Azure Container Apps), Azure SQL Database

## Relationships
- Customer/Broker Web App -> API Gateway: Submits claims [HTTPS/TLS 1.3]
- Claims Adjuster Web App -> API Gateway: Manages claims [HTTPS/TLS 1.3]
- API Gateway -> Integration/Messaging Container: Publishes asynchronous messages [Azure Service Bus Protocol]
- Integration/Messaging Container -> On-Premises COBOL/DB2 Mainframe System of Record: Synchronizes data [Azure ExpressRoute with IPSec]
- Operations Portal Container -> Azure Monitor: Reads telemetry and metrics [HTTPS]

## Technology Stack
- **Compute**: Azure Container Apps for microservices and web applications due to simplified container management.
- **Messaging**: Azure Service Bus with built-in dead-letter queues (DLQ) and exponential backoff for resilient asynchronous processing.
- **Database**: Azure SQL Database with Transparent Data Encryption (TDE) and column-level PII encryption for secure storage.
- **Security**: Azure Active Directory (Entra ID) for single sign-on and Managed Identities with Azure RBAC for least-privilege access.
- **Infrastructure & Monitoring**: Terraform/Bicep via GitHub Actions for Infrastructure-as-Code, and Azure Monitor/Application Insights for telemetry.

## Rationale
This hybrid architecture minimizes expensive mainframe modifications by decoupling modern cloud frontends through asynchronous messaging. It specifically addresses team skill constraints while meeting stringent security, compliance, and zero-data-loss requirements.