## Overview
[The system is a hybrid Insurance Claims Modernization platform that gradually replaces a legacy COBOL/DB2 mainframe with a cloud-native architecture.]
[Its core purpose is to enable online claim submission and adjuster workflows while maintaining zero data loss and supporting a 3-year migration window.]

## Key Elements
- Customers and Brokers (Users)
- Claims Adjusters (Users)
- On-Premises COBOL/DB2 Mainframe (System of Record)
- Active Directory (Identity Provider)
- Azure Claims Modernization Platform (Modular Monolith Container)
- Backend-for-Frontend (BFF) Container
- Anti-Corruption Layer (ACL) Container
- Azure Service Bus (Message Broker)
- Azure Cosmos DB / Redis (State Store & Outbox Cache)
- Azure Container Apps (Orchestration Runtime)
- Azure Key Vault (Secrets Management)

## Relationships
- Customers/Brokers interact with the BFF via HTTPS/REST for online claim submission (R-01).
- Claims Adjusters interact with the BFF via HTTPS/REST for claim handling (R-02).
- BFF communicates with the Modular Monolith via internal HTTPS/REST.
- Modular Monolith connects to Azure Cosmos DB/Redis via TCP/TLS for transactional outbox persistence.
- ACL communicates with the On-Premises COBOL/DB2 Mainframe via legacy protocols over secure VPN/ExpressRoute.
- Azure Container Apps hosts the BFF, ACL, and Modular Monolith containers.
- Azure Key Vault integrates with all containers via HTTPS for centralized secret retrieval (R-07).

## Technology Stack
- Azure Container Apps: Chosen to provide managed serverless containers without Kubernetes complexity, fitting the team's low cloud experience.
- Modular Monolith Architecture: Selected over microservices to avoid distributed systems overhead while maintaining clean internal boundaries.
- Azure Service Bus: Implements asynchronous messaging to guarantee zero data loss (R-04) and decouple systems.
- Azure Cosmos DB / Redis: Used for state management, caching, and implementing the transactional outbox pattern.
- Azure Key Vault: Centralizes secrets management and Active Directory SSO integration (R-07).

## Rationale
[This hybrid architecture decouples modern web interfaces from the legacy mainframe via a BFF and Anti-Corruption Layer, meeting stringent performance and rollback constraints.]
[It balances cloud scalability with a modular monolith approach, minimizing operational risk for a team with limited cloud experience.]