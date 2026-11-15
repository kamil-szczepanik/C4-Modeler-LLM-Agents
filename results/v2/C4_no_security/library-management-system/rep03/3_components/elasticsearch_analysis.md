## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It features an Elasticsearch component designed to deliver sub-800ms search responses while maintaining strict EU-only data residency.

## Key Elements
- Library Patrons (Members)
- Librarians
- Library Administrators
- Catalogue & Search Container
- REST API / Transport Layer (Java/Netty)
- Query & Search Engine (Lucene Core)
- Index & Shard Manager
- Data Storage & Translog Engine
- Cluster Coordination & Discovery Module

## Relationships
- Catalogue & Search Container -> REST API / Transport Layer: Sends JSON search queries and bulk indexing payloads [HTTP/TCP]
- REST API / Transport Layer -> Query & Search Engine: Passes parsed queries for execution
- Query & Search Engine -> Index & Shard Manager: Resolves targeted shards
- REST API / Transport Layer -> Index & Shard Manager: Routes document indexing requests to appropriate shards
- Index & Shard Manager -> Data Storage & Translog Engine: Writes segments and translogs to local NVMe storage
- Index & Shard Manager <-> Cluster Coordination & Discovery Module: Synchronizes cluster topology and shard allocation

## Technology Stack
- Elasticsearch: Distributed search engine providing full-text search and sub-800ms latencies (NFR R-05)
- Java/Netty: Powers the REST API and transport layer for high-throughput request handling
- Lucene Core: Executes aggregations, relevancy scoring, and faceted search for catalogue items (R-01)
- ECK (Elastic Cloud on Kubernetes): Orchestrates the stateful cluster across EU availability zones
- NVMe Storage & S3-compatible Object Storage: Provides high-throughput local disk I/O and encrypted EU-region backups

## Rationale
This architecture isolates ingestion, query execution, and cluster state management to handle high concurrent search loads. Pinning all shards, nodes, and backups strictly within EU borders satisfies regulatory data residency constraints.