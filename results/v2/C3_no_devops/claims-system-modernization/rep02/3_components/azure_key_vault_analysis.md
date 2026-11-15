## Overview
[The Azure Key Vault system provides secure secret, key, and certificate management for the Insurance Claims Modernization platform. It ensures secure hybrid integration with the legacy mainframe while protecting sensitive customer PII.]

## Key Elements
* DevOps & Security Engineers
* Secrets Management Component
* Keys (HSM) Management Component
* Certificates Management Component
* Telemetry & Audit Logging Component

## Relationships
* Claims Processing Core to Secrets Management Component via HTTPS (REST API) using Azure Managed Identities
* Audit & Reconciliation Ledger to Keys Management Component via Azure RBAC for Customer-Managed Keys (CMK)
* Customer Portal and Adjuster Workspace to Certificates Management Component via TLS 1.3
* Telemetry & Audit Logging Component to Azure Monitor / Sentinel via HTTPS/AMQP

## Technology Stack
* Azure Key Vault: Centralized secret and key management to abstract complex encryption for the team with limited cloud experience
* Azure Private Link: Provides network isolation via Private Endpoints within the Azure Virtual Network
* Azure RBAC: Enforces the principle of least privilege for secret and key access
* Azure Monitor Diagnostic Settings: Streams audit logs and telemetry for compliance and alerting

## Rationale
[This architecture secures hybrid credentials and customer PII while accommodating the team's limited cloud experience through managed identities and SDK abstraction. It ensures regulatory compliance and operational safety during the gradual migration from the legacy mainframe.]