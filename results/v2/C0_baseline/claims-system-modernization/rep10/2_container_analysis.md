## Overview
[A hybrid insurance claims modernization platform that gradually migrates claim types from a 30-year-old on-premises mainframe to Azure while maintaining legacy operations.]
[It ensures continuous business processing, data consistency, and low-latency adjuster workflows throughout the transition.]

## Key Elements
* **Customer Portal**: React Single Page Application hosted in Azure Static Web Apps.
* **Adjuster Workspace**: .NET Core web application deployed on Azure Container Apps.
* **Claim Routing & Feature Service**: Lightweight .NET Core API managing claim type migration via feature flags.
* **Claims Integration Service**: .NET Core worker/API handling data synchronization with the legacy mainframe.
* **Audit & Compliance Data Store**: Azure Cosmos DB paired with Azure Functions for unified audit trails.
* **Legacy Mainframe**: COBOL/DB2 on-premises system of record.
* **Infrastructure Services**: Azure Service Bus, Azure Key Vault, and Application Insights.

## Relationships
* **Customer/Broker to Customer Portal**: HTTPS over Internet.
* **Claim Adjuster to Adjuster Workspace**: HTTPS (OAuth 2.0 / OpenID Connect via Microsoft Entra ID).
* **Adjuster Workspace to Claim Routing Service**: gRPC over internal VNet.
* **Claim Routing Service to Claims Integration Service**: Azure Service Bus (asynchronous messaging).
* **Claims Integration Service to Legacy Mainframe**: Secure FTP / MQ over ExpressRoute/IPSec VPN with mTLS.

## Technology Stack
* **Azure Container Apps**: Standardized container hosting to accommodate the team's limited cloud experience.
* **.NET Core / C#**: Primary backend framework for microservices ensuring low-latency performance (<2s requirement).
* **Azure Service Bus**: Asynchronous message broker guaranteeing reliable, exactly-once processing and consistency.
* **Azure Cosmos DB**: Scalable NoSQL store for unified audit logging and compliance reporting.
* **Microsoft Entra ID**: Single Sign-On and token-based authorization via OAuth 2.0 / JWT.

## Rationale
[The hybrid architecture utilizes Azure Container Apps and managed services to minimize operational complexity for a cloud-novice team while strictly isolating claim logic for rapid one-day rollbacks.]
[Asynchronous messaging and circuit breakers protect the rigid on-premises mainframe batch window and ensure zero claim loss during incremental migration.]