## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It guarantees strict EU-only data residency and sub-800ms search performance.

## Key Elements
- **Users**: Library Patrons, Librarians and Circulation Staff, Library Administrators
- **API Gateway**: Kong/Envoy
- **Patron Web App & API**: Node.js/Next.js
- **Staff Management API**: Java/Spring Boot
- **Search Engine**: Managed OpenSearch/Elasticsearch (EU-hosted)
- **Database**: Managed PostgreSQL (EU-hosted, AES-256 encrypted)
- **Integration/Messaging Container**: Managed Apache Kafka / Amazon MQ (EU-hosted)
- **Notification Dispatcher**: Go/Worker service
- **External Systems**: External Notification Service, Payment Gateway, Identity Provider (IdP), ILL Network, Observability Platform & SIEM

## Relationships
- **Patron Web App** -> **API Gateway**: HTTPS/REST
- **API Gateway** -> **Patron/Staff Containers**: gRPC via mTLS
- **Staff Management Container** -> **Message Broker**: AMQP / Kafka protocol
- **Containers** -> **External SIEM**: OpenTelemetry (OTel) / Prometheus metrics over TLS

## Technology Stack
- **API Gateway**: Kong/Envoy for TLS termination, JWT validation, rate limiting
- **Backend & Frontend**: Node.js/Next.js (Patron Portal), Java/Spring Boot (Staff API), Go (Notification Dispatcher)
- **Data & Search**: Managed PostgreSQL & OpenSearch (EU regions) with EU-KMS AES-256 encryption
- **Messaging**: Managed Kafka / Amazon MQ for asynchronous decoupling
- **Security & Observability**: OpenTelemetry, Prometheus, mutual TLS, EU-hosted Secrets Manager

## Rationale
Separating patron self-service from staff management enables independent scaling to consistently achieve sub-800ms search latency. Managed EU-hosted cloud services, strict encryption, and decoupled message brokering enforce regional data residency while ensuring high availability during third-party outages.