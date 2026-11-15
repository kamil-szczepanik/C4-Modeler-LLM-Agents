## Overview
[The Claims Core Service is a Spring Boot component within a hybrid architecture that modernizes a legacy insurance mainframe. It enables incremental claim migration, ensures data consistency, and maintains high performance for adjusters.]

## Key Elements
* Claim Submission Controller (Spring MVC)
* Validation & Policy Component (Bean Validation / JSR-380)
* Claim Routing Engine
* Claim Processing Domain Service (Spring Data JPA)
* Read-Through Cache Component (Spring Cache)
* Outbox Event Publisher
* Reconciliation & Audit Listener

## Relationships
* Claim Submission Controller -> Validation & Policy Component: Validates incoming DTOs [In-process Method Call]
* Validation & Policy Component -> Claim Routing Engine: Passes validated domain commands [In-process Method Call]
* Claim Routing Engine -> Claim Processing Domain Service: Direct method invocation [In-process]
* Claim Routing Engine -> Anti-Corruption Layer: Delegates unmigrated types [gRPC over VNet]
* Claim Processing Domain Service -> Read-Through Cache Component: Reads/writes cached claim aggregates [In-process Method Call]
* Claim Processing Domain Service -> Outbox Event Publisher: Writes outbox messages [In-process Method Call]
* Outbox Event Publisher -> Message Broker (Azure Service Bus): Publishes domain events [AMQP over TLS]
* Claim Processing Domain Service -> Reconciliation & Audit Listener: Emits domain audit events [In-process Application Event]

## Technology Stack
* Java / Spring Boot: Core framework for business logic containerization on Azure App Service.
* Spring MVC: Exposes REST endpoints for claims handling.
* Bean Validation (JSR-380): Enforces structural payload validation.
* Spring Data JPA: Manages database interactions and transactional outbox persistence.
* Spring Cache: Powers the read-through cache integration for sub-2s UI response times.
* Azure Service Bus & gRPC: Facilitates secure messaging and hybrid mainframe communication.

## Rationale
[This modular component architecture ensures strict consistency and fast adjuster screen loads while safely interfacing with the legacy COBOL/DB2 mainframe. It directly supports incremental claim type migration and rapid 1-day fallback requirements.]