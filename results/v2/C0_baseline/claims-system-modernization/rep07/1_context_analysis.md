## Overview
This system modernizes a regional insurer's claims platform by gradually migrating claim types from a 30-year-old mainframe to a cloud-native Azure environment. The hybrid architecture maintains business continuity and strict data consistency while operating alongside the legacy system of record.

## Key Elements
- End Customers & Brokers
- Claims Adjusters
- Operations Managers & Migration Auditors
- New Insurance Claims Platform (.NET Core, Azure Kubernetes Service)
- Legacy Mainframe (COBOL, DB2)
- Anti-Corruption Layer (ACL) & API Gateway
- Azure Service Bus with Dead-Letter Queues
- Identity Provider (on-premises Active Directory / Azure Entra ID)
- Centralized Audit Sink (Azure Application Insights, Azure Immutable Blob Storage)
- Infrastructure as Code (Bicep / Terraform)

## Relationships
- End Customers, Brokers, and Adjusters interact with the New Claims Platform via HTTPS/REST.
- New Claims Platform communicates with the Legacy Mainframe via asynchronous messaging over Azure Service Bus and an enterprise API Gateway.
- Hybrid services authenticate across boundaries using TLS 1.3 with mutual TLS (mTLS).
- Users authenticate via OpenID Connect (OIDC) / OAuth 2.0 integrated with Active Directory / Azure Entra ID.
- Claim state transitions log to Azure Immutable Blob Storage using WORM policies.

## Technology Stack
- **Azure Kubernetes Service (.NET Core):** Delivers scalable, cloud-native microservices for the new web application.
- **Azure Service Bus:** Provides asynchronous messaging and durable buffering to prevent message loss during batch windows.
- **Azure Key Vault & HSM:** Manages customer-managed keys for envelope encryption and hardware security module-backed mTLS certificates.
- **Azure Immutable Blob Storage:** Ensures tamper-proof, cryptographically immutable audit trails for compliance.
- **Bicep / Terraform:** Standardizes infrastructure as code to offset the team's limited cloud experience.

## Rationale
The hybrid architecture decouples the modern Azure platform from legacy mainframe constraints using an Anti-Corruption Layer and asynchronous messaging. This ensures <2s UI performance, strict data consistency, and rapid one-day fallback capabilities without modifying the legacy system more than once per quarter.