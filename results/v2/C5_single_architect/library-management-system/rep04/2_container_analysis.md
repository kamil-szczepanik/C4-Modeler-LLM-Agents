## Overview
The Library Management System is a comprehensive solution for public and academic libraries designed to catalogue items, manage circulation, and provide self-service portals. It ensures strict EU-only data residency while delivering high-performance catalog searches.

## Key Elements
* Library Patron and Librarian / Library Staff (Users)
* Web Application Container (React, TypeScript)
* API Gateway Container (Kong or NGINX)
* Core Domain Container (Java, Spring Boot)
* Search Container (Elasticsearch)
* Integration Worker Container (Node.js/Python)
* Message Broker Container (RabbitMQ)
* PostgreSQL Database (EU-hosted)
* External Systems: Identity Provider / IdS, Payment Gateway, Notification Service, Digital Content Repository / DRM Provider

## Relationships
* Web Application to API Gateway via HTTPS/REST and WebSockets
* API Gateway to internal containers via gRPC and internal REST
* Core Domain to PostgreSQL and Elasticsearch via native TCP drivers over TLS
* Core Domain to Message Broker (RabbitMQ) via AMQP over TLS
* Integration Worker to external Payment Gateway and Notification Service

## Technology Stack
* React with TypeScript: Powers the frontend web application container
* Java with Spring Boot: Implements the reliable Core Domain container logic
* Elasticsearch: Dedicated engine to meet the <800ms search latency requirement
* PostgreSQL: EU-hosted relational database for transactional data integrity
* RabbitMQ: Asynchronous message broker to decouple workflows and integrations
* Kong or NGINX: API Gateway for secure routing, SSL termination, and rate limiting

## Rationale
This containerized architecture isolates the search workload into Elasticsearch to easily achieve the required sub-800ms response times. Additionally, hosting all databases and message brokers within the EU guarantees full compliance with strict data residency constraints.