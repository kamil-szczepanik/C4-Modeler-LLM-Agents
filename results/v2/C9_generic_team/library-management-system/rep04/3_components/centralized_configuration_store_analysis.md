## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It utilizes a centralized configuration store to maintain immutable image builds and enforce EU-only data residency.

## Key Elements
* Centralized Configuration Store: Consul / Spring Cloud Config
* Client Containers: Catalog Management, Circulation, User Portals (Spring Boot)
* Secret Management: Vault
* Monitoring and Telemetry: OTel Collector

## Relationships
* Client Containers fetch configurations from Centralized Configuration Store via TLS 1.3 with circuit breaking
* Centralized Configuration Store integrates with Vault for encrypted secret management
* OTel Collector monitors configuration health and triggers automated rollbacks on error spikes

## Technology Stack
* Consul / Spring Cloud Config: Centralizes configuration management and ensures immutable image builds
* Vault: Secures and encrypts sensitive credentials at rest and in transit
* TLS 1.3: Enforces secure encryption boundary for configuration transit

## Rationale
This architecture ensures strict EU-only data residency while maintaining high performance, system stability, and compliance. Immutable releases and automated rollbacks prevent runtime drift and protect availability.