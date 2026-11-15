## Overview
This system modernizes a regional insurer's claims platform by gradually migrating claims from a 30-year-old legacy mainframe to a cloud-native Azure environment. It ensures business continuity through a hybrid architecture where the legacy system remains the system of record for three years.

## Key Elements
- **Customers & Brokers**: External users submitting claims online.
- **Claims Adjusters**: Internal staff handling claims via a new web application.
- **Insurance Claims Modernization Platform**: Cloud-hosted core system running in Azure West Europe.
- **Legacy Mainframe System**: On-premises COBOL/DB2 system of record.
- **Core Integration Hub**: Anti-corruption layer bridging Azure and the mainframe.
- **Insurer's Active Directory**: Identity Provider (Entra ID).
- **Payment Gateway & Notification System**: External services for payouts and SMS/Email updates.

## Relationships
- **Customers & Brokers to Modernization Platform**: HTTPS / OIDC / MFA for online claim submission.
- **Claims Adjusters to Modernization Platform**: HTTPS / OIDC / OAuth 2.0 for claim handling.
- **Modernization Platform to Core Integration Hub**: Internal REST APIs / Messaging.
- **Core Integration Hub to Legacy Mainframe System**: mTLS, IPsec VPN / Azure ExpressRoute for hybrid data synchronization.
- **Modernization Platform to Insurer's Active Directory**: OIDC / SAML for Single Sign-On.
- **Modernization Platform to Notification System**: HTTPS / REST for automated status updates.

## Technology Stack
- **Azure West Europe**: Cloud provider hosting the modern web application and integration hub to overcome limited cloud experience.
- **Azure Key Vault**: Manages secrets, API keys, and credentials using managed identities.
- **COBOL / DB2**: Existing on-premises mainframe technology maintained as the system of record.
- **OAuth 2.0 / OIDC**: Protocol for Single Sign-On and multi-factor authentication integrated with Active Directory.
- **mTLS & IPsec VPN / Azure ExpressRoute**: Security protocols ensuring encrypted and isolated cross-network communication.

## Rationale
The hybrid architecture protects the fragile, expensive-to-change mainframe while enabling rapid delivery of modern cloud user interfaces. The Integration Hub isolates legacy latency and batch constraints to guarantee sub-2-second UI responses and strict data consistency.