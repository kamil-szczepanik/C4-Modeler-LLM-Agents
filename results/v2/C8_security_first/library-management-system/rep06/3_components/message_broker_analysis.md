## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The system ensures EU-only data residency and sub-800ms search responses.

## Key Elements
- **Users**: Library Patrons, Librarians/Catalogers, Library Administrators
- **External Systems**: EU Payment Gateway, National Library Database
- **Containers**: Patron Portal (Next.js), Librarian Dashboard (React), API Gateway (Kong/Envoy), Search & Catalogue Service (Elasticsearch/OpenSearch), Circulation Service (Node.js/Go), Notification Service (Node.js/Go), Integration Service (Python/Go), Message Broker (RabbitMQ), PostgreSQL Database (PostgreSQL with Read Replicas), Identity Provider (OAuth 2.0 / OIDC), HashiCorp Vault
- **Components (Message Broker)**: Exchange Routing Engine, Queue Manager, Consumer Delivery Manager, Dead-Letter Routing & Policy Engine, Access Control & TLS Termination Proxy

## Relationships
- Patron Portal -> API Gateway: HTTPS/REST [JSON]
- Librarian Dashboard -> API Gateway: HTTPS/REST [JSON]
- Circulation Service -> Message Broker: Publishes/consumes events [AMQP 0-9-1 via TLS 1.3]
- Notification Service -> Message Broker: Consumes events [AMQP 0-9-1 via TLS 1.3]
- Integration Service -> Message Broker: Publishes/consumes events [AMQP 0-9-1 via TLS 1.3]

## Technology Stack
- RabbitMQ: Chosen for flexible AMQP routing, per-queue dead-lettering, and fine-grained topic ACLs
- HashiCorp Vault: Provides dynamic credential generation and application-layer payload encryption for PII
- TLS 1.3 & mTLS: Enforces strict transport security and service authentication
- Kubernetes: EU-hosted clustered deployment for high availability and quorum queues

## Rationale
This architecture uses RabbitMQ with mirrored quorum queues across EU zones to guarantee zero data loss, sub-2-second event delivery, and strict GDPR compliance. Security controls like mTLS, Vault-backed encryption, and ACLs protect sensitive patron data without compromising performance.