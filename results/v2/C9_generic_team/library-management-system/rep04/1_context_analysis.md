## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It ensures strict EU-only data residency and meets high-performance search requirements.

## Key Elements
* Library Management System (Core container boundary)
* API Gateway / Edge Service
* Identity Provider (IdP)
* Caching / Indexing Layer
* Notification / Messaging Service
* Monitoring and Telemetry Aggregator
* Disaster Recovery / Backup Target
* Data Migration and Integration Endpoints

## Relationships
* Client/User Agent to API Gateway via HTTPS/TLS
* API Gateway to Caching/Indexing Layer via internal gRPC/REST for search (<800ms p99)
* Core System to Identity Provider via OAuth2/OIDC for authentication
* Core System to Notification Service via asynchronous webhooks/HTTPS for patron alerts
* Core System to Monitoring Aggregator via localized syslog/OTLP for telemetry
* Core System to Backup Target via encrypted scheduled replication

## Technology Stack
* API Gateway: Reverse proxy for geo-routing and SSL termination
* Caching / Indexing Layer: In-memory/search indexing technology for p99 < 800ms performance
* Identity Provider: OAuth2/OIDC compliant service enforcing EU residency
* Monitoring: EU-hosted APM/telemetry sink preventing PII export
* Storage: EU-Central region-locked databases and backups

## Rationale
This architecture enforces EU data residency by explicitly bounding all external dependencies, IdPs, backups, and notification services within EU infrastructure. Asynchronous logging and a dedicated caching layer protect the p99 search latency target (<800ms).