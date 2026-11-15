## Overview
[The system is a hybrid Insurance Claims Modernization platform that gradually replaces a legacy 30-year-old COBOL/DB2 mainframe claims system. Its core purpose is to enable online claim submission and adjuster workflows while maintaining zero downtime and strict data consistency during a 3-year migration.]

## Key Elements
* Customer and Broker
* Claims Adjuster
* Claims Operations Manager
* On-premise COBOL/DB2 Legacy Mainframe
* Azure API Management
* Claims Processing Service (Java, Spring Boot, Azure Container Apps)
* Migration Dashboard (React, Node.js, Azure Container Apps)
* Azure Service Bus
* Azure Logic Apps / Functions (Inbound Integration Workflow, Mainframe Sync Function, Operations Telemetry Forwarder, Exception Triage Orchestrator, Replay & Audit API)
* Azure SQL Database
* Azure Key Vault
* Azure Active Directory (Entra ID)
* Azure Application Insights

## Relationships
* Customer and Broker submit claims to Azure API Management via HTTPS/TLS 1.3.
* Claims Adjuster interacts with Claims Processing Service and Migration Dashboard via HTTPS.
* Azure API Management routes requests to Claims Processing Service and Azure Service Bus using HTTPS/AMQP.
* Mainframe Sync Function communicates with On-premise COBOL/DB2 Legacy Mainframe using HTTPS/TCP/SNA with mTLS.
* Replay & Audit API connects to Azure Service Bus to securely push deduplicated messages using AMQP.
* Azure Logic Apps / Functions securely retrieve secrets from Azure Key Vault via Managed Identities.

## Technology Stack
* Azure Container Apps: Hosts microservices providing serverless container scaling with minimal cloud expertise required.
* Azure Service Bus: Manages asynchronous message queuing to guarantee zero lost or duplicated claims (R-04).
* C# .NET 8 Isolated Worker: Powers Azure Functions for robust protocol adaptation within the 5-second timeout window.
* Azure Active Directory (Entra ID): Enforces OAuth 2.0 / OpenID Connect Single Sign-On and RBAC.
* Azure Key Vault: Secures connection strings and encryption keys via Managed Identities.

## Rationale
[This hybrid architecture abstracts complex legacy integration protocols using managed Azure services, minimizing operational overhead for a cloud-novice team. It strictly enforces business continuity requirements by isolating the fragile mainframe and providing robust exception handling, idempotency, and audit trails.]