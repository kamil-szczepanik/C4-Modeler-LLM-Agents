## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It guarantees strict EU-only data residency while maintaining high-performance search capabilities.

## Key Elements
* Library Patrons (Members), Librarians, and Library Administrators
* Self-Service Web/Mobile Portal container
* API Gateway container
* Core Circulation and Transactional Database containers
* Read-optimized Search Index container (Elasticsearch)
* Admin/Reporting container
* Payment Gateway and Notification Service integration containers
* Inter-Library Loan (ILL) Partners external system

## Relationships
* Library Patrons and Staff interact with the Self-Service Portal and Admin containers via HTTPS (TLS 1.3).
* API Gateway routes traffic to backend containers using OAuth2/OIDC and enforces mTLS for container-to-container communication.
* Core containers query the EU-hosted Elasticsearch container for catalogue searches (R-01).
* External Payment Gateways and Notification Services integrate via egress boundary payload filtering.

## Technology Stack
* Kubernetes: EU-region clusters for strict data residency enforcement.
* Elasticsearch: EU-hosted read-optimized search index for <800ms search SLA (R-05).
* ArgoCD: GitOps pipeline for immutable container deployments.
* OpenTelemetry: Distributed tracing across API Gateway, Search, and Payment containers.
* TLS 1.3 & AES-256: Encryption standards for data in-transit and at rest.

## Rationale
This architecture decouples the patron search and reporting workloads from the core transactional database to consistently achieve the required 99th-percentile search response under 800ms. Furthermore, it strictly enforces EU-only data residency and security compliance through localized infrastructure, mTLS, and egress PII payload filtering.