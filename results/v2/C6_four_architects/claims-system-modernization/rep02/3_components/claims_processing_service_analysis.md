## Overview
[The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe with a modern Azure-based hybrid cloud platform. It processes online claims and adjuster workflows while keeping the legacy mainframe as the system of record.]

## Key Elements
* Claim Submission Controller (Spring MVC)
* Claims Security & Context Facade (Spring Security)
* Validation & Enrichment Engine (Spring Validation / Drools)
* Migration Strategy Router (Java SPI / Strategy Pattern)
* Claim Domain Model Core (Spring Data JPA)
* Outbox Event Publisher
* Mainframe Sync Listener (Spring Integration)

## Relationships
* Claim Submission Controller -> Claims Security & Context Facade [In-memory Filter / Method Call]
* Claims Security & Context Facade -> Validation & Enrichment Engine [In-memory Java Method Call]
* Validation & Enrichment Engine -> Migration Strategy Router [In-memory Java Method Call]
* Migration Strategy Router -> Claim Domain Model Core [In-memory Java Method Call]
* Migration Strategy Router -> Mainframe Integration Adapter [IBM MQ, asynchronous]
* Claim Domain Model Core -> Outbox Event Publisher [In-memory transactional boundary]
* Outbox Event Publisher -> Primary Datastore [JDBC over TLS]

## Technology Stack
* Java / Spring Boot: Core runtime for enterprise reliability and team familiarity
* Azure Container Apps: Scalable hosting environment for containerized services
* Azure SQL Database: Relational transactional persistence ensuring data consistency
* IBM MQ: On-premises messaging protocol for legacy mainframe communication
* Azure Active Directory (Entra ID): Single sign-on and security context propagation

## Rationale
[This architecture cleanly separates legacy integration from modern domain logic using a Strategy Pattern router, enabling incremental claim migration and a one-day rollback capability. The Transactional Outbox pattern guarantees zero data loss while respecting strict hybrid deployment constraints.]