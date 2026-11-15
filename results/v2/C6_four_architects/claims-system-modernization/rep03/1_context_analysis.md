## Overview
[The system is a hybrid cloud Insurance Claims Modernization Platform that gradually replaces a legacy COBOL/DB2 mainframe while maintaining continuous claim processing. It delivers modern web interfaces for customers, brokers, and adjusters while decoupling legacy dependencies.]

## Key Elements
* **External Users**: Customers, Brokers, and Claims Adjusters
* **Modernization Platform (Azure)**: Cloud-hosted platform containing the Customer Portal, Adjuster Web App, Claim Processing Engine, and Integration/BFF service
* **Data Storage**: Azure SQL Database / Azure Cosmos DB for operational data and CQRS read-models
* **Integration Layer**: Enterprise Integration Bus (EIB) / API Management with Azure Service Bus
* **Legacy Mainframe**: On-premises COBOL/DB2 system of record
* **External Services**: Active Directory (Identity Provider), Core Rating & Underwriting Engine, Payment Gateway, and Notification Service (SendGrid/Azure Communication Services)

## Relationships
* **Users** interact with the **Modernization Platform** via HTTPS
* **Modernization Platform** authenticates against **Active Directory** via SAML/OIDC over HTTPS
* **Modernization Platform** calls the **Rating & Underwriting Engine**, **Payment Gateway**, and **Notification Service** via HTTPS/REST
* **Modernization Platform** communicates with the **EIB / API Gateway** via asynchronous messaging using Azure Service Bus
* **EIB / API Gateway** connects to the **Legacy Mainframe** via ExpressRoute and legacy protocols

## Technology Stack
* **Cloud Provider**: Microsoft Azure (West Europe region) with Azure Container Apps and Static Web Apps for simplified management given low cloud experience
* **Integration**: Azure Service Bus and Azure API Management to decouple services and protect the mainframe
* **Database**: Azure SQL Database / Azure Cosmos DB implementing CQRS to meet performance requirements
* **Security**: Active Directory integration using SAML/OIDC protocols over HTTPS

## Rationale
[This hybrid architecture isolates the expensive-to-change, slow legacy mainframe using an asynchronous Azure Service Bus and API Gateway, ensuring adjuster screens load under 2 seconds. Furthermore, CQRS and incremental claim-type routing guarantee transactional consistency without violating the strict nightly batch window.]