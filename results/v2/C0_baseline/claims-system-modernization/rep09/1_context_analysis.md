## Overview
The system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern cloud-native platform in a hybrid environment. It ensures business continuity, data consistency, and single sign-on while migrating claim types sequentially.

## Key Elements
- **Customers & Brokers:** External users submitting claims online.
- **Claims Adjusters:** Internal users handling claims via the modern web application.
- **Migration Operators:** Risk and operations staff managing data consistency and rollbacks.
- **Modern Claims Platform:** Cloud-native system hosted in Azure West Europe.
- **Legacy Mainframe:** On-premise COBOL/DB2 system of record.
- **Azure API Management (APIM):** Gateway acting as the single secure entry point.
- **Azure Service Bus:** Asynchronous integration broker with Dead-Letter Queues.
- **External Identity Provider:** On-premises Active Directory.

## Relationships
- Customers, Brokers, and Adjusters interact with the Azure API Management gateway via HTTPS.
- Azure API Management integrates with the Modern Claims Platform using REST/gRPC.
- Modern Claims Platform connects to the Legacy Mainframe via asynchronous messaging over Azure Service Bus secured by TLS 1.3 and mTLS.
- Modern Claims Platform authenticates users against Active Directory via OIDC/SAML.

## Technology Stack
- **Azure West Europe:** Cloud region hosting the modern microservices to meet performance requirements.
- **Azure API Management (APIM):** Centralizes ingress, mTLS enforcement, OAuth2 token validation, and rate-limiting.
- **Azure Service Bus:** Handles reliable asynchronous messaging and dead-letter queuing to respect the mainframe batch window.
- **Azure Application Insights:** Provides centralized logging and distributed tracing for operational observability.
- **Active Directory:** Manages single sign-on and identity federation.

## Rationale
- The hybrid architecture abstracts mainframe constraints using Azure APIM and Service Bus, enabling sub-two-second adjuster UI responses despite slow mainframe backends.
- Managed Azure services and centralized gateway policies offset the team's limited cloud experience while ensuring strict data consistency and zero-day rollback capabilities.