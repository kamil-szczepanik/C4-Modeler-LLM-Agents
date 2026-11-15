## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The system strictly enforces EU-only data residency while maintaining high-performance search capabilities.

## Key Elements
- Library Patrons, Librarians / Circulation Staff, Library Administrators
- Self-Service Portal
- API Gateway (OAuth2/OIDC, JWT)
- Search Container (Elasticsearch / OpenSearch)
- User Analytics & Feedback Container
- Centralized Logging & SIEM Service
- EU-localized HSM

## Relationships
- API Gateway -> Search Container: Routes search requests via mTLS (SPIFFE/SPIRE)
- Search Container -> Search Container: Receives data via asynchronous Change-Data-Capture (CDC) pipelines
- Search Container -> User Analytics & Feedback Container: Routes user telemetry via asynchronous Fluentbit sidecars
- Search Container -> Centralized Logging & SIEM Service: Pipes metrics and audit logs

## Technology Stack
- Elasticsearch / OpenSearch: Horizontally scalable search engine for low-latency search (<800 ms R-05 requirement)
- Kubernetes: Multi-AZ node deployment with HPA and dedicated master/coordinator nodes
- LUKS: Encrypted persistent volumes for index data to meet EU data residency mandates
- Fluentbit: Asynchronous sidecars for telemetry routing without impacting disk I/O

## Rationale
This architecture ensures strict EU data residency compliance while delivering sub-800ms search latency for catalog discovery. Resource governance, mTLS, and document-level access controls protect system stability and data security.