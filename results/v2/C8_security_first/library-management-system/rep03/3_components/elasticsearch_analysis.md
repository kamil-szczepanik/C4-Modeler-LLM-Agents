## Overview
The system is an Elasticsearch search cluster within the Library Management System, providing high-performance catalogue discovery for patrons and librarians. It ensures sub-800ms search responses while maintaining strict EU-only data residency.

## Key Elements
* Routing and Coordination Node (Java / Netty): Handles client requests, query distribution, security filtering, and cluster-state management
* Data Nodes (Lucene Engine): Store index shards, doc-values, and execute distributed matching across EU availability zones
* Inverted Index & Analyzer Pipeline: Implements custom tokenizers, stemmers, fuzzy matching, and domain-specific synonyms
* Search Microservice: Java / Spring Boot application acting as the sole intermediary between API gateways and Elasticsearch

## Relationships
* Search Microservice -> Routing and Coordination Node: Issues search/indexing queries over REST / JSON over TLS 1.3
* Routing and Coordination Node -> Data Nodes: Distributes search/index operations over Transport Protocol over TLS 1.3 (mTLS)

## Technology Stack
* Elasticsearch Cluster: Deployed via ECK Kubernetes Operator using StatefulSets for automated orchestration and zero-downtime rolling upgrades
* Lucene Storage Engine: Utilizes region-pinned NVMe block storage and doc-values for out-of-core facet aggregation and high-performance persistence
* Security Controls: Enforces mTLS node-to-node communication, AES-256 encryption at rest with EU-stored CMK, and FLS/DLS for data governance

## Rationale
Decomposing Elasticsearch into isolated coordination and data nodes prevents JVM exhaustion and enforces strict security boundaries. Multi-AZ deployment and doc-values optimization guarantee the sub-800ms search SLA while strictly adhering to EU data residency mandates.