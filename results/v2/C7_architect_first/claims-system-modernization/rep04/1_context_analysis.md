## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old on-premise mainframe with a cloud-native platform in Azure West Europe. It enables online claims submission and adjuster workflows while maintaining the legacy DB2/COBOL mainframe as the system of record.

## Key Elements
- **Actors:** Customer/Broker, Claims Adjuster.
- **External Systems:** Legacy Mainframe (On-premise DB2/COBOL), Corporate Active Directory (On-premise IDP).
- **Cloud Containers (Azure):** Insurance Claims Platform, Anti-Corruption Layer (ACL), CQRS Read Model, API Gateway.
- **Infrastructure:** Site-to-Site VPN, Azure Service Bus.

## Relationships
- Customer/Broker -> Insurance Claims Platform via HTTPS (Online submission).
- Claims Adjuster -> Insurance Claims Platform via HTTPS (Web UI).
- Insurance Claims Platform <-> Legacy Mainframe via Asynchronous Messaging/ETL over secure VPN (Strictly bound by 23:00-05:00 batch window).
- Insurance Claims Platform -> Corporate Active Directory via OIDC/SAML for SSO.

## Technology Stack
- **Cloud Provider:** Azure (West Europe) for managed services and reduced operational overhead given team cloud inexperience.
- **Integration/Messaging:** Azure Service Bus with dead-letter queues for asynchronous state sync without complex event-sourcing.
- **Security Protocols:** Mutual TLS (mTLS) over site-to-site VPN, AES-256 encryption at rest, OIDC/SAML, Azure Managed Identities.
- **Architectural Patterns:** Command Query Responsibility Segregation (CQRS) and Anti-Corruption Layer (ACL) for latency isolation and incremental migration.

## Rationale
This hybrid architecture isolates legacy latency to ensure sub-2-second adjuster screen loads while decoupling cloud domain models from rigid mainframe schemas. It satisfies strict migration constraints, ensuring zero data loss and enabling rapid one-day rollbacks per claim type.