## Overview
The Library Management System provides a solution for public and academic libraries to catalogue items, manage circulation, and offer self-service portals with strict EU-only data residency. The Search Service Container delivers fast, scalable search functionality ensuring 99th-percentile search responses under 800ms.

## Key Elements
* Search Service Container (Elasticsearch / OpenSearch)
* Message Broker Container (RabbitMQ / Kafka)
* Web App Container (Web Application Framework)
* Distributed Cache Container (Redis)
* Enterprise Logging and Monitoring Service
* EU-Hosted Backup and Archival Storage

## Relationships
* Message Broker Container -> Search Service Container: Consumes events for indexing [Asynchronous Message Stream]
* Web App Container -> Search Service Container: Serves search queries [HTTP]
* Search Service Container -> Distributed Cache Container: Caches frequent catalogue lookups [TCP]
* Search Service Container -> EU-Hosted Backup and Archival Storage: Stores automated index snapshots [HTTPS]

## Technology Stack
* Elasticsearch / OpenSearch: Chosen for fast, scalable search capabilities ensuring sub-800ms 99th-percentile response times.
* RabbitMQ / Kafka: Used for decoupled asynchronous event-driven ingestion to prevent database write bottlenecks.
* Redis: Implements result caching to offload the search cluster and protect latency SLAs.
* JSON Schema / Protocol Buffers: Enforces strict schema validation at the ingestion boundary to prevent payload corruption.

## Rationale
This architecture decouples heavy write ingestion from user-facing queries using asynchronous messaging and read/write segregation, ensuring high availability and performance. Strict EU data residency constraints and disaster recovery procedures are enforced through isolated backups and automated compliance tooling.