## Overview
The Claims Core Engine is a Java Spring Boot container within a hybrid cloud platform designed to gradually modernize a legacy mainframe claims system. It enables incremental claim-type migration while ensuring transactional consistency, low-latency adjuster screens, and robust mainframe fallback capabilities.

## Key Elements
* Claim Domain Service (Java/Spring): Encapsulates core claims processing business logic using Domain-Driven Design.
* Adapter Router (Java/Spring Integration): Dynamically routes requests between the modern database and legacy mainframe.
* Anti-Corruption Layer (ACL) (Java / Resilience4j): Translates data models and insulates the system from mainframe latency and schema quirks.
* Event Publisher Component (Apache Camel): Handles asynchronous event dispatching for dual-run state synchronization.

## Relationships
* Adjuster Workspace -> Claim Domain Service: Executes commands and reads claims data via gRPC.
* Claim Domain Service -> Migrated Claims Database: Persists modern claim records via JDBC over TLS.
* Claim Domain Service -> Adapter Router: Delegates legacy fallback calls via in-process Java method calls.
* Adapter Router -> Anti-Corruption Layer: Transforms data structures for legacy compatibility.
* Anti-Corruption Layer -> Integration Layer: Synchronizes events and bridges mainframe data via AMQP over Azure Event Hubs.

## Technology Stack
* Java Spring Boot: Provides a robust framework for enterprise domain logic.
* Azure Container Apps: Hosts the containerized microservice securely.
* Azure Database for PostgreSQL: Acts as the data store for migrated claim types.
* Resilience4j: Protects against mainframe latency and enforces fault tolerance.
* Apache Camel: Facilitates enterprise integration patterns and message routing.

## Rationale
This component architecture isolates complex legacy integration logic behind an Anti-Corruption Layer and Adapter Router, fulfilling the requirement for a one-day rollback per claim type. It maintains strict data consistency and performance standards despite hybrid infrastructure constraints.