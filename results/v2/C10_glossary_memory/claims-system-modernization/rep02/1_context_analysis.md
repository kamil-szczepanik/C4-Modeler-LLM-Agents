## Overview
The system gradually replaces a 30-year-old mainframe claims system with a modern cloud-based platform while the legacy system processes ongoing claims. It provides a hybrid architecture ensuring seamless incremental migration of claim types without service disruption.

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Operations and Support Staff
- Finance and Accounting
- Modern Claims Platform (Azure West Europe)
- Legacy Mainframe System (On-Premises COBOL/DB2)
- Enterprise Identity Provider (Active Directory / Entra ID)

## Relationships
- Customers, Brokers, Adjusters, Operations, Finance -> Modern Claims Platform via HTTPS/TLS (REST/GraphQL)
- Modern Claims Platform -> Enterprise Identity Provider via OpenID Connect (OIDC) for Single Sign-On (R-07)
- Modern Claims Platform <-> Legacy Mainframe System via Asynchronous Messaging / Enterprise Service Bus using encrypted TCP/MQ with mTLS
- Modern Claims Platform -> Finance/Accounting via SFTP / encrypted API feeds for financial reconciliation

## Technology Stack
- Azure App Service / Azure Container Apps: Hosts the Modern Claims Platform to meet the <2s performance requirement (R-05)
- Azure Service Bus: Asynchronous messaging to respect strict nightly batch windows (23:00-05:00)
- Azure API Gateway / Anti-Corruption Layer: Isolates the platform from schema drift given the constraint of at most one mainframe interface change per quarter
- Azure Key Vault: Manages secrets and automated certificate rotation for hybrid mTLS endpoints
- Azure Monitor / App Insights: Distributed tracing and tamper-proof audit logs to guarantee zero lost claims (R-04)

## Rationale
The hybrid architecture allows incremental migration of claim types one by one while keeping the COBOL/DB2 mainframe as the system of record. Fully managed Azure services offset the team's cloud inexperience while maintaining strict consistency and performance constraints.