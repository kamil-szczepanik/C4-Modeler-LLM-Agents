## Overview
The Core Domain container is a modular Spring Boot application designed to manage library item cataloguing, circulation logic, and search synchronisation. It ensures reliable transactional integrity while meeting strict EU data residency and sub-800ms search performance requirements.

## Key Elements
* **Catalog Management Component**: Handles physical and digital item cataloguing (R-01).
* **Circulation Engine Component**: Manages loans, reservations, and business invariants.
* **Event Publisher Component**: Asynchronously emits domain events using Spring AMQP.
* **Search Synchronizer Component**: Updates the search index to achieve < 800 ms search responses (R-05).
* **PostgreSQL Database**: Stores transactional domain data locally.
* **Search Engine**: Externalized index providing fast catalog queries.
* **Message Broker**: Handles asynchronous message distribution.

## Relationships
* **Catalog Management** & **Circulation Engine** -> **PostgreSQL Database**: Reads and writes transactional data via native TCP drivers over TLS enforcing EU-only data residency.
* **Circulation Engine** -> **Event Publisher**: Communicates via in-process Spring Beans and direct method calls.
* **Event Publisher** -> **Message Broker**: Publishes domain events via AMQP over TLS.
* **Catalog Management** -> **Search Synchronizer**: Triggers indexing updates via direct method calls.
* **Search Synchronizer** -> **Search Engine**: Updates indices via native TCP drivers over TLS.

## Technology Stack
* **Java & Spring Boot**: Core runtime framework providing a modular monolith structure.
* **Spring Data JPA / Spring TX**: Manages data access and strict transactional boundaries.
* **Spring AMQP**: Handles asynchronous event publishing.
* **PostgreSQL Database**: Relational datastore ensuring strict EU data residency.
* **Search Engine (Elasticsearch)**: External search index ensuring high-performance catalog searches.

## Rationale
This modular monolith architecture keeps transactional integrity high using in-process Spring Beans while cleanly separating concerns. Bypassing the transactional database for search queries directly addresses the < 800 ms latency requirement (R-05) and respects EU data residency constraints.