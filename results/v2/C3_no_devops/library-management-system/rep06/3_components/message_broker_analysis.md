## Overview
[Library Management System] provides public and academic libraries with item cataloging, circulation management, and self-service portals. The architecture prioritizes strict EU data residency and high performance.

## Key Elements
* Library Patrons & Circulation Staff
* Frontend Container (React/TypeScript SPA)
* API Gateway (Nginx/Kong)
* Catalogue & Search Service (Spring Boot/Java with Elasticsearch)
* Circulation & Member Service (Node.js/NestJS)
* Message Broker (Apache Kafka with Schema Registry and DLQ Manager)
* Databases (EU-hosted PostgreSQL with AES-256 encryption-at-rest)

## Relationships
* Frontend Container -> API Gateway: Routes client requests [HTTPS/REST]
* Circulation & Member Service -> Message Broker: Publishes domain events [mTLS, TCP/9092, OAuth2/OIDC]
* Notification Worker Container -> Message Broker: Consumes domain events [mTLS, TCP/9092]
* Analytics & Reporting Container -> Message Broker: Consumes historical events [mTLS, TCP/9092, OAuth2/OIDC]

## Technology Stack
* Apache Kafka: Selected for high-throughput, fault-tolerant event streaming.
* Confluent/Apicurio Schema Registry: Enforces strict data contracts and blocks unmasked PII.
* Frankfurt Cloud Infrastructure: Mandated for EU-only data residency constraints.
* AES-256: Applied for encryption-at-rest across all broker disks and databases.

## Rationale
This asynchronous, event-driven architecture decouples services to guarantee sub-800ms search performance and high availability. Robust security and Frankfurt hosting ensure compliance with EU data protection regulations.