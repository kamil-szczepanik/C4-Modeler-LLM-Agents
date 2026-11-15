## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The system enforces strict EU-only data residency while maintaining a 99th-percentile search response time under 800 ms.

## Key Elements
- **Library Patrons & Librarians**: End-users accessing discovery and catalog management.
- **Search API Handler**: Java/Spring MVC component exposing REST endpoints with built-in RBAC, input sanitization, and query analytics.
- **Indexing Service**: Java component consuming catalog updates from the message broker to synchronize search indices.
- **Elasticsearch Cluster**: Core distributed data store providing multi-lingual, fuzzy search and inverted index capabilities.
- **Message Broker**: Apache Kafka distributing asynchronous catalog update and analytics events.
- **Audit Container**: Go container receiving security and authentication telemetry.

## Relationships
- **Core Services Container -> Search API Handler**: Queries item and catalog data via HTTP/JSON over mTLS (TLS 1.3).
- **Message Broker -> Indexing Service**: Feeds catalog update events using the Kafka Consumer Protocol.
- **Search API Handler -> Message Broker**: Dispatches asynchronous zero-result search analytics events.
- **Search API Handler -> Audit Container**: Forwards failed authentication and unauthorized query attempts.

## Technology Stack
- **Search Engine**: Elasticsearch cluster configured with ICU and Lucene standard analyzers for multi-lingual and fuzzy search, deployed across a minimum 3-node master-eligible topology in EU regions.
- **API & Components**: Java with Spring MVC for the Search API Handler and Indexing Service.
- **Transport & Security**: TLS 1.3 for internal node-to-node and client connections; Vault for secret management.
- **Telemetry**: Prometheus for JVM metrics and OpenTelemetry for request tracing.

## Rationale
The architecture decouples asynchronous indexing and analytics from read queries via Apache Kafka, protecting read latency to satisfy the sub-800ms search SLA (R-05). Strict EU-resident deployment, TLS 1.3 encryption, and robust RBAC fulfill data residency constraints and enterprise security requirements.