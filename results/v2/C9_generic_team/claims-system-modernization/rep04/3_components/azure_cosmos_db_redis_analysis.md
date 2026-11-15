## Overview
The system is a hybrid cloud insurance claims modernization platform that gradually replaces a legacy COBOL/DB2 mainframe while maintaining continuous claim processing. It utilizes Azure services combined with local Docker emulation to ensure data consistency, rapid adjuster screen loads, and seamless rollback capabilities.

## Key Elements
- Azure Cosmos DB: Primary NoSQL state store and transactional outbox persistence layer.
- Azure Redis Cache: Distributed cache and locking mechanism utilizing a Cache-Aside strategy.
- Modular Monolith (Azure Container Apps): Core application container housing the strict data-access abstraction layer.
- Azure Key Vault: Centralized secret management provider accessed via Managed Identities.
- Docker Containers: Local development emulators for Cosmos DB and Redis.
- CI/CD Pipeline: Automated deployment and schema migration workflow.

## Relationships
- Modular Monolith -> Azure Cosmos DB: State persistence and transactional outbox caching via [TCP/TLS].
- Modular Monolith -> Azure Redis Cache: Distributed locking, cache-aside read/writes, and TTL management via [TCP/TLS].
- Modular Monolith -> Azure Key Vault: Secure retrieval of connection strings and access keys via [HTTPS/Managed Identities].
- Developers -> Docker Containers: Local emulation and transactional outbox testing via [Docker Bridge Network].

## Technology Stack
- Azure Cosmos DB: Chosen as the NoSQL state store with autoscale RU limits and strong session consistency to meet strict consistency requirements (R-04).
- Azure Redis Cache: Selected for distributed locking and Cache-Aside caching to achieve sub-2-second adjuster screen loads (R-05).
- Polly / SDK Retry Policies: Implemented within the abstraction layer for exponential backoff and circuit-breaker patterns.
- Azure Key Vault & Managed Identities: Utilized for secret-less credential injection to meet security mandates (R-07).
- Docker: Deployed locally for containerized database and cache emulation to support developers with limited cloud experience.

## Rationale
This architecture uses managed Azure data stores wrapped in a strict data-access abstraction layer to mitigate the team's low cloud experience while ensuring high maintainability and security. Automated schema migrations, local Docker emulation, and explicit caching patterns satisfy stringent consistency (R-04) and rapid rollback (R-06) requirements during incremental claim migrations.