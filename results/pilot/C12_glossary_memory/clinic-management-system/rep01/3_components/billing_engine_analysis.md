## Overview
The Billing Engine is an isolated Java Spring Boot container within the Clinic Management System designed to handle financial workflows, insurance claims, and payment processing. It ensures rapid claim generation, accurate financial reconciliation, and secure out-of-pocket balance settlements while complying with HIPAA and GDPR regulations.

## Key Elements
- Claim Generation Controller (Java Spring Boot component): Handles incoming internal gRPC requests and enforces token validation.
- Invoice Processor (Java Spring Boot component): Manages itemized statement logic and domain event publishing using Spring Events.
- Payment Orchestrator (Java Spring Boot component): Coordinates external financial transactions and outbox patterns.
- Billing Repository (Java Spring Boot component): Manages data access using Spring Data JPA with field-level encryption and Optimistic Locking.
- Database (PostgreSQL container): Encrypted PostgreSQL cluster providing ACID compliance and AES-256 encryption at rest.
- Insurance Payment Gateways (External System): External systems for processing insurance claims and payments.

## Relationships
- API Gateway -> Claim Generation Controller: Routes internal financial requests [Internal gRPC]
- Payment Orchestrator -> Insurance Payment Gateways: Coordinates external financial transactions [HTTPS REST over mutual TLS (mTLS) with public-key pinning]
- Billing Repository -> Database (PostgreSQL): Manages data access and persistence [JDBC with connection pooling and AES-256 encryption at rest]

## Technology Stack
- Java Spring Boot: Chosen as the core framework for building robust, enterprise-grade microservices within the container.
- PostgreSQL & Spring Data JPA: Selected for reliable ACID-compliant relational data storage with Optimistic Locking support.
- gRPC: Utilized for high-performance internal communication between the API Gateway and the Billing Engine.
- mTLS & HTTPS REST: Implemented for secure, encrypted external communication with payment gateways.

## Rationale
This architecture ensures 99.99% high availability and financial data integrity through transactional outbox patterns, hexagonal isolation of core financial rules, and strict security controls. Field-level encryption, mTLS, and RBAC satisfy rigorous HIPAA and GDPR compliance mandates while supporting high-throughput billing operations.