## Overview
This hybrid cloud architecture gradually replaces a 30-year-old mainframe claims system by migrating claim types incrementally to a modern Azure platform. It isolates the legacy system while ensuring zero data loss and sub-2-second adjuster response times.

## Key Elements
- **End Customers & Brokers**: External users submitting claims online.
- **Claims Adjusters**: Internal users processing claims via the new web application.
- **Migration Operations Lead**: Specialized user monitoring incremental cutovers and rollbacks.
- **Insurance Claims Modernization Platform**: Cloud-native target system hosted in Azure West Europe.
- **Legacy Mainframe System**: On-premises COBOL/DB2 system of record.
- **Corporate Active Directory**: On-premises identity provider.
- **Third-Party Payment Gateway**: External system handling outbound payouts.

## Relationships
- End Customers & Brokers -> Insurance Claims Modernization Platform [HTTPS/REST]: Online claim submission
- Claims Adjusters -> Insurance Claims Modernization Platform [HTTPS]: Web UI access
- Insurance Claims Modernization Platform <-> Legacy Mainframe System [MQ/Batch/API with mTLS]: Dual-run synchronization
- Insurance Claims Modernization Platform -> Corporate Active Directory [OIDC/SAML]: Single Sign-On authentication
- Insurance Claims Modernization Platform -> Third-Party Payment Gateway [HTTPS/REST with OAuth 2.0]: Outbound payouts

## Technology Stack
- **Azure App Service**: Hosts the modern web application for predictable scalability and reduced operational complexity given team skill gaps.
- **Azure Service Bus**: Manages asynchronous hybrid messaging with dead-letter queues to guarantee transactional consistency.
- **Azure Database for PostgreSQL**: Provides secure relational storage with AES-256 encryption at rest for migrated claim data.
- **ExpressRoute/VPN**: Secures hybrid transit between Azure and the on-premises mainframe using mutual TLS (mTLS).

## Rationale
The hybrid architecture decouples modern user experiences from legacy constraints, keeping expensive mainframe modifications under the quarterly limit. Managed Azure services mitigate the team's cloud experience gap while ensuring strict consistency and rapid rollback capabilities.