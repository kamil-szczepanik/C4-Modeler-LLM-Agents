## Overview
A hybrid cloud architecture securely modernizes an aging regional insurer claims platform. It bridges an on-premises mainframe with Azure services while maintaining strict data consistency and compliance.

## Key Elements
- Security & Infrastructure Services (Azure Key Vault, CSI Secret Store Driver, Azure Monitor, Azure ExpressRoute)
- Claims Core API (Spring Boot, Java, Azure Kubernetes Service)
- Integration & Sync Engine (Azure Event Hubs with Kafka interface)
- Identity & Access Proxy (Azure API Management, OAuth2, OIDC)
- Insurer's Active Directory and Legacy Mainframe (On-premises)

## Relationships
- Claims Core API and Integration & Sync Engine read secrets from Azure Key Vault via local CSI volume mounts (FileSystem protocol).
- Claims Core API and Integration & Sync Engine send telemetry and audit logs to Azure Monitor via HTTPS (OpenTelemetry protocol).
- Identity & Access Proxy validates tokens against Insurer's Active Directory via OIDC/OAuth2 over HTTPS.
- On-premises Legacy Mainframe communicates with Azure components securely via Azure ExpressRoute using mTLS and TLS 1.3.

## Technology Stack
- Azure Key Vault with CSI Secret Store Driver: Manages and injects runtime secrets securely without hardcoding.
- Azure Monitor: Centralizes observability, metrics, and immutable audit logging.
- Azure ExpressRoute: Provides secure, dedicated hybrid networking between on-premises and Azure.
- Terraform/Bicep: Implements GitOps for automated infrastructure and security policy deployment.

## Rationale
This architecture addresses low cloud team experience by using managed Azure infrastructure services with automated pipelines and strict guardrails. It satisfies strict security, compliance, and hybrid connectivity constraints required during the mainframe migration phase.