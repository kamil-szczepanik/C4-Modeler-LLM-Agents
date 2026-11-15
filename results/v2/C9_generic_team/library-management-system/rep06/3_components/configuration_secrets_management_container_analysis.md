## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture enforces strict EU-only data residency and sub-800ms search performance.

## Key Elements
- Patrons and Library Staff
- Client-Side SPA/Mobile Container (Web/Mobile Technologies)
- API Gateway Container (NGINX / Kong)
- Core Business Logic / Circulation API Container (Microservice / API Runtime)
- Search Engine Container (Elasticsearch / OpenSearch)
- Data Access Layer / Persistence Container (PostgreSQL)
- Asynchronous Message Broker Container (RabbitMQ / Kafka)
- Background Workers Container (Background Worker Runtime)
- Configuration & Secrets Management Container (HashiCorp Vault)
- Centralized Observability Container (Observability Platform)
- External Identity Providers (SSO/OAuth), Payment Gateways, External Archival/Reporting System

## Relationships
- Client-Side SPA/Mobile Container interacts with API Gateway Container via HTTPS/REST/GraphQL
- API Gateway Container routes requests to Core Business Logic / Circulation API Container via gRPC/REST
- Core Business Logic / Circulation API Container queries Search Engine Container via HTTP/REST
- Core Business Logic / Circulation API Container persists data in Data Access Layer / Persistence Container via PostgreSQL Protocol
- Core Business Logic / Circulation API Container publishes/consumes events with Asynchronous Message Broker Container via AMQP/Kafka Protocol
- Background Workers Container processes tasks from Asynchronous Message Broker Container via AMQP/Kafka Protocol
- Dependent containers retrieve configurations and secrets from Configuration & Secrets Management Container via Vault API/Sidecar Agents
- Dependent containers forward audit logs and telemetry to Centralized Observability Container via OpenTelemetry/Syslog

## Technology Stack
- HashiCorp Vault: Deployed strictly within EU infrastructure for secure configuration and dynamic secret generation
- PostgreSQL: Relational persistence accessed via dynamic, short-lived database credentials
- JSON Schema / Pydantic: Validates configuration payloads during container pre-flight checks
- Centralized Observability Platform: Collects immutable, structured audit logs and runtime telemetry

## Rationale
This architecture secures sensitive credentials and enforces compliance through EU-restricted data residency and dynamic secret generation. Decoupled secret injection and schema validation ensure system stability and high performance.