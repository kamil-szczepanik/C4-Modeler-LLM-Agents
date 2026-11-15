## Overview
The system is a Library Management System designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It uses Elasticsearch to deliver high-performance, multi-lingual, faceted search capabilities.

## Key Elements
- **Library Management System**: Core software solution.
- **Catalog & Search Service**: Java/Spring Boot service handling item discovery.
- **Elasticsearch Container**: High-performance indexing database.
- **Routing & Coordination Component**: Handles incoming query distribution and aggregation.
- **Search & Query Execution Component**: Executes full-text and faceted search queries.
- **Indexing & Lucene Storage Component**: Manages inverted indices and Lucene storage.
- **Analysis & Tokenization Component**: Handles text normalization, stemming, and diacritic filtering.

## Relationships
- `Catalog & Search Service` -> `Routing & Coordination Component`: HTTP/REST or Transport Client [TCP]
- `Routing & Coordination Component` -> `Analysis & Tokenization Component`: Internal In-Memory Pipeline [Java API]
- `Analysis & Tokenization Component` -> `Indexing & Lucene Storage Component`: Lucene Document Ingestion [In-Memory]
- `Routing & Coordination Component` -> `Search & Query Execution Component` & `Indexing & Lucene Storage Component`: Inter-node Transport Protocol [TCP/9300]

## Technology Stack
- **Elasticsearch**: Chosen for sub-second, typo-tolerant search and advanced faceting.
- **Kubernetes StatefulSets**: Deployed with persistent local NVMe storage to prevent I/O bottlenecks.
- **Prometheus Exporters**: Used for monitoring JVM garbage collection pauses and thread pool rejections.
- **EU-central S3-compatible Object Storage**: Used for restricted cross-region snapshot backups.

## Rationale
This architecture ensures 99th-percentile search responses remain under 800 ms through internal component decoupling and strict JVM/storage resource hardening. It strictly adheres to EU data residency mandates via region-locked deployments and storage configurations.