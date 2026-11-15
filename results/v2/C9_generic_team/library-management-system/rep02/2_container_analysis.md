## Overview
The Library Management System provides public and academic libraries with item cataloging, circulation management, and self-service portals. It enforces strict EU-only data residency and meets performance requirements through a decoupled microservices architecture.

## Key Elements
* Web Application (SPA)
* API Gateway
* Core Business Services (Catalogue, Circulation, User Management)
* Search Engine Container (Elasticsearch/OpenSearch)
* Database Container (PostgreSQL)
* Async Event Broker Container (Apache Kafka or RabbitMQ)
* Shared Caching Container (Redis)
* File Storage Container
* Worker / Background Job Processing Container
* Configuration Management Container/Service

## Relationships
* Web Application to API Gateway via HTTPS/TLS
* API Gateway to Core Business Services via gRPC/REST
* Core Business Services to Database Container via PostgreSQL protocol
* Core Business Services to Search Engine Container via HTTP/REST
* Core Business Services to Async Event Broker Container via AMQP/Kafka protocol
* Core Business Services to Shared Caching Container via Redis protocol
* Core Business Services to File Storage Container via S3/HTTPS

## Technology Stack
* Frontend: Web Application (SPA) served via CDN
* Gateway: API Gateway with TLS termination and IAM token validation
* Database: Regional PostgreSQL instance with encryption at rest
* Search: Elasticsearch or OpenSearch cluster isolated within the EU
* Caching: Redis deployed regionally in front of the database
* Messaging: Apache Kafka or RabbitMQ hosted regionally

## Rationale
Decoupling search and transaction workflows using dedicated search and caching containers ensures 99th-percentile search response times remain below 800 ms. Regional hosting of all stateful components guarantees compliance with EU-only data residency constraints.