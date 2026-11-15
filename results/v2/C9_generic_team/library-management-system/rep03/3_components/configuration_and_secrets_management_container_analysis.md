## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within an EU data residency boundary. The architecture uses a Configuration and Secrets Management Container to handle dynamic runtime injection, security, and performance requirements.

## Key Elements
* Configuration and Secrets Management Container (Dynamic Runtime Injection)
* Library Users and Administrators
* External Identity Providers
* Third-Party Hardware Interfaces
* High-Volume Publisher Feeds
* Inter-Library Loan Networks
* Notification and Communication Gateways
* EU-Hosted Observability Infrastructure
* Archival and Backup Storage Service
* Client-Side Application Container (Single Page App / Mobile App)
* API Gateway Container (Reverse Proxy / API Gateway)
* Core Catalog/Circulation Service Container (Microservice)
* Search Engine Container (Dedicated Indexing Engine)
* Caching Container (Redis)
* Message Broker Container (Message Broker)
* Background Worker Container (Background Worker)
* Telemetry Sidecar/Agent Container (Sidecar Agent)

## Relationships
* Client-Side Application Container interacts with API Gateway Container via HTTPS/REST
* API Gateway Container communicates with Core Catalog/Circulation Service Container via gRPC
* Core Catalog/Circulation Service Container queries Search Engine Container via gRPC
* Core Catalog/Circulation Service Container utilizes Caching Container via Redis Protocol
* Dependent containers fetch runtime configurations from Configuration and Secrets Management Container via HTTPS with `X-Config-Version` headers
* Telemetry Sidecar/Agent Container reports metrics and audit logs to EU-Hosted Observability Infrastructure via OTLP/HTTPS

## Technology Stack
* Redis: Used for local caching and fallback mechanisms to maintain high availability and performance (< 800 ms search response)
* HTTPS/TLS 1.3: Enforced for secure, encrypted data transmission in transit adhering to EU data residency
* Standardized Configuration Provider Interface (Adapter Pattern): Decouples application code from the underlying secrets backend
* OTLP/HTTPS: Protocol for transmitting audit reports and telemetry to the EU-Hosted Observability Infrastructure

## Rationale
This architecture ensures strict compliance with EU-only data residency constraints through localized storage and transmission controls. Additionally, implementing immutable configuration versioning, startup schema validation, and local fallback caching protects search performance targets (< 800 ms 99th-percentile) against transient latency.