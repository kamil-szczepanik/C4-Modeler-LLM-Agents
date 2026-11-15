## Overview
The system is an insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe with a cloud-native architecture. It processes online claims and adjuster workflows while maintaining synchronization with the mainframe during a 3-year hybrid migration.

## Key Elements
- Users: Customers, Brokers, Claims Adjusters
- Frontend Container: Backend-for-Frontend (BFF) (Azure Container Apps)
- Core Business Container: Modular Monolith (Azure Container Apps)
- Integration Container: Anti-Corruption Layer (ACL) (Azure Container Apps)
- Messaging & Storage: Azure Service Bus, Azure Cosmos DB, Redis
- Security & Secrets: Active Directory, Azure Key Vault

## Relationships
- Customers/Brokers & Claims Adjusters -> BFF: Accesses claims via HTTPS/REST
- BFF -> Modular Monolith: Routes application logic via Internal HTTPS/REST
- Modular Monolith -> Azure Cosmos DB / Redis: Persists state and caches read models via TCP/TLS
- Modular Monolith -> Azure Key Vault: Retrieves secrets securely via HTTPS
- Modular Monolith -> Anti-Corruption Layer (ACL): Synchronizes claim events via Azure Service Bus (AMQP/HTTPS)
- Anti-Corruption Layer (ACL) -> On-Premises COBOL/DB2 Mainframe: Exchanges legacy claim data via proprietary TCP/IP protocols

## Technology Stack
- Azure Container Apps: Hosts containers due to managed infrastructure simplicity for teams with low cloud experience
- Modular Monolith Architecture: Reduces distributed system complexity while encapsulating domain logic
- Azure Cosmos DB & Redis: Provides scalable multi-model storage and fast read-projections for sub-2s UI loads
- Azure Service Bus: Enables reliable asynchronous messaging between the cloud platform and the mainframe
- ArchUnit: Enforces strict compile-time package boundaries and prevents domain leakage
- Pact: Provides automated contract testing for module and ACL interfaces

## Rationale
The modular monolith architecture minimizes distributed system overhead for a team with limited cloud experience while enforcing strict module boundaries. Asynchronous projections and transactional outbox patterns guarantee data consistency and performance without violating legacy mainframe constraints.