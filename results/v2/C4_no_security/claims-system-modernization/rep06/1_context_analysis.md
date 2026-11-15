## Overview
The system incrementally modernizes a 30-year-old COBOL/DB2 mainframe claims platform into an Azure-hosted cloud solution. It enables online claim submission and adjuster processing while maintaining legacy data consistency during a multi-year migration.

## Key Elements
* Policyholders and Insurance Brokers (Users)
* Claims Adjusters (Users)
* New Insurance Platform (Azure App Service, Azure Functions, Azure West Europe)
* Legacy Mainframe (On-premises COBOL/DB2 System of Record)
* Corporate Identity Provider (On-premises Active Directory)
* Audit & Compliance Archive (Azure Blob Storage with WORM policies)

## Relationships
* Policyholders and Brokers interact with New Insurance Platform via HTTPS
* Claims Adjusters use New Insurance Platform via HTTPS
* New Insurance Platform authenticates via Microsoft Entra ID federated with On-Premises Active Directory
* New Insurance Platform communicates asynchronously with Legacy Mainframe via Enterprise Service Bus / Message Queues
* New Insurance Platform streams audit logs to Audit & Compliance Archive via Azure Event Hubs

## Technology Stack
* Microsoft Azure App Service / Functions (PaaS for low-cloud-experience team)
* Microsoft Entra ID (Out-of-the-box Single Sign-On)
* Azure Event Hubs (Asynchronous log streaming)
* Azure Blob Storage (WORM-compliant audit retention)
* Infrastructure-as-Code via Bicep or Terraform (To prevent configuration drift)

## Rationale
The hybrid architecture shields the cloud platform from rigid mainframe batch windows and slow response times. Utilizing Azure PaaS and managed services minimizes operational complexity for a team with limited cloud experience while ensuring strict zero-data-loss compliance.