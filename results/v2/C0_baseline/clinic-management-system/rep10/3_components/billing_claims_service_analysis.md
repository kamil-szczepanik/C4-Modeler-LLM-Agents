## Overview
The Billing & Claims Service manages patient financial transactions, insurance claim lifecycles, and patient payments for the Clinic Management System. It ensures secure, HIPAA-compliant, and highly available financial operations across hybrid cloud environments.

## Key Elements
- **Claim Generation Component** (Spring MVC / Domain Model)
- **Claim Tracking Component** (Spring Data JPA)
- **Audit Trail Component** (Spring AOP / JDBC with Transactional Outbox)
- **Patient Payment Portal Component** (Spring MVC / REST)
- **PostgreSQL Database** (AES-256 encrypted at rest)
- **RabbitMQ Message Broker** (AMQP)
- **HashiCorp Vault** (AppRole authentication)
- **Redis** (Idempotency cache)

## Relationships
- *Claim Generation Component* -> *PostgreSQL*: Persists billing records and PHI [JDBC / TLS]
- *Claim Tracking Component* -> *RabbitMQ*: Publishes claim status update events [AMQP]
- *Audit Trail Component* -> *PostgreSQL*: Writes immutable audit logs via Transactional Outbox [JDBC / TLS]
- *Patient Payment Portal Component* -> *PostgreSQL*: Reads statements and records payment transactions [JDBC / TLS]
- *Patient Payment Portal Component* -> *RabbitMQ*: Publishes payment success events [AMQP]
- *Patient Payment Portal Component* -> *Redis*: Validates idempotency keys [RESP / TLS]
- *Billing & Claims Service* -> *HashiCorp Vault*: Fetches secrets and API keys [API / TLS]

## Technology Stack
- **Java / Spring Boot**: Chosen for enterprise maturity, transactional consistency, and integration capabilities.
- **Spring Security & OAuth2/OIDC**: Enforces strict RBAC and granular scope validation (`billing:write`, `patient:pay`) to prevent IDOR.
- **Transactional Outbox Pattern**: Resolves audit logging consistency without impacting revenue-path latency or violating HIPAA.
- **Resilience4j**: Implements circuit breaking for external payment gateway integrations to prevent cascading failures.
- **External Payment Gateway SDK**: Enforces tokenization to eliminate raw PAN data and reduce PCI-DSS scope.

## Rationale
This architecture balances strict HIPAA and PCI-DSS compliance mandates with high availability (99.99%) through decoupled components, transactional outbox logging, and tokenization. It streamlines revenue operations and patient self-service while guaranteeing zero data loss and robust financial audit trails.