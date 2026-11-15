## Overview
[The system modernizes a 30-year-old regional insurance claims mainframe by incrementally migrating claim types to a secure Azure-hosted platform. The Adjuster Backend Service acts as the core processing engine, utilizing an Anti-Corruption Layer to bridge cloud-native components with the legacy system.]

## Key Elements
* Claims Controller (Spring MVC / REST API)
* Claims Domain Service (Java / Spring Boot business logic)
* Mainframe ACL Adapter (Legacy translation layer)
* Persistence Repository (Spring Data JPA)
* Messaging Publisher (Azure Service Bus integration)
* Cache Manager Component (Azure Redis Cache interface)

## Relationships
* Adjuster Workspace -> Claims Controller: Submits adjuster operations [REST/HTTPS over TLS 1.3]
* Claims Domain Service -> Persistence Repository: Persists and retrieves claim data [Spring Data JPA / TDS]
* Claims Domain Service -> Cache Manager Component: Reads/writes transient claim views [Redis Protocol]
* Claims Domain Service -> Messaging Publisher: Emits asynchronous domain events [AMQP]
* Mainframe ACL Adapter -> Mainframe Integration Adapter: Communicates with legacy system [Internal API / mTLS]
* Adjuster Backend Service -> Azure Key Vault: Retrieves secrets and certificates [Managed Identities / HTTPS]

## Technology Stack
* Java 17 / Spring Boot: Selected for robust enterprise patterns and team familiarity
* Azure Container Apps: Chosen to containerize the service without microservices overhead given limited cloud experience
* Azure SQL Database: Provides persistent storage with Transparent Data Encryption (TDE)
* Azure Redis Cache: Reduces adjuster screen load times to under 2 seconds by bypassing mainframe latency
* Azure Service Bus: Ensures zero claim loss and handles queue-depth auto-scaling during nightly mainframe batch windows (23:00-05:00)

## Rationale
[The component-level architecture isolates high mainframe latency and rigid legacy interfaces behind a dedicated Anti-Corruption Layer, satisfying strict performance and 1-day fallback requirements. Enterprise security controls and containerized simplicity mitigate risks for a team with limited cloud experience.]