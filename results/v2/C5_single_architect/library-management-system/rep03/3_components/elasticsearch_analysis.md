## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It utilizes an Elasticsearch component architecture to ensure high-speed search performance with EU-only data residency.

## Key Elements
- **Query DSL Engine**: Processes incoming search queries using Elasticsearch Query DSL.
- **Indexing & Lucene Core**: Manages inverted indices and document storage using Apache Lucene.
- **Cluster Coordination Module**: Handles node discovery, shard allocation, and cluster state using Elasticsearch Zen Discovery/Raft.
- **Document Routing & Shard Manager**: Directs operations to appropriate shards using the Elasticsearch Routing Module.

## Relationships
- **Catalogue Service -> Query DSL Engine**: Executes search and index requests via REST / HTTP, JSON over TCP.
- **Query DSL Engine -> Document Routing & Shard Manager**: Resolves shard locations via Internal JVM Method.
- **Document Routing & Shard Manager -> Indexing & Lucene Core**: Executes segment-level operations via Apache Lucene API.

## Technology Stack
- **Elasticsearch**: Core search engine for delivering high-speed search capabilities.
- **Apache Lucene**: Low-level core for inverted indices and document storage.
- **Elasticsearch Routing Module**: Handles document routing and shard management for distributed queries.

## Rationale
This component architecture separates query processing, routing, and index management to achieve the <800ms P99 search response requirement. Localized shard allocation explicitly supports the EU-only data residency constraint.