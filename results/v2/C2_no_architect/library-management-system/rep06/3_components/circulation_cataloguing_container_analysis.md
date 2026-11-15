## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The system enforces strict EU data residency and high-performance transactional capabilities.

## Key Elements
* Circulation & Cataloguing Container (Java Microservice)
* PostgreSQL Database (Primary/Read Replica)
* Apache Kafka / Redpanda Event Streaming Container
* API Gateway (Istio Service Mesh / Kubernetes Gateway)
* EU-hosted Identity Provider (IdP)
* Kubernetes Worker Nodes & Storage Volumes (EU-hosted)

## Relationships
* API Gateway -> Circulation & Cataloguing Container: Routes traffic [mTLS]
* Circulation & Cataloguing Container -> PostgreSQL Database (Primary/Read Replica): Writes/reads transactional data [SQL]
* Circulation & Cataloguing Container -> Kafka/Redpanda Event Streaming Container: Publishes audit and sync events [Kafka Protocol, Encryption-in-Transit, Payload Signing]
* EU-hosted IdP -> Circulation & Cataloguing Container: Issues authentication tokens [JWT, Cryptographic Claims Validation]

## Technology Stack
* Java Microservice: Implements business logic, Resilience4j circuit breakers, and HikariCP connection pooling
* PostgreSQL Database: Stores catalog and transactional data with column-level encryption for PII and EU-pinned storage volumes
* Apache Kafka / Redpanda: Handles asynchronous event streaming and Dead Letter Queues (DLQs)
* Istio Service Mesh: Enforces mTLS and traffic routing via Kubernetes Gateway
* Kubernetes: Manages horizontal pod autoscaling (HPA) and EU-only node/storage pinning

## Rationale
This architecture ensures < 800 ms response times and high availability via database read-replicas, connection pooling, and circuit breakers. Strict EU infrastructure pinning, column-level encryption, and RBAC satisfy GDPR and data residency requirements.