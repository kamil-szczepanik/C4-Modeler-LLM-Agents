## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It is architected as a distributed containerized system ensuring strict EU data residency and high-performance search capabilities.

## Key Elements
* Patrons and Staff
* Web Application (React, CDN)
* API Gateway (NGINX/Envoy)
* Core Services Container (Java, Spring Boot)
* Search Container (Elasticsearch)
* Database (PostgreSQL)
* Caching Layer (Redis)
* Async Worker Container
* Integration Worker Container
* Search Worker Container (Debezium/CDC)
* RabbitMQ Message Broker
* External Systems: Identity Provider, Payment Gateway, National Library Registry, Notification Service, Digital Content Delivery Provider

## Relationships
* Patrons/Staff to Web Application via HTTPS
* Web Application to API Gateway via HTTPS/REST/GraphQL
* API Gateway to Core Services and Search via gRPC/HTTPS
* Core Services to PostgreSQL and Redis via TCP
* Core Services to RabbitMQ via AMQP
* RabbitMQ to Async, Integration, and Search Workers via AMQP
* Search Worker to PostgreSQL (CDC) and Elasticsearch via HTTPS/REST

## Technology Stack
* Frontend: React hosted on CDN for static patron and staff portals
* Gateway & Core: NGINX/Envoy for routing; Java Spring Boot for transactional domain logic
* Data & Caching: PostgreSQL for EU-resident relational data; Redis for high-speed metadata caching
* Search & Sync: Elasticsearch for sub-800ms search performance (R-05); Debezium for change data capture
* Messaging & Workers: RabbitMQ for AMQP event streaming; dedicated workers for background jobs, integrations, and search indexing

## Rationale
This containerized architecture decouples heavy search and external integration workloads from core transactional services, ensuring sub-800ms search responses (R-05). Strict EU-restricted cloud deployment and regional routing guarantees enforce data residency compliance.