## Overview
This hybrid cloud architecture incrementally replaces a legacy mainframe insurance claims system using a strangler fig pattern. It ensures business continuity, high performance, and secure processing during a multi-year migration.

## Key Elements
* **Users:** Customers, Brokers, and Claims Adjusters
* **External Systems:** Legacy Mainframe (COBOL/DB2) and Active Directory
* **Edge / Security:** API Gateway / Edge (Azure API Management)
* **Frontend:** Claims Web App (React SPA on Azure Static Web Apps)
* **Backend Services:** Claims Core Service (Java/Spring Boot on Azure App Service), Anti-Corruption Layer (Azure Functions), Audit & Reconciliation Worker (Java/Spring Batch)
* **Integration:** On-Premise Integration Agent
* **Data & Messaging:** Modern Claims Database (Azure SQL Database), Read-Through Cache (Azure Cache for Redis), Message Broker (Azure Service Bus)

## Relationships
* Customers & Brokers to Claims Web App via HTTPS (REST)
* Claims Web App to API Gateway via HTTPS (REST / OpenID Connect)
* API Gateway to Claims Core Service via HTTPS (REST over internal VNet)
* Claims Core Service to Modern Claims Database via TDS (SQL)
* Claims Core Service to Read-Through Cache via Redis TCP
* Claims Core Service to Message Broker via AMQP over TLS
* On-Premise Integration Agent to Message Broker via outbound AMQP/HTTPS over TLS
* On-Premise Integration Agent to Legacy Mainframe via CICS/DB2 connectors
* API Gateway to Active Directory via OIDC/JWT

## Technology Stack
* **Frontend:** Azure Static Web Apps with React for rapid, responsive adjuster and customer UI (R-02, R-05)
* **Compute Platform:** Azure App Service & Azure Functions (Java/Spring Boot) chosen for enterprise familiarity given low cloud experience
* **Integration & Messaging:** Azure Service Bus paired with an On-Premise Integration Agent for secure, outbound-only hybrid connectivity
* **Data & Caching:** Azure SQL Database for ACID compliance (R-04) and Azure Cache for Redis to meet sub-2s performance goals (R-05)
* **Security:** Azure API Management integrated with Active Directory via OpenID Connect/JWT (R-07)

## Rationale
The hybrid cloud design respects strict on-premise mainframe constraints and limited cloud experience by leveraging managed PaaS and decoupled asynchronous messaging. This ensures seamless incremental claim type migration, robust data consistency, and rapid rollback capabilities without extending the nightly batch window.