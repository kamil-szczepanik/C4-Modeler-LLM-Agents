## Overview
The system modernizes a regional insurer's claims platform by gradually migrating claim types from a 30-year-old legacy mainframe to a cloud-native architecture over a three-year period. It ensures seamless online submissions for customers and brokers while maintaining business continuity through a hybrid operational model.

## Key Elements
* Policyholders (Customers) and Brokers
* Claims Adjusters
* Modern Claims Platform (Azure West Europe)
* Legacy Mainframe System of Record (COBOL/DB2 on-premise)
* Insurer Active Directory / Entra ID
* Enterprise Notification System
* Azure Service Bus

## Relationships
* Policyholders & Brokers -> Modern Claims Platform: HTTPS (REST/GraphQL) for online claim submissions (R-01)
* Claims Adjusters -> Modern Claims Platform: HTTPS for claim handling (R-02)
* Modern Claims Platform <-> Legacy Mainframe: Hybrid VPN, mTLS, and Azure Service Bus for claim type migration and dual-run sync (R-03, R-04)
* Modern Claims Platform -> Insurer Active Directory: OIDC/OAuth 2.0 for Single Sign-On (R-07)
* Modern Claims Platform -> Enterprise Notification System: HTTPS/SMTP for claim status updates (R-01)

## Technology Stack
* Azure App Service / Kubernetes & .NET/Java: Hosts the modern cloud platform in West Europe for scalability and performance.
* Azure Service Bus: Asynchronously decouples systems to protect the rigid nightly batch window and mainframe latency.
* Azure Key Vault with Managed Identities: Secures credentials and prevents hardcoding, mitigating cloud inexperience risks.
* Azure Bicep: Enforces Infrastructure-as-Code to minimize deployment human errors.
* Azure Monitor / Application Insights: Provides centralized distributed tracing and business-driven observability for state parity and R-06 rollbacks.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies while empowering an inexperienced cloud team with robust managed Azure services. It guarantees zero data loss, strict security boundaries, and rapid rollback capabilities during the three-year incremental migration.