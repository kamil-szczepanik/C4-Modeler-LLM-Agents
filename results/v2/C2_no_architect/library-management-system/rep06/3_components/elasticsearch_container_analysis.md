## Overview
[The system is a Library Management System providing cataloguing, circulation, and self-service portals for public and academic libraries. Its core purpose is to deliver high-performance search and inventory management while strictly enforcing EU data residency constraints.]

## Key Elements
* Library Patrons
* Librarians and Circulation Staff
* Library Administrators
* Patron Portal (Web Frontend / Backend Service)
* Circulation & Cataloguing Container (Java / Microservice)
* Elasticsearch Container (Elasticsearch 3-node cluster)
* Audit & Event Tracking Container (Microservice)
* EU-hosted Identity Provider (IdP)
* EU-localized S3-compatible Object Storage

## Relationships
* Patron Portal -> Elasticsearch Container: Queries search data using CQRS [REST/TCP via Istio mTLS]
* Elasticsearch Container -> Audit & Event Tracking Container: Streams security audit logs [REST/TCP]
* Elasticsearch Container -> EU-localized S3-compatible Object Storage: Stores automated snapshots [HTTPS]

## Technology Stack
* Elasticsearch: Provides sub-second search performance and index lifecycle management (ILM) to meet R-05 (<800ms search latency).
* Kubernetes: Manages container orchestration with node selectors, taint tolerations, and resource governance (JVM heap set to 50% of container RAM).
* Istio Service Mesh: Enforces mutual TLS (mTLS) for all container-to-container traffic.
* HashiCorp Vault: Manages automated secret rotation and internal certificates.
* Prometheus: Tracks JVM heap usage, cluster health, and search latency percentiles.

## Rationale
[This architecture satisfies the sub-second search performance requirement (R-05) by utilizing a dedicated, scalable Elasticsearch cluster isolated from the primary operational database. It rigorously adheres to the EU-only data residency constraint through localized persistent volumes, region-specific S3 backups, and strict RBAC/ABAC data controls.]