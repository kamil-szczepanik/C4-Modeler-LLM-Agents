## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It is engineered with strict EU-only data residency and high-performance search SLAs.

## Key Elements
* Library Users and Administrators
* Client-Side Application Container (Single Page App / Mobile App)
* API Gateway Container
* Core Catalog/Circulation Service Container
* Search Engine Container (dedicated indexing)
* Caching Container (Redis)
* Message Broker Container
* Background Worker Container
* Configuration and Secrets Management Container
* Telemetry Sidecar/Agent Container
* External Identity Providers, Third-Party Hardware Interfaces, High-Volume Publisher Feeds, Inter-Library Loan Networks, Notification Gateways, EU-Hosted Observability Infrastructure, and Archival/Backup Storage Service

## Relationships
* Client-Side Application connects to API Gateway via HTTPS/TLS termination.
* API Gateway routes synchronous internal calls to Core Catalog and Search Engine via HTTP/gRPC.
* Core Catalog and Search Engine interact with Caching Container (Redis) for read-heavy query optimization.
* Message Broker handles asynchronous event-driven workflows with publisher feeds and notification gateways.
* Background Worker processes asynchronous jobs independently from the Message Broker.
* Telemetry Sidecar exports sanitized operational metrics and logs exclusively to EU-Hosted Observability Infrastructure.

## Technology Stack
* Search Engine: Dedicated indexing container to ensure 99th-percentile search response < 800 ms (R-05).
* Caching Container: Redis to handle read-heavy library catalog browsing and reduce database load.
* Message Broker & Background Workers: Asynchronous event-driven components to decouple publisher ingestion loads.
* Configuration & Secrets Management: Dynamic runtime injection for database connection strings and keys.
* Observability: EU-Hosted Observability Infrastructure with localized PII sanitization.

## Rationale
This architecture guarantees strict EU-only data residency by isolating all persistent storage and telemetry pipelines within compliant EU infrastructure. Furthermore, decoupling read queries via Redis and write ingestion via a Message Broker ensures the system consistently meets the demanding <800ms search response SLA.