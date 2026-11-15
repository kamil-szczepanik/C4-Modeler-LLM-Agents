## Overview
The Online Bookstore system is a scalable e-commerce platform built on AWS, designed to support secure transactions, personalized recommendations, and strict regulatory compliance. It utilizes a microservices architecture with isolated data stores to handle high user volume while protecting sensitive consumer information.

## Key Elements
- React/Angular Single Page Application (SPA) / Mobile Client
- AWS API Gateway & Reverse Proxy
- Catalog Service, Order & Checkout Service, Recommendation Service, Review Service (Java/Spring Boot, Node.js, Python)
- AWS SQS/SNS Message Broker
- Amazon ElastiCache Distributed Caching
- Compliance/User Data Container (Segregated Isolated AWS RDS/Aurora Databases)
- AWS KMS (Key Management Service) & Secrets Manager

## Relationships
- SPA / Mobile Client -> AWS API Gateway: HTTPS / REST / WebSockets
- API Gateway -> Microservices: Internal VPC Routing / gRPC / REST
- Microservices -> Compliance/User Data Container: Database-per-Service [TCP / VPC Security Groups]
- Microservices -> AWS SQS/SNS: Asynchronous Event Messaging [AMQP / HTTPS]
- Compliance/User Data Container -> AWS KMS: Cryptographic Key Management [HTTPS]

## Technology Stack
- AWS RDS / Aurora: Segregated database-per-service for strict data isolation and multi-region replication.
- AWS KMS: Powers Cryptographic Erasure and encryption-at-rest to meet GDPR/CCPA mandates.
- Flyway / Liquibase: Automated database migration tooling for zero-downtime multi-region deployments.
- AWS SQS/SNS: Asynchronous messaging for decoupled microservice communication.
- Amazon ElastiCache: Distributed caching for high-performance catalogue and session handling.

## Rationale
This architecture ensures 99.95% uptime and scalability for 1M MAU through decoupled microservices and regional AWS deployment. Cryptographic erasure and database isolation satisfy strict GDPR/CCPA compliance without sacrificing system performance.