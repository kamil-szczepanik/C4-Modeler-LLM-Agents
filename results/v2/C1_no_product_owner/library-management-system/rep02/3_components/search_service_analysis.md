## Overview
The Library Management System provides a cataloging, circulation, and self-service portal for public and academic libraries. Its Search Service component delivers high-performance item discovery while adhering to strict EU data residency constraints.

## Key Elements
* Search Service (Java / Spring Boot): Core container housing search logic.
* Search Controller: Exposes gRPC endpoints using Spring gRPC.
* Query Parser & Validator: Sanitizes inputs via Apache Lucene Query Parser.
* Index Synchronizer: Consumes domain events using Spring Kafka.
* Search Client: Executes queries using OpenSearch Java Client with Resilience4j.
* Reindexing Worker: Handles batch reindexing using Spring Batch.
* Telemetry Interceptor: Collects metrics via Micrometer and OpenTelemetry.
* Search Index: Managed OpenSearch cluster (AWS OpenSearch Service EU-hosted).
* Managed Event Bus (Kafka / EventBridge) and PostgreSQL Database.

## Relationships
* API Gateway -> Search Controller [gRPC over mTLS]
* Index Synchronizer <- Managed Event Bus [Kafka]
* Search Client -> Search Index [REST over HTTPS, mTLS, AWS SigV4]
* Reindexing Worker -> Search Index [REST over HTTPS Bulk API]
* Search Controller -> Query Parser & Validator -> Search Client [In-process]

## Technology Stack
* Java / Spring Boot: Core runtime for memory efficiency and enterprise maturity.
* AWS OpenSearch Service (EU-hosted): Delivers scalable search indexing within EU boundaries.
* Apache Lucene: Provides robust query parsing and validation.
* Spring Kafka: Enables real-time index synchronization.
* Spring Batch: Manages zero-downtime bulk reindexing pipelines.
* Resilience4j: Prevents cascading failures via circuit breakers.
* OpenTelemetry / Micrometer: Ensures observability for latency SLAs.

## Rationale
This architecture uses decoupled asynchronous event ingestion and isolated batch workers to protect real-time query performance, consistently meeting the <800ms 99th-percentile search latency requirement. Strict mTLS, IAM separation, and EU-hosted OpenSearch enforce compliance with EU data residency regulations.