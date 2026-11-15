## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe while maintaining continuous claim processing. It couples a cloud-hosted web interface with asynchronous integration patterns to decouple users from legacy system lag.

## Key Elements
* External Users: Customers, Brokers, and Claims Adjusters
* New Claims Platform: Azure App Service web application hosted in Azure West Europe
* Integration Layer: Azure API Management Gateway and Azure Service Bus
* System of Record: On-premise COBOL/DB2 Legacy Mainframe

## Relationships
* Customers and Brokers interact with the New Claims Platform via HTTPS for online claim submission
* Claims Adjusters interact with the New Claims Platform via HTTPS for claim handling
* New Claims Platform interacts with the Legacy Mainframe via REST/HTTPS for synchronous queries through the API Gateway
* New Claims Platform interacts with the Legacy Mainframe via AMQP/HTTPS using Azure Service Bus for asynchronous claim state updates
* Services authenticate against Azure Active Directory (Entra ID) using OpenID Connect (OIDC) / OAuth 2.0

## Technology Stack
* Cloud Provider: Hybrid (On-premise mainframe and Azure West Europe)
* Compute & Hosting: Azure App Service for containerized web applications
* Integration & Messaging: Azure API Management Gateway and Azure Service Bus with Dead-Letter Queues
* Security & Identity: Azure Active Directory (Entra ID), Azure Key Vault, and TLS 1.3 with mTLS
* Infrastructure & Observability: Azure Bicep/Terraform and Azure Application Insights

## Rationale
This architecture uses managed Azure services to offset the team's low cloud experience while enforcing strict security boundaries. An asynchronous integration layer and API gateway isolate the new platform from legacy mainframe lag and protect fragile quarterly interface constraints.