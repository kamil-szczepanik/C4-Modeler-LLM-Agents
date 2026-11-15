## Overview
The Core Circulation & Cataloguing Service manages public and academic library inventories, loans, and fines. It provides secure transaction processing and metadata management while strictly enforcing EU data residency constraints.

## Key Elements
* API Gateway (Nginx/Kong)
* Core Circulation & Cataloguing Service (Spring Boot)
* Security Context Interceptor
* Circulation Engine
* Cataloguing Manager
* Transaction Event Publisher
* PostgreSQL (EU-hosted)
* RabbitMQ
* External Identity Provider (IdP)

## Relationships
* API Gateway -> Security Context Interceptor: Forwards authenticated requests [mTLS, gRPC/REST over TLS 1.3]
* Security Context Interceptor -> Circulation Engine / Cataloguing Manager: Delegates validated execution contexts [In-process method calls]
* Circulation Engine -> PostgreSQL: Persists transactional state and applies pessimistic locking [JDBC over TLS 1.3]
* Transaction Event Publisher -> RabbitMQ: Publishes signed domain events like `ItemCheckedOut` [AMQP over TLS 1.3]

## Technology Stack
* Spring Boot: Chosen for the Core container to provide robust ACID transaction handling and enterprise modularity.
* Spring Data JPA: Utilized with pessimistic locking to safely manage high-concurrency inventory check-outs.
* PostgreSQL: Serves as the primary transactional datastore with EU hosting and column-level PII encryption.
* RabbitMQ & Spring AMQP: Asynchronously dispatches domain events to unblock search indexing and notifications.
* HashiCorp Vault: Secures database credentials and event-signing keys outside configuration files.

## Rationale
This architecture uses a modular monolith pattern within Spring Boot to isolate core library domains while guaranteeing strict ACID compliance for financial and inventory states. Leveraging mTLS, JWT validation, and event-driven decoupling satisfies strict EU data residency and low-latency performance constraints.