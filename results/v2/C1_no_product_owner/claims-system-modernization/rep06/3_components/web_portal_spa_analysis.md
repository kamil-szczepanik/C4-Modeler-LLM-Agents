## Overview
This system modernizes a regional insurer's 30-year-old mainframe claims platform through a hybrid cloud migration. It replaces legacy components incrementally while maintaining uninterrupted nightly batch processing and a 3-year mainframe system of record constraint.

## Key Elements
- Customers and Brokers
- Claims Adjusters
- Web Portal (SPA)
- Adjuster Workspace
- Claims Core API
- Integration & Sync Engine
- Identity & Access Proxy
- Claims Read Model & Cache
- Legacy Mainframe

## Relationships
- Customers and Brokers -> Web Portal (SPA): Submits online claims [HTTPS/REST]
- Claims Adjusters -> Adjuster Workspace: Manages claims [HTTPS]
- Web Portal (SPA) -> Identity & Access Proxy: Routes authenticated traffic [HTTPS]
- Identity & Access Proxy -> Claims Core API: Forwards API requests [REST/gRPC]
- Claims Core API -> Integration & Sync Engine: Publishes claim events [Azure Event Hubs / Kafka]
- Integration & Sync Engine -> Legacy Mainframe: Synchronizes batch data [File Transfer / DB2]

## Technology Stack
- Web Portal (SPA): React, TypeScript, Azure Static Web Apps for rapid CI/CD and low cloud overhead
- Backend Services: Spring Boot, Java, Azure Kubernetes Service (AKS) for containerized claim processing
- Messaging: Azure Event Hubs with Kafka interface for reliable event streaming
- Database: Azure Cosmos DB (SQL API) for high-performance read models and caching
- Security: Azure Key Vault, Azure API Management (APM), OAuth2, OIDC for secure single sign-on

## Rationale
The hybrid architecture isolates the expensive-to-change COBOL/DB2 mainframe while enabling incremental claim type migration to Azure. This approach ensures zero data loss, meets strict sub-2-second performance goals, and accommodates the team's limited cloud experience via managed services.