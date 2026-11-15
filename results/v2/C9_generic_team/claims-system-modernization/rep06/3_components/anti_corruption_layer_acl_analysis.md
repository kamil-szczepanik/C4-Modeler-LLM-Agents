## Overview
This system modernizes a regional insurer's 30-year-old claims platform by incrementally migrating claim types to Azure while retaining the on-premise mainframe as the system of record. It bridges legacy COBOL/DB2 systems with modern cloud components using an Anti-Corruption Layer to ensure zero data loss, strict security, and high performance.

## Key Elements
- Customers and Brokers (External Users)
- Claims Adjusters (Internal Users)
- On-Premise COBOL/DB2 Mainframe (System of Record)
- On-Premise Active Directory
- Web Application (SPA) (Azure App Service)
- Backend-for-Frontend (BFF) (Azure App Service)
- Anti-Corruption Layer (ACL) (Azure App Service)
- Message Broker (Azure Service Bus)
- Cache / Read Model Store (Managed Cloud Database)
- Observability (Azure Application Insights)

## Relationships
- Customers, Brokers, and Adjusters -> Web Application (SPA): Accesses online claim submission and adjuster screens [HTTPS]
- Web Application (SPA) -> Backend-for-Frontend (BFF): Communicates via [HTTPS/REST]
- Backend-for-Frontend (BFF) -> Anti-Corruption Layer (ACL): Communicates via [HTTPS/REST]
- Anti-Corruption Layer (ACL) -> On-Premise COBOL/DB2 Mainframe: Exchanges data via [Secure Mainframe Protocols]
- Anti-Corruption Layer (ACL) -> Message Broker (Azure Service Bus): Publishes and subscribes events via [Azure Service Bus Protocol]
- Web Application (SPA) -> On-Premise Active Directory: Authenticates via [Single Sign-On / OIDC/OAuth2]

## Technology Stack
- Azure App Service: Hosts modern web, BFF, and ACL containers for rapid deployment.
- Azure Service Bus: Provides asynchronous messaging and Outbox pattern support for reliable delivery.
- Managed Cloud Database / Cache: Implements read-through/write-through caching to satisfy sub-2s UI requirements.
- Azure Application Insights: Delivers distributed tracing and metrics instrumentation for hybrid observability.
- Clean Architecture / Ports & Adapters: Organizes ACL internal code to simplify maintenance despite low cloud experience.

## Rationale
This hybrid architecture isolates expensive mainframe dependencies behind a robust Anti-Corruption Layer while incrementally migrating claim types. It successfully reconciles strict legacy constraints, latency bottlenecks, and zero-data-loss requirements within Azure.