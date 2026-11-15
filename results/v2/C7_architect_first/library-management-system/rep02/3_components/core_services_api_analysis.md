## Overview
- The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries while adhering to EU-only data residency.
- The Core Services API utilizes Node.js and NestJS with modular architecture to deliver robust performance, security, and integration capabilities.

## Key Elements
- **Catalogue Management Component**: NestJS module for physical and digital item CRUD operations.
- **Circulation & RBAC Component**: NestJS module enforcing role-based access control and loan logic.
- **Search Integration Component**: NestJS module interfacing with Elasticsearch or OpenSearch.
- **Integration Facade Component**: NestJS module managing outbound calls to payment, DRM, and notification services.
- **Event Emitter Module**: Internal NestJS asynchronous event dispatcher for transaction decoupling.
- **Relational Database**: PostgreSQL for persistent transactional storage with SSL/TLS encryption.
- **Search Engine**: Elasticsearch or OpenSearch for catalog queries.
- **Async Worker**: Python/Celery and Redis for background task processing.

## Relationships
- **API Gateway -> Core Services API**: Routes requests via gRPC with mTLS.
- **Core Services API -> Relational Database**: Reads and writes transactional data via TCP using the PostgreSQL protocol.
- **Core Services API -> Search Engine**: Performs catalog queries via HTTP/REST.
- **Core Services API -> Async Worker**: Queues background tasks via Redis.
- **Core Services API -> External Payment Gateway**: Processes fines via HTTPS/REST.
- **Core Services API -> DRM Provider**: Fetches digital assets via HTTPS/REST.
- **Core Services API -> Notification Service**: Sends automated alerts via HTTPS/REST.

## Technology Stack
- **Node.js with NestJS**: Chosen for modular architecture and component-level decomposition.
- **PostgreSQL**: Selected for ACID-compliant transactional data storage with SSL/TLS.
- **Elasticsearch / OpenSearch**: Deployed to ensure 99th-percentile search response under 800 ms.
- **Redis & Python/Celery**: Utilized for reliable asynchronous background task processing and event queuing.
- **HashiCorp Vault**: Implemented for secure secrets and credential management with auto-rotation.
- **OpenTelemetry**: Integrated for distributed tracing and observability.

## Rationale
- This modular NestJS architecture isolates domain logic, protects database health via search offloading, and ensures sub-800ms search responses.
- Strict security controls, data residency compliance, and integration bulkheads guarantee high availability and GDPR alignment for patron operations.