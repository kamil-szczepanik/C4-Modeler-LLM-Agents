## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old on-premises mainframe claims system with a modern cloud-native platform in Azure West Europe. It uses a hybrid architecture with an integration gateway to enable incremental, claim-type-by-claim-type migration while the legacy mainframe remains the system of record.

## Key Elements
*   **External Users**: Customers, Brokers, and Claims Adjusters
*   **Modern Claims Platform**: Azure-hosted web application and API handling online submissions and adjuster workflows
*   **Legacy Mainframe**: On-premises COBOL/DB2 system acting as the system of record
*   **Integration Gateway**: Cross-boundary translation and routing component bridging Azure and the mainframe
*   **Insurer’s Active Directory**: Enterprise identity provider for single sign-on

## Relationships
*   Customers & Brokers to Modern Claims Platform: HTTPS (Web/API)
*   Claims Adjusters to Modern Claims Platform: HTTPS (Web/API with OAuth2/OIDC)
*   Modern Claims Platform to Integration Gateway: HTTPS/REST or AMQP over Azure Service Bus
*   Integration Gateway to Legacy Mainframe: IBM MQ over ExpressRoute with mTLS
*   Modern Claims Platform to Insurer’s Active Directory: OIDC / OAuth2

## Technology Stack
*   **Cloud Provider**: Azure West Europe (Hybrid deployment with on-premises mainframe)
*   **Compute & App Hosting**: Azure App Service (Managed PaaS to reduce operational overhead)
*   **Messaging & Integration**: Azure Service Bus and IBM MQ (Ensures reliable asynchronous delivery within batch windows)
*   **Security & Identity**: Azure Active Directory, Managed Identities, and Azure Key Vault (Eliminates hardcoded credentials and secures PII)
*   **Infrastructure & Automation**: Terraform/Bicep and Azure Policy (Compensates for low team cloud experience)
*   **Reliability & Resilience**: Outbox Pattern, feature flags, and dual-write routing (Guarantees zero data loss and enables 1-day rollback)

## Rationale
This hybrid architecture decouples the modern cloud frontend from the fragile legacy mainframe using asynchronous messaging and an integration gateway. It fulfills strict performance, security, and migration rollback requirements while accommodating the team's low cloud experience through managed PaaS and infrastructure-as-code.