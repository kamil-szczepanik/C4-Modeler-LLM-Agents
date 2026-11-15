## Overview
This architecture defines the internal component structure of the OpenSearch Service container for the Online Bookstore e-commerce platform. It provides scalable, secure, and sub-second catalog search capabilities across multiple AWS regions.

## Key Elements
* Search API Handler (Java/Lucene-native REST layer)
* Security & Access Control Component (IAM/RBAC middleware)
* Query Parser & DSL Engine (JSON-to-Lucene query tree translator)
* Indexing & Sharding Manager (Document routing and distributed shard allocator)
* Cluster State Coordinator (OpenSearch Cluster Manager node role)
* Data Nodes (Apache Lucene Indices)

## Relationships
* Catalog Service -> Search API Handler: HTTP/REST (JSON) over TLS 1.3
* Search API Handler -> Security & Access Control Component: In-memory middleware hook
* Security & Access Control Component -> Query Parser & DSL Engine: In-memory invocation
* Query Parser & DSL Engine -> Data Nodes: Apache Lucene Java API
* Cluster State Coordinator -> Data Nodes: Transport Protocol (TCP/Custom)
* Indexing & Sharding Manager -> Data Nodes: Transport Protocol (TCP/Custom)

## Technology Stack
* Amazon OpenSearch Service: Managed search platform providing automated scaling and infrastructure abstraction
* Apache Lucene: Core indexing and search engine technology powering data nodes
* Java: Native runtime for Search API and Lucene integration
* HTTPS / TLS 1.3: Encrypted transport protocol for external container communication

## Rationale
This component decomposition ensures sub-second catalog search performance to meet strict performance requirements. Furthermore, distributed sharding and cluster coordination guarantee high availability and scalability across multiple AWS regions.