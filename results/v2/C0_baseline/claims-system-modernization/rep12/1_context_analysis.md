## Overview
[The Insurance Claims Modernization platform gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-hosted web application. It enables incremental claim-type migration while the legacy system maintains the system of record.]

## Key Elements
* End Customers & Brokers
* Claims Adjusters
* Insurance Claims Modernization Platform (Azure App Service, Kubernetes, PostgreSQL)
* Legacy Mainframe (z/OS, DB2, CICS)
* Corporate Active Directory (Microsoft Entra ID / AD)
* Notification Service (SendGrid / Azure Communication Services)
* Payment Gateway (Regional Banking API)

## Relationships
* End Customers & Brokers -> Modern Platform (HTTPS)
* Claims Adjusters -> Modern Platform (HTTPS)
* Modern Platform <-> Legacy Mainframe (Asynchronous messaging / ETL via secure gateway with mTLS)
* Modern Platform -> Corporate Active Directory (OIDC/SAML)
* Modern Platform -> Notification Service (HTTPS)
* Modern Platform -> Payment Gateway (REST/JSON over mTLS with payload signatures)

## Technology Stack
* Azure App Service & Kubernetes: Cloud hosting for scalable containerized modern microservices
* PostgreSQL: Modern relational database for migrated claim types
* Microsoft Entra ID (Active Directory): Centralized IAM for SSO and RBAC
* Azure Key Vault: Secure management of secrets, API keys, and certificates
* OpenTelemetry: Distributed tracing across Azure and on-prem mainframe

## Rationale
[A hybrid architecture with an Anti-Corruption Layer decouples the modern Azure platform from the fragile legacy mainframe, ensuring strict data consistency and fast UI performance. This isolates expensive mainframe change cycles while enabling incremental claim migration and rapid rollbacks.]