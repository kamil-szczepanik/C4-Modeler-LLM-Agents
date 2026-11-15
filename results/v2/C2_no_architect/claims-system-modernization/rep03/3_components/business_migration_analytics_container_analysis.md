## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern hybrid cloud platform. The Business/Migration Analytics Container provides real-time visibility into migration velocity, zero-loss reconciliation, and rollback readiness.

## Key Elements
*   **Users:** Claims Adjusters, Business Operations Managers, Migration Leads
*   **Containers:** Business/Migration Analytics Container (Python, Azure Analytics), Modern Web Application (React, ASP.NET Core)
*   **Messaging & Integration:** Azure Service Bus
*   **Infrastructure & Security:** Azure Application Gateway, Azure Key Vault, Azure Monitor Workbooks, Azure Private Subnet

## Relationships
*   **Business Operations Managers / Migration Leads -> Business/Migration Analytics Container:** Views migration dashboards and financial risk reports via OAuth2/OIDC over HTTPS/TLS 1.3.
*   **Business/Migration Analytics Container -> Azure Service Bus:** Ingests event streams via mTLS to process migration telemetry without direct mainframe polling.
*   **Business/Migration Analytics Container -> Azure Monitor Workbooks:** Visualizes metrics and dry-run simulation results via managed telemetry pipelines.
*   **Business/Migration Analytics Container -> Azure Key Vault:** Retrieves secrets and Customer-Managed Keys using Managed Identities.

## Technology Stack
*   **Analytics Engine:** Python (Chosen for data processing simplicity given low cloud experience)
*   **Visualization & Monitoring:** Azure Monitor Workbooks (Managed UI to avoid custom infrastructure overhead)
*   **Messaging Protocol:** TLS 1.3 / mTLS over Azure Service Bus (Secures hybrid event streaming)
*   **Security & Identity:** Azure Active Directory with OAuth2/OIDC and Managed Identities (Enforces RBAC and zero hardcoded credentials)

## Rationale
This architecture balances hybrid cloud constraints and strict zero-loss consistency requirements by isolating analytics on Azure without burdening the legacy mainframe. Using managed Azure services minimizes operational complexity for a team with low cloud experience while enforcing robust security and auditing controls.