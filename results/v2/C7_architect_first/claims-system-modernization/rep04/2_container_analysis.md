## Overview
The system is a hybrid cloud Insurance Claims Modernization platform that gradually replaces a 30-year-old COBOL/DB2 mainframe system. It delivers modern web applications for customers and adjusters while ensuring continuous claims processing.

## Key Elements
* Customer Portal (React, Azure Static Web Apps)
* Adjuster Workspace (.NET Core, Azure App Service)
* Claims Integration Service (.NET Core Worker Service, Azure Container Apps)
* Mainframe Adapter (.NET Core API, On-Premises)
* Azure Service Bus (AMQP message broker)
* Corporate Active Directory / Microsoft Entra ID
* Azure Key Vault with Managed Identities

## Relationships
* Customer/Broker interacts with Customer Portal via HTTPS/REST
* Adjuster interacts with Adjuster Workspace via HTTPS/REST
* Adjuster Workspace communicates with Claims Integration Service via gRPC over HTTP/2 (with mandatory TLS)
* Claims Integration Service publishes events to Azure Service Bus via AMQP
* Claims Integration Service communicates with Mainframe Adapter via REST/JSON over mTLS
* Mainframe Adapter integrates with legacy COBOL/DB2 Mainframe
* Applications authenticate users via OpenID Connect (OIDC) against Microsoft Entra ID

## Technology Stack
* Frontend: React (Azure Static Web Apps) for modern, responsive UI
* Backend Services: .NET Core on Azure App Service and Azure Container Apps for robust API and worker logic
* Messaging: Azure Service Bus (AMQP) for reliable asynchronous eventing and zero data loss
* Infrastructure & Security: Terraform/Bicep, GitHub Actions, Azure Key Vault, Managed Identities, and OpenTelemetry for observability
* Hybrid Connectivity: mTLS with certificate pinning for secure on-premise mainframe integration

## Rationale
This hybrid architecture isolates expensive mainframe changes behind a dedicated adapter while modernizing user-facing experiences in Azure. It leverages managed cloud services to minimize the team's cloud operational burden while ensuring zero data loss and strict maintainability.