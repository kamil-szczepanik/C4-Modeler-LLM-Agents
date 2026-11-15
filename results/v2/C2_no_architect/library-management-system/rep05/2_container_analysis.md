## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for public and academic libraries. It ensures strict EU-only data residency and high-performance search capabilities.

## Key Elements
* Library Patrons, Librarians, and Library Administrators
* API Gateway
* Self-Service Portal Container
* Circulation Management Container
* Analytics/Reporting Container
* Catalogue Database and Read-Replica Data Store
* External Institutional BI Tools and Municipal Dashboards
* Message Broker (Kafka / RabbitMQ)

## Relationships
* Patrons and Staff interact with the API Gateway via HTTPS using OAuth2/OIDC with short-lived JWTs
* Inter-container communication uses mTLS via Istio service mesh
* Core containers query the Catalogue Database and read-replica store via TLS 1.3
* Core containers publish events asynchronously to the Message Broker for the Analytics Container
* Analytics Container provides aggregated data to Library Administrators

## Technology Stack
* Kubernetes: EU-region-only managed clusters for data residency compliance
* Istio: Service mesh for mTLS and trust boundaries
* OAuth2/OIDC & JWT: Authentication and RBAC at the API Gateway
* OpenTelemetry: Distributed tracing to maintain <800ms search latency
* Kafka / RabbitMQ: Asynchronous event ingestion for analytics
* AES-256 & TLS 1.3: Data encryption at rest and in transit

## Rationale
This architecture enforces EU data residency through regional deployments and strict egress controls. It guarantees sub-800ms search performance via independent stateless services, read-replicas, and asynchronous telemetry.