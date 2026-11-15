## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals with strict EU data residency enforcement.

## Key Elements
- Library Patrons & Staff, Library Administrators
- Web Application Frontend (React/TypeScript)
- Mobile API Gateway (Node.js/Express)
- Search Aggregator (Node.js/GraphQL)
- Core Circulation & Catalog Service (Java/Spring Boot)
- Integration Service (Python/Celery)
- Authentication & Session Service
- Asynchronous Notification Worker (Python)
- PostgreSQL Database Cluster and Redis Cache Tier
- Elasticsearch / OpenSearch Cluster
- External Payment Gateways, OverDrive, JSTOR, Institutional SSO Providers

## Relationships
- Patrons and Staff interact with Web Application Frontend and Mobile API Gateway via HTTPS/REST and WebSockets
- API Gateway communicates with Search Aggregator and Core Circulation Service via gRPC over TLS
- Internal microservices communicate via gRPC over TLS with mutual TLS (mTLS) enforcement
- Integration Service synchronizes with OverDrive, JSTOR, and External Payment Gateways via webhooks and outbound egress filtering
- Core services query PostgreSQL Database Cluster, Redis Cache, and Elasticsearch / OpenSearch Cluster

## Technology Stack
- React/TypeScript for the Web Application Frontend
- Node.js/Express for the Mobile API Gateway
- Node.js/GraphQL for the Search Aggregator
- Java/Spring Boot for the Core Circulation & Catalog Service
- Python/Celery for the Integration Service and Asynchronous Notification Workers
- PostgreSQL and Redis for stateful transactional data and caching within EU cloud regions
- Elasticsearch / OpenSearch for high-performance catalog indexing
- Kubernetes with NetworkPolicies, Horizontal Pod Autoscalers, and OpenTelemetry sidecars
- Terraform for GitOps-driven infrastructure provisioning

## Rationale
This architecture uses dedicated container tiers like the Search Aggregator and Elasticsearch to meet the sub-800ms search latency requirement while isolating transactional workflows. Strict network segmentation, regional pinning, and EU-localized stateful services ensure full compliance with European data residency constraints.