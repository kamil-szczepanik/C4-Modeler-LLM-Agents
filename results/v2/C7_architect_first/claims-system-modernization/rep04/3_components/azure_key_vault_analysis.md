## Overview
[This system modernizes a 30-year-old regional insurer mainframe claims platform using a hybrid cloud architecture. It gradually migrates claim types to Azure while maintaining uninterrupted legacy processing and compliance.]

## Key Elements
* Adjuster Workspace (.NET Core, Azure App Service)
* Claims Integration Service (.NET Core Worker Service, Azure Container Apps)
* Mainframe Adapter (.NET Core API, On-Premises)
* Azure Key Vault with Managed Identities and Private Endpoints
* Azure Service Bus (AMQP)
* Legacy Mainframe (COBOL/DB2)
* Corporate Active Directory

## Relationships
* Adjuster Workspace and Claims Integration Service retrieve secrets from Azure Key Vault via HTTPS (REST API) using Azure Managed Identities over Private Endpoints.
* Adjuster Workspace interacts with Claims Integration Service via HTTPS (REST API).
* Claims Integration Service connects to Legacy Mainframe via Mainframe Adapter using mutual TLS (mTLS) over HTTPS.
* Claims Integration Service coordinates asynchronous messaging via Azure Service Bus using AMQP.

## Technology Stack
* .NET Core: Selected for containerized microservices due to strong ecosystem support.
* Azure Key Vault: Chosen for secure credential and certificate management using Hardware Security Module (HSM) backing.
* Azure Managed Identities: Utilized to eliminate hardcoded credentials and enforce token-only authentication.
* Azure Private Endpoints: Deployed to secure network traffic between Azure workloads and Key Vault.

## Rationale
[The hybrid architecture isolates expensive mainframe changes while enabling modern web workflows via Azure. Strict security controls and private networking satisfy compliance without impacting migration velocity.]