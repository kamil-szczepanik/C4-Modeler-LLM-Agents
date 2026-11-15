## Overview
The system is a hybrid cloud Modern Claims Platform that gradually replaces a 30-year-old COBOL/DB2 mainframe while maintaining continuous claims processing. It decouples cloud-native workflows from legacy constraints using asynchronous integration and bidirectional synchronization.

## Key Elements
* **Customer & Broker:** External actors submitting online claims via web UI.
* **Claims Adjuster:** Internal actor processing claims in the new web application.
* **IT Administrator:** Manages system administration and access.
* **Modern Claims Platform (Azure West Europe):** Cloud-native core system containing an API Gateway, BFF, Claims Domain Service, Anti-Corruption Layer (ACL), and Async Workers.
* **Legacy Mainframe (On-Premises):** COBOL/DB2 system of record handling nightly batch processing (23:00-05:00).
* **Insurer's Active Directory (Azure AD / Entra ID):** Enterprise identity provider for SSO.
* **Payment Gateway:** External third-party system for executing financial payouts.

## Relationships
* **Customer/Broker/Adjuster -> Modern Claims Platform:** HTTPS (TLS 1.3) for web UI interactions.
* **Modern Claims Platform -> Insurer's Active Directory:** OIDC / OAuth 2.0 over HTTPS for Single Sign-On.
* **Modern Claims Platform <-> Legacy Mainframe:** Azure Service Bus via AMQP/HTTPS for asynchronous bidirectional messaging and state synchronization.
* **Modern Claims Platform -> Payment Gateway:** REST / HTTPS for claim payout processing.

## Technology Stack
* **Cloud Platform:** Microsoft Azure (West Europe region) to host the modern containerized infrastructure.
* **Frontend & Backend:** React and ASP.NET Core for responsive UI and domain services.
* **Integration & Messaging:** Azure Service Bus (AMQP) to decouple latency and protect the strict batch window.
* **Security:** Azure AD / Entra ID using OIDC and OAuth 2.0 for centralized authentication.

## Rationale
The hybrid architecture isolates the cloud platform from rigid mainframe constraints and 5-second legacy latencies using asynchronous messaging, ensuring sub-2-second adjuster screen loads. Bidirectional synchronization via Azure Service Bus guarantees data consistency and enables a 24-hour fallback to the mainframe for migrated claim types.