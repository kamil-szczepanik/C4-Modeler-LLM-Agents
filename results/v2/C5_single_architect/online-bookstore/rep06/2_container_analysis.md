## Overview
The Online Bookstore is a globally distributed, scalable e-commerce system designed to support physical and electronic book sales, search, secure checkout, reviews, and recommendations. It delivers high performance and 99.95% availability for 1 million monthly active users across multiple AWS regions.

## Key Elements
* **Customer & Admin/Support Staff**: End users and operators interacting with the system.
* **Single Page Application (SPA)**: React frontend hosted on Amazon S3 and distributed via Amazon CloudFront.
* **API Gateway**: Amazon API Gateway managing REST/GraphQL routing and JWT security.
* **Catalog Service**: Go microservice backed by Amazon Aurora PostgreSQL.
* **Order & Checkout Service**: Spring Boot microservice backed by Amazon Aurora PostgreSQL.
* **Recommendation Service**: Python FastAPI microservice utilizing Amazon ElastiCache (Redis).
* **Customer & Review Service**: Node.js microservice backed by MongoDB.
* **Messaging & Workers**: Amazon SQS and SNS for asynchronous event-driven decoupling.
* **External Systems**: Payment Gateway, Shipping Provider APIs, Tax Calculation Service, and Identity Provider/SSO.

## Relationships
* **Customer -> SPA**: HTTPS / HTML / JS
* **SPA -> API Gateway**: HTTPS / JSON (JWT authenticated)
* **API Gateway -> Microservices (Catalog, Order, Recommendation, Customer & Review)**: gRPC / HTTPS
* **Order Service -> External Payment & Shipping APIs**: HTTPS / REST
* **Order Service -> Amazon SQS**: Async / JSON
* **Microservices -> Amazon Aurora PostgreSQL**: TCP / PostgreSQL protocol
* **Recommendation Service -> Amazon ElastiCache (Redis)**: TCP / Redis protocol

## Technology Stack
* **AWS Cloud (us-east-1, eu-west-1, ap-southeast-1)**: Multi-region deployment for global availability and low latency.
* **React & Amazon CloudFront/S3**: Delivers sub-2-second page loads on 3G connections.
* **Go, Spring Boot, Python FastAPI, Node.js**: Domain-specific microservice runtimes optimized for performance and scalability.
* **Amazon Aurora PostgreSQL**: Provides ACID compliance for transactional catalog and order data.
* **Amazon ElastiCache (Redis)**: Enables fast catalog caching and session management.
* **MongoDB**: Stores flexible, unstructured customer review data.
* **Amazon SQS/SNS**: Decouples services asynchronously for reliable order processing and shipping integration.

## Rationale
This container architecture uses microservices and managed AWS services to independently scale high-demand features like search and checkout while meeting the 1M MAU and 99.95% uptime targets. Polyglot persistence and asynchronous messaging via SQS ensure optimal performance, data isolation, and strict compliance with security and regional constraints.