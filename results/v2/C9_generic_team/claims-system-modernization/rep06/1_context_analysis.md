## Overview
[The system modernizes a regional insurer's legacy COBOL/DB2 mainframe claims platform by incrementally migrating claim types to a hybrid cloud architecture. Its core purpose is to maintain continuous claims processing while transitioning workloads to a modern web application.]

## Key Elements
*   [Customers and Brokers]
*   [Claims Adjusters]
*   [Azure Web Application (Container)]
*   [Azure Anti-Corruption Layer / ACL (Container)]
*   [Azure Database with Snapshot State Versioning (Container)]
*   [Azure Observability Container]
*   [On-Premise COBOL/DB2 Mainframe (System of Record)]

## Relationships
*   [Customers and Brokers interact with Azure Web Application via HTTPS/REST for online claim submission]
*   [Claims Adjusters interact with Azure Web Application via HTTPS/REST for claim handling]
*   [Azure Anti-Corruption Layer communicates with On-Premise Mainframe via Secure VPN/ExpressRoute and synchronous REST/MQ APIs]
*   [Azure Web Application authenticates against On-Premise Active Directory via OAuth2/OpenID Connect (SSO)]

## Technology Stack
*   [Azure Cloud (West Europe) with local read-optimized cache for sub-2s UI performance]
*   [Transactional Outbox Pattern for guaranteed at-least-once hybrid message delivery]
*   [JSON Schema / Avro Schema Registry within ACL to prevent mainframe contract violations]
*   [CQRS Pattern to decouple synchronous UI from slow legacy dependencies]
*   [Snapshot State Versioning in Azure database for historical auditability and rollbacks]

## Rationale
[This hybrid architecture isolates the rigid, expensive-to-change on-premise mainframe using an Anti-Corruption Layer and asynchronous patterns, protecting system consistency. It accommodates the team's low cloud experience with well-defined C4 boundaries while meeting strict performance, security, and rollback requirements.]