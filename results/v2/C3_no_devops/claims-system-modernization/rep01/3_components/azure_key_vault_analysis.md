## Overview
[The system modernizes a 30-year-old mainframe claims platform using a hybrid cloud architecture to support online claims and adjuster workflows. Azure Key Vault provides secure, audited management of sensitive credentials and cryptographic keys for the new services.]

## Key Elements
* Secrets Management Component (Azure Key Vault Secrets)
* Key Management Component (Azure Key Vault Premium HSM-backed)
* Access Control & Audit Component (Azure RBAC & Azure Monitor)
* Secret Rotation Component (Azure Event Grid & Azure Functions)

## Relationships
* Claims Core Domain Service -> Secrets Management Component: Retrieves database and API credentials via HTTPS / Managed Identity (TLS 1.3)
* Claims Core Domain Service -> Key Management Component: Requests cryptographic keys for PII encryption at rest via HTTPS / Managed Identity (TLS 1.3)
* Secrets Management Component -> Azure Event Grid: Emits secret expiration events
* Azure Event Grid -> Secret Rotation Component: Triggers automated credential rotation via Managed Identity
* Azure Monitor -> Audit & Compliance System: Exports security and audit logs via syslog / Event Hubs

## Technology Stack
* Azure Key Vault Premium: HSM-backed security for stringent PII compliance and cryptographic key management
* Azure RBAC & Managed Identities: Eliminates hardcoded credentials and enforces least-privilege access
* Azure Event Grid & Azure Functions: Automates zero-downtime secret rotation to prevent human error
* Azure Private Endpoints: Secures network traffic within the Azure VNet, blocking public internet exposure

## Rationale
[This architecture secures sensitive insurance data through HSM-backed encryption and strict network isolation while minimizing operational complexity for an inexperienced cloud team via automated secret rotation. It ensures compliance and continuous auditing without introducing manual risks or downtime to the hybrid claims modernization process.]