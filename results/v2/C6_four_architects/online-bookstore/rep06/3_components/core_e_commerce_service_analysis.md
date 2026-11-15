## Overview
The Core E-Commerce Service is a NestJS modular application running on AWS ECS Fargate that manages bookstore operations, transactions, and user experiences. It provides robust e-commerce capabilities while ensuring high scalability, strict transactional integrity, and low-latency performance.

## Key Elements
- **Catalog Component**: Manages book browsing, keyword searches, and product details.
- **Cart Management Component**: Handles shopping cart state and low-latency session caching.
- **Checkout & Order Processing Component**: Orchestrates secure transactions and multi-currency pricing.
- **Rating & Review Component**: Manages customer reviews and 5-star ratings.
- **Currency Conversion Component**: Resolves dynamic pricing across USD, EUR, and GBP.
- **Shipping Integration Component**: Coordinates asynchronous third-party shipping API calls.
- **Inventory Management Component**: Validates and reserves stock levels to prevent overselling.
- **Event Dispatcher Component**: Publishes domain events asynchronously.

## Relationships
- **Catalog, Checkout, Inventory, Review Components -> Amazon Aurora PostgreSQL**: Reads and writes transactional data [SQL/TLS via TypeORM]
- **Cart Management Component -> Amazon DynamoDB & Amazon ElastiCache (Redis)**: Persists session/cart state [Redis Protocol / TLS]
- **Checkout & Order Processing Component -> Amazon SQS**: Triggers shipping integration tasks [AWS SDK / HTTPS]
- **Event Dispatcher Component -> Amazon EventBridge**: Publishes domain events (`OrderPlaced`, `ReviewAdded`) [AWS SDK / HTTPS]
- **Internal Components -> Internal Components**: Executes synchronous business logic [TypeScript interfaces / In-Process Method Calls]

## Technology Stack
- **NestJS & TypeScript**: Enforces strict modular boundaries and type safety for complex payloads.
- **Amazon ECS Fargate**: Provides serverless container orchestration for scalability.
- **Amazon Aurora PostgreSQL**: Ensures ACID transactional consistency for orders, catalog, and reviews.
- **Amazon ElastiCache (Redis)**: Delivers low-latency session caching and currency rate caching.
- **Amazon SQS & EventBridge**: Decouples external API dependencies and handles reliable asynchronous messaging.

## Rationale
The modular NestJS architecture isolates bounded contexts, enabling the system to effortlessly handle 1M MAU and maintain 99.95% availability. Utilizing in-process method calls alongside asynchronous AWS services ensures sub-2-second page loads and strict ACID compliance for financial transactions.