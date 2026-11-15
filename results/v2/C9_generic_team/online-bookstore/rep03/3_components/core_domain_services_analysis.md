## Overview
- The system is an online bookstore providing catalog browsing, secure checkout, reviews, and personalized recommendations at scale.
- The architecture utilizes a scalable, cloud-native microservices design on AWS to ensure high availability, security, and performance.

## Key Elements
- Core Domain Services container hosted on AWS ECS / EKS
- Caching Layer using Amazon ElastiCache (Redis)
- Persistence Layer using Amazon RDS and Amazon OpenSearch
- Asynchronous Message Broker using AWS SQS/SNS with Dead Letter Queue (DLQ)
- API Gateway / BFF using AWS API Gateway

## Relationships
- API Gateway / BFF -> Core Domain Services: Invokes backend business logic via gRPC and REST
- Core Domain Services -> Caching Layer: Retrieves cached catalogue, rate data, and idempotency tokens via TCP
- Core Domain Services -> Persistence Layer: Reads and writes transactional and search data via TCP
- Core Domain Services -> Asynchronous Message Broker: Publishes asynchronous events for orders and shipping via AMQP/HTTPS

## Technology Stack
- AWS ECS / EKS: Orchestrates containerized microservices for scalability and high availability
- gRPC & Protocol Buffers: Ensures high-performance synchronous inter-service communication and strict API contracts
- Amazon ElastiCache (Redis): Provides high-speed caching, rate-limiting, and idempotency key validation
- Amazon RDS & OpenSearch: Powers relational transactional storage and fast keyword search capabilities
- AWS Systems Manager Parameter Store / Secrets Manager: Enables secure dynamic configuration and secret management

## Rationale
- This architecture combines CQRS, internal Domain-Driven Design boundaries, and strict schema isolation to independently scale read and write paths for 1M MAU.
- Resiliency patterns like circuit breakers, idempotency keys, and decoupled health probes directly satisfy the 99.95% availability target and performance constraints.