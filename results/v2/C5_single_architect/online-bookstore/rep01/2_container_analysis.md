## Overview
The Online Bookstore is a scaled-down e-commerce platform for purchasing physical and electronic books with integrated recommendations and reviews. It provides a secure, high-performance, multi-region architecture capable of scaling to 1M MAU.

## Key Elements
* Customer
* Single Page Application (SPA)
* API Gateway
* Catalog & Search Container
* Order & Checkout Container
* Recommendations Container
* Notification Service
* Async Event Bus
* Amazon Aurora PostgreSQL & Amazon DynamoDB
* Third-Party Payment Gateway, Shipping Provider, Identity Provider, Currency Exchange Rate Service

## Relationships
* Customer -> SPA: HTTPS / WSS
* SPA -> API Gateway: HTTPS (REST/GraphQL)
* API Gateway -> Catalog, Order, Recommendations, Notification Containers: gRPC over TLS (VPC private subnets)
* Order & Checkout Container -> Third-Party Payment Gateway: HTTPS (TLS)
* Order & Checkout Container -> Async Event Bus: Publishes `OrderPlaced` events via TLS
* Async Event Bus -> Third-Party Shipping Provider: Webhooks / HTTPS APIs
* Services -> Amazon Aurora PostgreSQL & DynamoDB: SQL / NoSQL over TLS

## Technology Stack
* Frontend: React / TypeScript on Amazon S3 + CloudFront for <2s page load performance
* Gateway: AWS API Gateway for rate limiting and auth validation
* Backend Services: Spring Boot (Catalog), Node.js/Express (Order), Python/FastAPI (Recommendations), Go (Notifications)
* Databases: Amazon Aurora PostgreSQL (relational) and Amazon DynamoDB (carts/sessions)
* Messaging: Amazon EventBridge / Amazon MSK for asynchronous decoupling
* AI/ML: Amazon SageMaker for recommendations

## Rationale
This microservices-based AWS architecture ensures 99.95% uptime and horizontal scalability for 1M MAU through containerized services and managed databases. Strict regional deployment and secure third-party integrations fulfill multi-currency, compliance, and strict performance constraints.