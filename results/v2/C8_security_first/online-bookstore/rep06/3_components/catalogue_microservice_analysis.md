## Overview
The Catalogue Microservice is a secure, scalable e-commerce component designed to manage book inventory, details, and search capabilities for the Online Bookstore. It processes search and catalog queries to drive user engagement while ensuring strict regulatory compliance.

## Key Elements
- Catalogue API Controller (Node.js/Spring Boot)
- Search & Indexing Engine (Java/Python)
- Inventory Management Service
- Event Synchronization Worker
- Amazon OpenSearch & PostgreSQL
- Amazon SQS

## Relationships
- API Gateway -> Catalogue API Controller [gRPC/HTTPS]
- Catalogue API Controller -> Search & Indexing Engine [HTTP/REST]
- Catalogue API Controller -> Inventory Management Service [In-process]
- Inventory Management Service -> PostgreSQL [JDBC/TCP, TLS 1.3]
- Inventory Management Service -> Amazon SQS [HTTPS]
- Event Synchronization Worker -> Search & Indexing Engine [In-process]
- Search & Indexing Engine -> Amazon OpenSearch [HTTPS]

## Technology Stack
- AWS ECS Fargate: Scalable container orchestration without EC2 overhead
- Amazon OpenSearch: Fast, typo-tolerant search and indexing
- PostgreSQL: Relational persistence for structured inventory data
- Amazon SQS: Reliable asynchronous event queuing
- AWS KMS & Secrets Manager: Data encryption and secure credential management

## Rationale
This architecture uses containerized microservices deployed across multiple Availability Zones to ensure 99.95% uptime and scale to 1M MAU. Asynchronous synchronization via Amazon SQS balances search performance with near-real-time inventory accuracy.