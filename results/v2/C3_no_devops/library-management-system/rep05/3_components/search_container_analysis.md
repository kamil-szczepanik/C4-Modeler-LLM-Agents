## Overview
The Library Management System provides physical and digital item cataloging, circulation management, and self-service portals for libraries. The architecture guarantees sub-second search performance while enforcing strict EU-only data residency and patron privacy.

## Key Elements
- Library Patrons and Librarians / Circulation Staff
- Web Application (React, TypeScript, Nginx)
- API Gateway (Spring Cloud Gateway, Java)
- Core Services Container (Spring Boot, Java)
- Search Container (OpenSearch / Elasticsearch)
- PostgreSQL (AWS RDS EU)
- Message Broker (Apache Kafka / RabbitMQ)
- External Systems: Stripe EU, Keycloak/Auth0 EU tenant, SendGrid EU

## Relationships
- API Gateway -> Search Container: Routes search queries via gRPC/HTTPS using mTLS
- Core Services Container -> Search Container: Indexes and queries search items via TCP/gRPC with mTLS
- Core Services Container -> Search Container (Analytics Exporter): Polls aggregated anonymized metrics over REST/TCP using mTLS

## Technology Stack
- OpenSearch: Powers sub-second search performance (< 800ms) and faceted filtering
- Spring Boot / Java: Implements internal search components and API handlers
- AES-256 with EU-hosted KMS: Encrypts search indices and snapshot storage at rest
- OpenSearch Security Plugins: Enforces fine-grained access control (FGAC) and JWT claim assertions

## Rationale
This architecture uses an isolated OpenSearch cluster to fulfill high-performance search requirements while enforcing strict network, cryptographic, and anonymization controls to ensure compliance with EU data residency mandates.