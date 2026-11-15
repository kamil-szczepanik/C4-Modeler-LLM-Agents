## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe while maintaining data consistency. It enables online submissions, fast adjuster processing, and incremental claim type migration over a 3-year period.

## Key Elements
* **Users:** Customers, Brokers, Claims Adjusters, and Finance/Compliance Auditors.
* **Modern Claims Platform (Azure West Europe):** Hosts the online portal, Adjuster Web App, Reporting & Reconciliation Service, and Transactional Outbox.
* **Legacy Mainframe Claims System (On-Premises):** COBOL/DB2 system acting as the enduring system of record.
* **Identity Provider:** Insurer's Active Directory / Azure AD.

## Relationships
* **Customer/Broker -> Modern Claims Platform:** HTTPS (Web/UI) for online claim submission.
* **Claims Adjuster -> Modern Claims Platform:** HTTPS for claim handling with sub-2s response times.
* **Modern Claims Platform <-> Legacy Mainframe:** Asynchronous message bus (MQ/Kafka) via Site-to-Site VPN / Azure ExpressRoute secured with Mutual TLS (mTLS).
* **Modern Claims Platform -> Identity Provider:** OIDC/OAuth 2.0 with MFA for Single Sign-On (R-07).

## Technology Stack
* **Cloud Infrastructure:** Azure App Service / AKS (Azure West Europe) chosen for managed services to offset limited cloud experience.
* **Integration & Consistency:** Asynchronous message broker with Transactional Outbox Pattern for zero-loss claim migration (R-04).
* **Performance & Caching:** Read-aside caching in the modern platform to bypass 5-second mainframe latency and meet sub-2s adjuster requirements (R-05).
* **Security & Compliance:** Azure Key Vault for secrets management; AES-256 encryption at rest; append-only storage for audit log integrity.

## Rationale
This hybrid architecture isolates the user-facing web tier from legacy mainframe latency while strictly adhering to the 3-year system-of-record constraint and interface change limits. Incremental claim migration and read-aside caching ensure fast adjuster response times and rapid 24-hour rollback capabilities.