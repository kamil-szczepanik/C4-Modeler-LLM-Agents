## Overview
The Catalogue & Search Service Container is a high-performance Java/Spring-based microservice within the Library Management System, designed to catalogue physical/digital items and provide sub-800ms search responses. It isolates read-heavy discovery from write-heavy cataloguing while strictly enforcing EU-only data residency.

## Key Elements
* **API Gateway / Ingress:** Traefik or Envoy handling external routing.
* **Patron BFF & Staff Workflow Containers:** Clients querying the catalogue.
* **Catalogue & Search Service Container:** Core container housing internal components.
* **gRPC API Handler (Java/Spring):** Exposes endpoints, parses JWT claims for RBAC, and handles input sanitization.
* **Search & Discovery Engine:** Elasticsearch client handling DSL queries, facets, typo tolerance, and relevance.
* **Cataloguing & Bulk Ingestion Worker (Java):** Processes write/update operations and schema validation.
* **Data Access Repository:** Interfaces with storage engines.
* **PostgreSQL:** Relational metadata persistence.
* **Elasticsearch Cluster:** Search index with AES-256 encryption at rest.

## Relationships
* Patron BFF & Staff Workflow -> gRPC API Handler: Queries catalogue and search [gRPC over mTLS]
* gRPC API Handler -> Search & Discovery Engine / Cataloguing Worker: In-process Java method calls
* Cataloguing & Bulk Ingestion Worker -> PostgreSQL: Relational metadata persistence [JDBC over TLS, TCP 5432]
* Search & Discovery Engine -> Elasticsearch Cluster: Search and indexing operations [Elasticsearch REST Client over TLS 1.3, TCP 9200]

## Technology Stack
* **Java / Spring Boot:** Provides robust API handling, dependency injection, and concurrency management for high-throughput workloads.
* **Elasticsearch:** Delivers <800ms search performance, faceted filtering, and relevance tuning.
* **PostgreSQL:** Ensures reliable, ACID-compliant relational metadata storage.
* **gRPC over mTLS:** Secures high-performance inter-service communication.
* **Kubernetes:** Orchestrates pods with HPA, automated secrets CSI, and strict resource quotas in EU clusters.

## Rationale
This architecture separates transactional metadata in PostgreSQL from search indices in Elasticsearch to meet the sub-800ms performance NFR under peak loads. Enforcing AES-256 encryption, TLS 1.3, and EU-only Kubernetes node placement guarantees compliance with EU data residency constraints.