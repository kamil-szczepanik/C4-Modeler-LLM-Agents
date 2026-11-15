## Overview
[The system modernizes a regional insurer's claims platform by gradually migrating claim types from a 30-year-old mainframe to a hybrid cloud environment. The architecture uses a dedicated Mainframe Adapter to encapsulate legacy protocols, ensuring zero data loss and enabling instant rollbacks during the 3-year transition.]

## Key Elements
* Customers and Brokers
* Claims Adjusters
* Claims API (BFF)
* Mainframe Adapter (Node.js/TypeScript in Azure Kubernetes Service)
* Legacy COBOL/DB2 Mainframe
* Azure Service Bus
* Azure Cosmos DB
* Azure Key Vault
* Azure Blob Storage

## Relationships
* Claims API (BFF) -> Mainframe Adapter: Invokes internal endpoints [gRPC/REST via Azure AD JWT/OAuth2]
* Mainframe Adapter -> Legacy COBOL/DB2 Mainframe: Communicates with on-premise legacy system [Mutually authenticated TLS (mTLS) over Azure ExpressRoute/VPN]
* Mainframe Adapter -> Azure Service Bus: Offloads shadow traffic and asynchronous events [AMQP/HTTPS]
* Mainframe Adapter -> Azure Key Vault: Retrieves secrets [Managed Identities]
* Mainframe Adapter -> Azure Blob Storage: Streams immutable audit logs [HTTPS]

## Technology Stack
* Node.js / TypeScript: Chosen for the Mainframe Adapter to build high-performance I/O integration layers
* Azure Kubernetes Service (AKS): Hosts containerized microservices with KEDA for event-driven autoscaling
* Express.js & Middleware: Implements routing, simulation modes, and circuit breaker resiliency patterns
* Azure App Configuration: Provides real-time feature toggling for instant claim type rollbacks
* Azure ExpressRoute / mTLS: Secures the hybrid boundary between Azure and the on-premise mainframe

## Rationale
[This hybrid architecture abstracts rigid mainframe constraints while meeting strict performance and consistency requirements. It allows incremental migration of claim types without destabilizing the system of record.]