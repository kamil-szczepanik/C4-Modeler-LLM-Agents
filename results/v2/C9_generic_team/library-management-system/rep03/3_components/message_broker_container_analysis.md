## Overview
The Library Management System provides cataloging, circulation, and self-service portals for academic and public libraries. It ensures strict EU-only data residency and high-performance search capabilities.

## Key Elements
- Library Users and Administrators
- Client-Side Application Container (Single Page App / Mobile App)
- API Gateway Container (Reverse Proxy / API Gateway)
- Core Catalog/Circulation Service Container (Microservice)
- Search Engine Container (Dedicated Indexing Engine)
- Caching Container (Redis)
- Message Broker Container (Message Broker)
- Background Worker Container (Background Worker)
- Configuration and Secrets Management Container
- Telemetry Sidecar/Agent Container
- External Identity Providers, Third-Party Hardware Interfaces, High-Volume Publisher Feeds, Inter-Library Loan Networks, Notification and Communication Gateways, EU-Hosted Observability Infrastructure, Archival and Backup Storage Service, Client Update and Distribution Channels, External Configuration and Feature Flag Management Service

## Relationships
- High-Volume Publisher Feeds -> Message Broker Container: Ingests digital catalog data asynchronously [Asynchronous Messaging]
- Message Broker Container -> Background Worker Container: Triggers asynchronous job processing [Message Queue]
- Message Broker Container -> Notification and Communication Gateways: Dispatches asynchronous notifications [Webhooks/SMTP]

## Technology Stack
- Message Broker Container: Manages event-driven workflows with Schema Registry (Avro/JSON Schema) validation, Dead Letter Queues (DLQs), and W3C Trace Context propagation.
- Redis: Powers caching to maintain 99th-percentile search responses below 800 ms.
- GitOps / Configuration-as-Code: Manages broker topologies, topics, ACLs, and retention policies declaratively.

## Rationale
This architecture uses asynchronous decoupling via a managed message broker to shield core services from traffic spikes while enforcing strict EU data residency constraints. Distributed tracing, payload offloading, and robust error-handling patterns ensure high availability and data integrity.