## Overview
The Library Management System provides cataloging, circulation, and self-service portals for libraries, featuring an EU-hosted Elasticsearch container. This internal component architecture ensures sub-800ms search responses while maintaining strict EU data residency.

## Key Elements
- Search REST API Endpoint (HTTP/REST)
- Query Parsing & Analysis Engine (In-Process)
- Distributed Index & Shard Manager (In-Process)
- Caches & Segment Buffer (In-Memory)
- Cluster Coordination & Replication Manager (TCP)
- Node Transport Layer (Elasticsearch Transport Protocol)
- Lucene Storage Engine (Low-level indexing)

## Relationships
- Search Service -> Search REST API Endpoint (HTTP/JSON)
- Search REST API Endpoint -> Query Parsing & Analysis Engine (In-Process)
- Query Parsing & Analysis Engine -> Caches & Segment Buffer (In-Process)
- Query Parsing & Analysis Engine -> Distributed Index & Shard Manager (In-Process)
- Distributed Index & Shard Manager -> Node Transport Layer (TCP)
- Distributed Index & Shard Manager <-> Cluster Coordination & Replication Manager (TCP)
- Caches & Segment Buffer & Distributed Index & Shard Manager -> Lucene Storage Engine (In-Process/JNI)
- Lucene Storage Engine -> Search REST API Endpoint (In-Process)

## Technology Stack
- Elasticsearch: Core search container providing distributed full-text indexing
- Apache Lucene: Low-level storage and segment-merging engine
- Java/Transport Protocols: Inter-node communication and cluster coordination

## Rationale
The component-level decomposition isolates query parsing, caching, and shard management to meet the 99th-percentile search SLA of under 800ms. Restricting node coordination and storage to EU boundaries strictly enforces the data residency constraint.