## Overview
- A distributed Library Management System designed to handle public and academic library catalogues, circulation workflows, and self-service portals.
- Enforces strict EU-only data residency while maintaining high-performance search responses under 800 milliseconds at the 99th percentile.

## Key Elements
- Library Member (Patron) [person]
- Librarian / Staff [person]
- Library Administrator [person]
- Web Application / SPA (React, TypeScript) [container]
- API Gateway (NGINX / Envoy) [container]
- Catalog & Search Service (Java, Spring Boot + Elasticsearch) [container]
- Circulation Service (Node.js / NestJS) [container]
- Database (PostgreSQL) [container]
- Message Broker (Apache Kafka / RabbitMQ) [container]
- Audit Service (Go) [container]
- Payment Gateway [externalSystem]
- Notification Provider [externalSystem]
- Identity Provider [externalSystem]

## Relationships
- Library Member (Patron), Librarian / Staff, Library Administrator -> API Gateway: Accesses system features via HTTPS / TLS 1.3
- API Gateway -> Catalog & Search Service, Circulation Service: Routes requests using gRPC over mTLS
- Circulation Service -> Database: Reads and writes transactional data using SQL over mTLS
- Circulation Service -> Message Broker: Publishes and consumes events using AMQP/Kafka Protocol over mTLS
- Circulation Service -> Audit Service: Sends audit logs using REST over mTLS
- Circulation Service -> Payment Gateway, Notification Provider: Processes payments and sends alerts using HTTPS/REST
- API Gateway -> Identity Provider: Authenticates users via OIDC/OAuth2 over HTTPS

## Technology Stack
- React with TypeScript: Powers the Web Application / SPA for client-side rendering.
- NGINX / Envoy: Provides edge routing, TLS termination, and OIDC token validation at the API Gateway.
- Java with Spring Boot & Elasticsearch: Powers the Catalog & Search Service to meet sub-800ms search constraints.
- Node.js with NestJS: Implements the Circulation Service for efficient loan and fine management.
- PostgreSQL: Acts as the primary relational data store with AES-256 PII column encryption.
- Apache Kafka / RabbitMQ: Facilitates asynchronous, event-driven messaging.
- Go: Powers the high-performance Audit Service.
- Kubernetes: Hosts containerized workloads with horizontal pod autoscaling and Vault-backed secrets.

## Rationale
- Microservices architecture cleanly separates high-performance search requirements from transactional circulation workflows.
- Strict mTLS, TLS 1.3, and AES-256 encryption ensure compliance with EU-only data residency and GDPR security mandates.