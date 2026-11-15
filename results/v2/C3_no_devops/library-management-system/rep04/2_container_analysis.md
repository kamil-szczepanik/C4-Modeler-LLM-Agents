## Overview
The Library Management System is a comprehensive platform designed for public and academic libraries to catalogue physical and digital assets, manage circulation workflows, and deliver self-service patron portals. It enforces strict EU-only data residency and sub-800ms search response times.

## Key Elements
* Users: Library Patron, Librarian/Circulation Staff, Library Administrator
* External Systems: Identity Provider (IdP), Payment Gateway, Notification Service, Inter-Library Loan (ILL) Network
* Core Containers: API Gateway (Nginx/Kong), Patron Portal (React SPA), Staff Dashboard (Angular SPA), Core Circulation & Cataloguing Service (Spring Boot), Search Service (Elasticsearch), Integration Service (Node.js), Notification Worker (Python/Celery), Reporting Service (Python/FastAPI)
* Data Stores: PostgreSQL (Primary database), PostgreSQL Read Replica (Analytics), RabbitMQ (Message broker)

## Relationships
* Patron Portal / Staff Dashboard -> API Gateway via HTTPS (TLS 1.3)
* API Gateway -> Core Circulation Service & Search Service via gRPC/REST over TLS 1.3
* Core Circulation Service -> PostgreSQL via JDBC (TLS 1.3) with asynchronous replication to PostgreSQL Read Replica
* Integration Service -> External Systems via REST/Webhooks over mTLS
* Notification Worker -> RabbitMQ via AMQP over TLS 1.3
* Staff Dashboard -> Reporting Service via REST/JSON over mTLS
* Reporting Service -> PostgreSQL Read Replica via SQL over mTLS

## Technology Stack
* React & Angular: Chosen for building responsive, decoupled single-page application frontends.
* Nginx/Kong: Selected as an EU-hosted API Gateway for centralized ingress, routing, and OAuth 2.0 validation.
* Spring Boot (Java): Chosen for the core circulation service to ensure strict ACID transaction compliance.
* Elasticsearch: Deployed to guarantee 99th-percentile search responses under 800ms (R-05) without impacting primary database performance.
* PostgreSQL: Selected for robust relational data management with column-level encryption and EU-only data residency support.
* RabbitMQ & Python/Celery: Chosen for asynchronous background task processing and notifications.
* Node.js: Selected for the Integration Service to efficiently handle asynchronous external API payloads.

## Rationale
This architecture uses dedicated micro-services and a specialized search engine to meet strict performance targets (<800ms search) while isolating transactional workloads. Strict network segmentation, private subnets, and encryption mechanisms ensure comprehensive EU data residency and GDPR compliance.