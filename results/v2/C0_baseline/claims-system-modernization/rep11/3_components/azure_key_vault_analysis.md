## Overview
- Securely stores and manages system secrets, certificates, and integration credentials using Azure Key Vault with Managed Identities.
- Protects sensitive financial and customer data across a hybrid cloud and on-premise mainframe claims modernization architecture.

## Key Elements
- **Secrets Engine (Azure Key Vault Secret Management):** Stores connection strings and API keys for the Claims API and Mainframe Adapter.
- **Certificates Engine (Azure Key Vault Certificate Management):** Manages TLS/SSL certificates for secure ingress.
- **Access Policy & RBAC Enforcer:** Restricts access using Azure RBAC and Managed Identities with the principle of least privilege.
- **Private Endpoint Connector (Azure Private Link):** Isolates network traffic within the AKS Virtual Network.
- **Diagnostic Log Forwarder:** Streams audit events and telemetry to Azure Monitor / Log Analytics.

## Relationships
- Claims API -> Secrets Engine: Reads database secrets via [HTTPS via Private Endpoint / TLS 1.3]
- Mainframe Adapter -> Secrets Engine: Reads integration credentials via [HTTPS via Private Endpoint / TLS 1.3]
- Azure Key Vault -> Log Analytics: Emits audit and access logs via [Internal Azure Diagnostics]

## Technology Stack
- **Azure Key Vault:** Centralized secret and certificate management service.
- **Azure Managed Identities:** Eliminates hardcoded credentials for AKS-hosted containers.
- **Azure Private Link / Private Endpoints:** Disables public network access for network isolation.
- **Azure RBAC:** Enforces granular, role-based access control.
- **Azure Dedicated HSM:** Provides Customer-Managed Keys (CMK) for cryptographic isolation.
- **Azure Monitor / Log Analytics:** Collects diagnostic logs and triggers secret expiration alerts.

## Rationale
- Secures sensitive insurance data and PII while mitigating risks associated with the team's limited cloud experience.
- Enforces strict compliance, zero-trust network boundaries, and reliable hybrid claims processing.