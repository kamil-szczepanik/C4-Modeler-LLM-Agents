## Overview
[The system modernizes a 30-year-old regional insurer COBOL/DB2 mainframe claims platform through a hybrid cloud architecture. It provides online claim submission and adjuster workflows while ensuring continuous legacy synchronization and auditability.]

## Key Elements
* End Customers and Brokers
* Claims Adjusters and Claims Managers
* Legacy Mainframe
* Corporate Active Directory / Azure AD
* Analytics & Reporting System
* New Claims Platform
* Azure API Management (APM) Gateway
* Customer/Broker Portal
* Adjuster Workstation
* Integration & Routing Engine
* Observability & Audit Logging
* Secret Management

## Relationships
* End Customers and Brokers -> New Claims Platform [HTTPS]
* Claims Adjusters and Claims Managers -> New Claims Platform [HTTPS]
* New Claims Platform -> Legacy Mainframe [Azure ExpressRoute, mTLS, Azure API Management]
* New Claims Platform -> Analytics & Reporting System [Azure Event Hubs, TLS 1.3]
* Customer/Broker Portal -> Integration & Routing Engine [HTTPS / AMQP]
* Adjuster Workstation -> Integration & Routing Engine [HTTPS / AMQP]
* Integration & Routing Engine -> Azure API Management Gateway [HTTPS]
* Azure API Management Gateway -> Legacy Mainframe [Azure ExpressRoute, mTLS]

## Technology Stack
* Azure App Service: Hosts React portal and Angular workstation for low-latency UIs.
* Azure Functions & Azure Service Bus: Powers asynchronous queueing, routing, and audit event processing.
* Azure Cosmos DB Ledger mode: Ensures immutable, cryptographically verified audit trails for R-04 consistency.
* Azure Application Insights: Provides distributed telemetry and tracing across hybrid environments.
* Azure API Management: Protects legacy mainframe interfaces and handles rate-limiting.
* Azure Key Vault: Manages secrets, connection keys, and automated 90-day rotation.

## Rationale
[This hybrid architecture isolates expensive mainframe interfaces while enabling incremental cloud migration of claim types. It guarantees transactional consistency and fast UI response times despite legacy latency constraints.]