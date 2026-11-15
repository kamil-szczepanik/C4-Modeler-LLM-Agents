## Overview
The Library Management System is a comprehensive digital solution for public and academic libraries to catalogue items, manage circulation, and provide secure self-service portals. The architecture enforces strict EU-only data residency and sub-second search performance while serving patrons, librarians, and administrators.

## Key Elements
- **Users**: Library Patrons (Students, Public), Librarians / Circulation Staff, Library Administrators
- **Frontend Container**: React/TypeScript Single Page Application (SPA) served via CDN
- **API Gateway**: Nginx/Kong handling routing, rate limiting, and JWT/OAuth2 validation
- **Catalogue & Search Service**: Spring Boot / Java with Elasticsearch
- **Circulation & Member Service**: Node.js / NestJS handling loans, fines, and PII
- **Analytics & Reporting Container**: Python / FastAPI with a read-optimized PostgreSQL replica
- **Notification Worker Container**: Go-based background worker
- **Message Broker**: Apache Kafka / RabbitMQ
- **Databases**: EU-hosted PostgreSQL with AES-256 encryption-at-rest
- **External Systems**: EU Identity Provider (IdP), EU-compliant Payment Gateway, EU Cloud Hosting Provider (Frankfurt)

## Relationships
- **Users to Frontend**: HTTPS
- **Frontend to API Gateway**: HTTPS/REST
- **API Gateway to IdP**: OAuth2/OIDC token introspection
- **API Gateway to Backend Services**: gRPC over mTLS within Frankfurt VPC
- **Circulation Service to PostgreSQL**: TLS with AES-256 encryption-at-rest
- **Catalogue Service to Elasticsearch**: Internal cluster protocol
- **Services to Message Broker**: TLS-secured gRPC/AMQP with SASL/SCRAM authentication
- **Payment Worker to Payment Gateway**: HTTPS/TLS 1.3

## Technology Stack
- **React/TypeScript**: Powers the interactive patron and staff self-service portal
- **Nginx/Kong**: Acts as a secure, high-performance single entry point with rate limiting
- **Spring Boot & Elasticsearch**: Delivers sub-second catalogue searches meeting R-05 (<800ms)
- **Node.js / NestJS & PostgreSQL**: Secures transactional circulation data and PII under strict EU residency
- **Python / FastAPI**: Isolates heavy administrative reporting queries via a read replica
- **Go & Kafka/RabbitMQ**: Handles asynchronous notifications and event-driven decoupled workflows

## Rationale
This container architecture isolates high-throughput search, transactional circulation, and reporting workloads to guarantee performance and prevent resource contention. Enforcing private subnets, mTLS, and AES-256 encryption within the Frankfurt cloud region strictly satisfies EU data residency and GDPR compliance constraints.