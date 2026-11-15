## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It is deployed exclusively within EU cloud regions to strictly satisfy data residency constraints.

## Key Elements
- Web Frontend (React, Nginx)
- API Gateway (Kong, Spring Cloud Gateway)
- Core Catalog Service (Spring Boot, PostgreSQL)
- Circulation & Search Service (FastAPI, Elasticsearch)
- Worker Service (Celery, RabbitMQ)
- External Identity Provider (IdP)
- EU-Compliant Payment Gateway & Third-Party Notification Service

## Relationships
- Web Frontend to API Gateway via HTTPS/REST
- API Gateway to internal services via gRPC over Istio service mesh (mTLS)
- API Gateway to External IdP via OAuth2/OIDC JWT validation
- Worker Service to EU-Compliant Payment Gateway and Third-Party Notification Service via HTTPS
- Circulation & Search Service to Elasticsearch via TCP

## Technology Stack
- Kubernetes (EKS/AKS/GKE): Container orchestration with ArgoCD GitOps and EU-only node affinity
- Istio Service Mesh: Zero-trust networking, mTLS, circuit breaking, and traffic management
- PostgreSQL & Elasticsearch: Operational data storage with EU-hosted encryption-at-rest (CMK)
- OpenTelemetry & Prometheus: Distributed tracing and latency metrics monitoring

## Rationale
Container isolation with FastAPI and Elasticsearch guarantees the 99th-percentile search response time remains under 800ms. Strict EU-region deployment and zero-trust mTLS ensure compliance with data residency and security mandates.