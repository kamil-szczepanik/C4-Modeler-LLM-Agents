## Overview
[System: Library Management System]
[Core Purpose: Catalogue items, manage circulation, and provide self-service portals with strict EU data residency.]

## Key Elements
- HashiCorp Vault (Secrets Management)
- Integrated Raft Storage Backend
- Core/HTTP API Layer
- Vault Agent Sidecar (Component)
- Circulation Service, Integration Service, Next.js Patron Portal, React Librarian Dashboard
- PostgreSQL Database with Read Replicas
- Elasticsearch/OpenSearch (Search & Catalogue)
- Kong/Envoy API Gateway

## Relationships
- Circulation/Integration Services communicate with Vault Agent Sidecar via HTTP over Unix Domain Sockets / localhost TCP
- Vault Agent Sidecar communicates with Core/HTTP API Layer via HTTPS (REST) over mTLS (Port 8200)
- Core/HTTP API Layer persists encrypted data to Integrated Raft Storage Backend using Raft internal RPC over TLS
- API Gateway routes external traffic to Patron/Librarian frontends and backend services

## Technology Stack
- HashiCorp Vault with Integrated Raft: High availability, zero external data residency leaks
- Vault Agent Sidecar: Client-side caching and transit security
- PostgreSQL & Elasticsearch: Core persistence and sub-800ms search performance
- Kubernetes & Helm: Deployment and orchestration
- TLS 1.3 & mTLS: Transit security and encryption

## Rationale
[This architecture satisfies EU data residency constraints through localized Raft storage and regional Cloud KMS auto-unseal mechanisms.]
[Vault Agent sidecars and Database Secrets Engines ensure sub-second patron checkouts, high availability (99.99%), and dynamic credential security without operational friction.]