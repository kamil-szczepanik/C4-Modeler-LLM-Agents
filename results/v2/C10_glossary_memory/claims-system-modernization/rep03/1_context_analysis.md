## Overview
This system modernizes a regional insurer's 30-year-old mainframe claims platform through a gradual hybrid migration. It replaces legacy components while ensuring continuous claims processing and business continuity.

## Key Elements
* Customers & Brokers: External users submitting claims online
* Claims Adjusters: Internal users managing claims via the new web application
* New Insurance Claims Platform: Azure West Europe cloud-native services including Azure App Service, Azure Functions, and Azure API Management
* Migration Router / Facade: Architectural gateway handling incremental claim type routing and rollback
* Legacy Mainframe: On-premise COBOL/DB2 system of record
* Identity Provider: Corporate Active Directory / Azure AD
* Notification Service: SendGrid/Twilio external SMS/email provider

## Relationships
* Customers, Brokers, and Adjusters interact with the New Insurance Claims Platform via HTTPS/WSS
* New Insurance Claims Platform authenticates against Identity Provider via OpenID Connect/OAuth 2.0
* New Insurance Claims Platform synchronizes data with Legacy Mainframe via Azure Service Bus over Azure ExpressRoute/VPN
* New Insurance Claims Platform integrates with Notification Service via HTTPS REST API

## Technology Stack
* Cloud Platform: Azure West Europe for modern containerized and serverless workloads, addressing team inexperience through managed services
* Integration & Messaging: Azure Service Bus and Azure API Management to protect the legacy mainframe batch window
* Infrastructure & Security: Terraform/Bicep for GitOps, Azure Key Vault for secrets management, and Azure Application Insights for distributed tracing
* Hybrid Connectivity: Azure ExpressRoute or Site-to-Site VPN securing data in transit between cloud and on-premise

## Rationale
The hybrid architecture protects the 3-year mainframe system-of-record constraint while incrementally migrating claim types to the cloud. The Migration Router and asynchronous messaging ensure zero data loss, low adjuster latency, and rapid 1-day rollback capabilities.