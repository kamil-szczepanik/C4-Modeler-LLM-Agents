## Overview
ECS Fargate Go Microservices form the core backend tier of the Online Bookstore, handling business logic, order fulfillment, and notifications. They ensure high-throughput execution for 1M MAU while adhering to strict security and multi-region availability mandates.

## Key Elements
*   **Containers:** ECS Fargate Go Microservices (Go, Amazon ECSFargate, gRPC)
*   **Internal Components:** HTTP/gRPC API Routers, Domain Handlers, Business Logic Services, Data Access Repositories, Event Consumers, Outbound Adapters
*   **Data & Storage:** Amazon Aurora PostgreSQL, Amazon DynamoDB, Redis, Amazon SQS, Amazon SNS
*   **External Integrations:** Payment Gateway APIs, Third-Party Shipping Providers, Global Tax and Currency Conversion Service, Transactional Email and SMS Service Provider

## Relationships
*   React Single Page Application -> ECS Fargate Go Microservices [HTTPS, gRPC]
*   ECS Fargate Go Microservices -> Amazon Aurora PostgreSQL [TLS 1.3, AES-256]
*   ECS Fargate Go Microservices -> AWS DynamoDB [TLS 1.3, AES-256]
*   ECS Fargate Go Microservices -> Amazon SQS & SNS [AWS SDK]
*   ECS Fargate Go Microservices -> Redis [Redis Protocol]
*   ECS Fargate Go Microservices -> Payment Gateway APIs [HTTPS REST APIs]
*   ECS Fargate Go Microservices -> Third-Party Shipping Providers [HTTPS REST APIs]

## Technology Stack
*   **Language:** Go (concurrent goroutines for low-latency performance)
*   **Compute:** Amazon ECS on AWS Fargate (serverless container orchestration)
*   **Communication:** gRPC for internal microservices, REST/HTTPS for external APIs
*   **Databases:** Amazon Aurora PostgreSQL and AWS DynamoDB (encrypted via AES-256)
*   **Security:** AWS KMS, AWS Secrets Manager, SPIFFE/SPIRE for mTLS, JWT validation

## Rationale
Go microservices on Fargate provide scalable, low-latency execution to meet strict performance and 99.95% availability targets across global regions. Clean Architecture and robust encryption mechanisms ensure fault isolation, high security, and GDPR/CCPA compliance.