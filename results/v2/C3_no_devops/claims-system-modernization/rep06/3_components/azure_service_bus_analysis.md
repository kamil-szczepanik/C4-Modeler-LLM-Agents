## Overview
[The system is a modern hybrid cloud platform that gradually replaces a 30-year-old insurance mainframe claims system while maintaining continuous processing. It enables online claim submissions and adjuster workflows while incrementally migrating claim types.]

## Key Elements
- **Azure Service Bus**: Central messaging broker providing reliable asynchronous integration via Anti-Corruption Layer (ACL)
- **Claim Migration Topic & Subscriptions**: Pub/sub engine with session-based ordering for incremental claim-type routing
- **Mainframe Sync Queue**: Partitioned, transactional queue with duplicate detection for guaranteed consistency
- **Dead-Letter Queue (DLQ)**: Automated capture mechanism for poisoned messages and batch window lockouts
- **Azure Kubernetes Service (AKS)**: Host for Node.js/Java microservices interacting with the bus

## Relationships
- **Azure Kubernetes Service -> Azure Service Bus**: Publishes and consumes asynchronous messages using AMQP 1.0 over TLS 1.3
- **Azure API Management -> Azure Service Bus**: Sends asynchronous integration messages via AMQP 1.0
- **Azure Service Bus -> On-Premises COBOL/DB2 Mainframe**: Communicates legacy synchronization via mTLS over IPsec VPN / ExpressRoute

## Technology Stack
- **Azure Service Bus**: Selected for reliable transactional messaging and enterprise decoupling
- **AMQP 1.0**: Protocol for connection multiplexing and enterprise-grade reliability over hybrid boundaries
- **Azure Entra ID (Managed Identities)**: Replaces SAS connection strings to enforce least-privilege RBAC
- **Terraform**: Infrastructure-as-Code tool used to manage cloud components and prevent configuration drift

## Rationale
[This architecture successfully decouples high-performance cloud UI requirements from slow mainframe responses while ensuring zero data loss during incremental migration. It securely bridges the hybrid environment using robust message queuing and strict identity controls.]