## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It utilizes a read-optimized search index to guarantee high-performance discovery.

## Key Elements
- Library Patrons (Members) & Library Librarians / Staff
- API Gateway (Kubernetes, OAuth2/OIDC, mTLS)
- Read-optimized Search Index (Elasticsearch, EU-hosted)
- Core Circulation and Transactional Database (Kubernetes, EU-region clusters)

## Relationships
- API Gateway -> Read-optimized Search Index: Routes search requests with query-time JWT filtering [mTLS, TLS 1.3]
- Core Circulation Database -> Read-optimized Search Index: Streams updates via Change Data Capture pipeline [Debezium, TLS 1.3]

## Technology Stack
- Elasticsearch: Read-optimized search engine chosen for sub-800ms performance and faceted search capabilities
- Debezium: Change Data Capture tool for near-real-time data synchronization preventing phantom availability
- Kubernetes: Container orchestration platform for resource isolation, operator management, and scaling
- Prometheus/Grafana: Observability stack for tracking JVM heap and query latency SLAs
- Vault / Kubernetes Secrets: Secret management for TLS certificates and keystore passwords

## Rationale
This architecture guarantees strict EU data residency compliance while meeting the stringent non-functional performance requirement of 99th-percentile search response under 800 ms. Security controls, CDC pipelines, and resource isolation ensure both data integrity and high availability during academic traffic surges.