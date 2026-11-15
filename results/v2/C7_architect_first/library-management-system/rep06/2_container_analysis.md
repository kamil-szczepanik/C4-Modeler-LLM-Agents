## Overview
[The Library Management System is a comprehensive digital platform for public and academic libraries designed to catalogue physical and digital assets, manage circulation, and provide self-service portals.]
[It strictly enforces EU-only data residency and maintains a 99th-percentile search response time of under 800 milliseconds.]

## Key Elements
* Library Patrons and Library Staff (Users)
* External Payment Gateway and Digital Content Repositories (External Systems)
* Web Application (React/TypeScript, Nginx)
* API Gateway (Kong or Spring Cloud Gateway)
* Core Domain Service (Java/Spring Boot)
* Search Service (Python/FastAPI, Elasticsearch)
* Notification Service (Node.js)
* PostgreSQL Database
* RabbitMQ Message Broker

## Relationships
* Users to Web Application via HTTPS
* Web Application to API Gateway via HTTPS/REST
* API Gateway to Core Domain Service and Search Service via gRPC with mTLS
* Core Domain Service to PostgreSQL via TLS 1.3
* Notification Service to RabbitMQ via AMQP with TLS 1.3
* External Systems to API Gateway via HTTPS

## Technology Stack
* React/TypeScript & Nginx: Client-side rendering and static asset hosting
* Kong / Spring Cloud Gateway: API routing, rate limiting, and OAuth2/OIDC token validation
* Java / Spring Boot: Core business logic, circulation management, and immutable audit logging
* Python / FastAPI & Elasticsearch: High-performance search to meet the <800ms P99 requirement
* PostgreSQL: Relational operational data store with primary-replica streaming
* Node.js & RabbitMQ: Asynchronous messaging with quorum queues for zero-loss notifications
* Kubernetes: Container orchestration utilizing NetworkPolicies, PDBs, and HPAs in EU-region clusters

## Rationale
[The container decomposition isolates the high-performance search engine to meet strict latency goals while maintaining modular scalability for core circulation tasks.]
[A secure, Kubernetes-orchestrated, EU-hosted infrastructure guarantees strict regulatory data residency and zero-trust security compliance.]