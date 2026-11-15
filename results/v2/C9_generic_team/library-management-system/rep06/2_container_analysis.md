## Overview
[Library Management System] provides public and academic libraries with item cataloging, circulation management, and self-service portals under strict EU-only data residency constraints.

## Key Elements
* Patrons and Library Staff (Users)
* External Identity Providers (SSO/OAuth), Payment Gateways, and External Archival/Reporting System
* Client-Side SPA/Mobile Container (Self-service portals and staff apps)
* API Gateway Container (NGINX/Kong equivalent)
* Core Business Logic / Circulation API Container
* Search Engine Container (Elasticsearch/OpenSearch)
* Data Access Layer / Persistence Container (PostgreSQL/Relational database)
* Asynchronous Message Broker Container (RabbitMQ/Kafka)
* Background Workers Container
* Configuration & Secrets Management Container (HashiCorp Vault)
* Centralized Observability Container

## Relationships
* Client-Side SPA/Mobile to API Gateway Container via HTTPS (REST/GraphQL)
* API Gateway to Core Business Logic Container via internal gRPC/HTTP
* Core Business Logic to Search Engine Container via REST/gRPC (<800ms search SLA)
* Core Business Logic to Data Access Layer via TLS
* Core Business Logic to Asynchronous Message Broker Container via AMQP/Kafka Protocol
* Message Broker to Background Workers Container via event subscription
* External Identity Providers to API Gateway via OAuth2/OIDC
* Payment Gateways to API Gateway via HTTPS Webhooks

## Technology Stack
* API Gateway: NGINX / Kong for rate limiting, TLS termination, and JWT validation
* Search Engine: Elasticsearch / OpenSearch for sub-800ms search performance
* Persistence: PostgreSQL deployed exclusively within EU regions for data residency
* Message Broker: RabbitMQ / Kafka for decoupled event-driven processing
* Secrets Management: HashiCorp Vault for secure credential handling
* API Contracts: OpenAPI / Swagger specifications

## Rationale
Decoupling search, message brokering, and background tasks from core APIs ensures scalability and sub-800ms search performance. Strict network zoning and isolated EU persistence containers guarantee complete regulatory compliance.