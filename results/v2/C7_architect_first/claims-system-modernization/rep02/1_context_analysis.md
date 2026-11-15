## Overview
The system is a hybrid cloud insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe while ensuring zero data loss and continuous operations. It provides modern digital claim submission for customers and a high-performance web application for claims adjusters.

## Key Elements
*   **Users:** Customers, Brokers, and Claims Adjusters
*   **Modern Platform:** Azure West Europe cloud-hosted web application and claims processing system
*   **Legacy System:** On-premises COBOL/DB2 Mainframe (System of Record)
*   **Integration Component:** Claims Anti-Corruption Layer (ACL) and Azure Service Bus with Dead Letter Queues
*   **Identity Provider:** Insurer Active Directory (On-premises) connected via Azure AD / Entra ID Connect

## Relationships
*   **Users to Modern Platform:** HTTPS via TLS 1.3 for web and mobile client access
*   **Modern Platform to Active Directory:** OIDC / OAuth2 over HTTPS for Single Sign-On (R-07)
*   **Modern Platform to Legacy Mainframe:** Asynchronous messaging through the Anti-Corruption Layer (ACL) via Azure Service Bus
*   **Hybrid Boundary:** Mutual TLS (mTLS) and TLS 1.3 encryption across all Azure-to-on-premises traffic

## Technology Stack
*   **Cloud Provider:** Microsoft Azure (West Europe region) to support managed services given limited cloud experience
*   **Integration & Messaging:** Azure Service Bus with Dead Letter Queues (DLQs) to handle mainframe batch window blackouts (23:00-05:00)
*   **Infrastructure as Code (IaC):** Terraform or Bicep for automated deployments and operational consistency
*   **Security & Identity:** OIDC/OAuth2, Azure AD / Entra ID Connect, and short-lived access tokens (max 1 hour)
*   **Observability:** OpenTelemetry for distributed tracing across the hybrid boundary

## Rationale
The hybrid architecture respects strict financial and operational constraints by keeping the COBOL/DB2 mainframe as the system of record while decoupling the new platform via an Anti-Corruption Layer and asynchronous messaging. This isolates expensive mainframe integration points, prevents data loss during nightly batch windows, and enables iterative claim-type migration with rapid one-day rollbacks.