## Overview
This system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern cloud-native platform on Microsoft Azure West Europe while maintaining regional business continuity. It uses a hybrid architecture with a Strangler Fig pattern to migrate claim types incrementally over a 3-year period.

## Key Elements
* Policyholder / Broker (Users): Submit online claims.
* Claims Adjuster (User): Handle claims via the new web application.
* Insurance Claims Modernization Platform (Software System): Azure-hosted cloud-native platform utilizing Azure App Service and Azure Service Bus.
* Legacy Mainframe (External System): On-premise COBOL/DB2 system acting as the system of record.
* Active Directory / Entra ID (External System): Corporate identity provider for Single Sign-On.
* Notification Service (External System): Third-party email and SMS gateway.
* Payment Gateway (External System): Enterprise financial system for payouts.
* Azure API Management (Container): Manages inbound/outbound API traffic, circuit breakers, and OAuth 2.0 enforcement.
* Azure Key Vault (Container): Secures secrets and API keys using managed identities.

## Relationships
* Policyholders & Brokers -> Modernization Platform: HTTPS/TLS for online claim submission.
* Claims Adjusters -> Modernization Platform: HTTPS/TLS via Web App for claim handling.
* Modernization Platform <-> Legacy Mainframe: Asynchronous messaging/ETL during the 23:00-05:00 batch window over mTLS.
* Modernization Platform -> Active Directory / Entra ID: OIDC/OAuth 2.0 for Single Sign-On.
* Modernization Platform -> Notification Service: HTTPS/REST via Azure API Management for customer updates.
* Modernization Platform -> Payment Gateway: HTTPS/REST via Azure API Management for disbursement tracking.

## Technology Stack
* Microsoft Azure West Europe: Chosen for native Active Directory integration and managed services to offset low cloud experience.
* Terraform / Bicep: Used for Infrastructure as Code to ensure reproducible Azure environments.
* OpenTelemetry: Implemented for distributed tracing across on-premise mainframe and Azure components.
* Azure API Management & Key Vault: Enforces OAuth 2.0, circuit breakers, IP whitelisting, and secure secret management.
* Strangler Fig Pattern with Feature Flags: Enables independent 1-day rollbacks of migrated claim types without mainframe code changes.

## Rationale
The hybrid architecture protects business value by keeping the stable mainframe as the system of record while incrementally migrating claim types via Azure managed services. This minimizes expensive mainframe changes, stays within batch window constraints, and accommodates the team's low cloud expertise.