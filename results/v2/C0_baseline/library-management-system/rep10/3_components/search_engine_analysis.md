## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU data residency constraints. The Search Engine container delivers sub-800ms search latency using a secure, multi-lingual, and scalable architecture.

## Key Elements
- **Query Parser & Router (Java/Spring):** Translates REST queries, enforces RBAC, Document-Level Security (DLS), OAuth2/JWT validation, and query sanitization.
- **Index Management Service (Java):** Handles bulk indexing, schema updates, zero-downtime index aliasing, and Synonym/Linguistic Analysis pipelines.
- **Search Storage Node (Managed OpenSearch Cluster, EU-hosted):** Core index store with AES-256 encryption at rest and automated EU-only geo-redundant snapshots.
- **Patron Web App & API / Staff Management API:** Upstream clients querying the search engine.
- **Integration/Messaging Container (Managed Apache Kafka):** Streams catalogue updates.
- **Observability Platform & SIEM:** Receives scrubbed query logs, audit trails, and performance metrics.

## Relationships
- Patron Web App & API / Staff Management API -> Query Parser & Router: Queries catalogue [HTTPS/REST with mTLS and OAuth2/JWT]
- Integration/Messaging Container -> Index Management Service: Consumes catalogue update events [Kafka Protocol]
- Query Parser & Router -> Search Storage Node: Executes search DSL [Transport Protocol over TLS 1.3]
- Search Engine Containers -> Observability Platform & SIEM: Forwards audit logs and slow-query metrics [HTTPS/Syslog]

## Technology Stack
- **Managed OpenSearch/Elasticsearch:** Provides sub-800ms search performance (R-05), sharding, and auto-scaling.
- **Java/Spring Boot:** Powers internal routing, security enforcement, and index management services.
- **Apache Kafka:** Asynchronously decouples catalogue updates to ensure search availability.
- **TLS 1.3 & AES-256:** Secures internal cluster traffic and enforces encryption-at-rest.

## Rationale
This architecture uses managed, EU-hosted components to strictly enforce GDPR and data residency constraints while meeting the rigorous sub-800ms search performance requirement. Asynchronous ingestion, robust security controls, and multi-lingual analysis pipelines ensure scalability, patron privacy, and advanced staff workflows.