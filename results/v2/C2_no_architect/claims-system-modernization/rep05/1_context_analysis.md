## Overview
This system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid cloud platform. It enables online claim submissions and adjuster processing while maintaining the legacy mainframe as the system of record.

## Key Elements
* Customers and Brokers: External users submitting claims online
* Claims Adjusters: Internal users managing claims in the new web application
* IT Administrators: Internal staff managing operational tooling, feature flags, and rollbacks
* Modern Claims Platform: Azure-hosted web application and CQRS read/write services
* Legacy System: On-premise COBOL/DB2 mainframe claims system

## Relationships
* Customers/Brokers interact with Modern Claims Platform via HTTPS (REST API)
* Claims Adjusters interact with Modern Claims Platform via HTTPS (OAuth 2.0 / OIDC)
* Modern Claims Platform communicates with Legacy System via mTLS and asynchronous messaging
* Modern Claims Platform integrates with Azure Active Directory (Entra ID) for SSO

## Technology Stack
* Cloud Provider: Hybrid architecture utilizing Azure West Europe and on-premise mainframe
* Integration & Messaging: Azure Service Bus with idempotent consumers and circuit breakers
* Security: Azure Key Vault for secrets management and AES-256 encryption
* Observability: Azure App Insights, Managed Grafana, and Prometheus for centralized monitoring
* Configuration: Azure App Configuration for feature flagging and schema versioning

## Rationale
The hybrid architecture protects business continuity by keeping the mainframe as the system of record during the three-year migration. CQRS and asynchronous messaging isolate the modern UI from mainframe latency to ensure sub-two-second response times.