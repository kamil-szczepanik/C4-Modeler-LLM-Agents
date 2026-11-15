## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It is engineered with strict EU-only data residency and high-performance search capabilities.

## Key Elements
- **Users**: Library Staff, Library Patrons
- **Frontend**: Web Application (React, TypeScript) hosted via CDN
- **Ingress/Security**: API Gateway (Spring Cloud Gateway / Envoy) with OAuth2/OIDC JWT validation
- **Services**: Core Domain Service (Java / Spring Boot), Search Service (Java / Elasticsearch / OpenSearch), Notification Service (Node.js / TypeScript)
- **Data & Events**: PostgreSQL Database, Managed Event Bus (Kafka/EventBridge), Search Index
- **Infrastructure**: Kubernetes (EKS/AKS EU-equivalent), Istio/Linkerd service mesh, HashiCorp Vault

## Relationships
- **Frontend to API Gateway**: HTTPS/REST
- **Internal Service-to-Service**: gRPC over mTLS
- **Event Streaming**: TLS-encrypted TCP with SASL/OAuth2 authentication via Managed Event Bus
- **Database Synchronization**: Change Data Capture (Debezium) from PostgreSQL to Search Index

## Technology Stack
- **Frontend**: React & TypeScript for responsive client-side portals
- **Backend**: Java / Spring Boot for core business and search services; Node.js / TypeScript for asynchronous notifications
- **Data Store**: PostgreSQL with AES-256 encryption-at-rest for transactional data
- **Search**: Elasticsearch / OpenSearch to satisfy <800ms 99th-percentile search latency
- **Infrastructure & Mesh**: Kubernetes, Istio/Linkerd for mTLS, ArgoCD for GitOps deployment

## Rationale
This container architecture isolates performance-heavy search queries from transactional workloads while guaranteeing sub-800ms response times. Zero-trust mTLS, GitOps, and managed EU cloud infrastructure strictly enforce the mandated EU-only data residency and security requirements.