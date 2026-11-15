## Overview
[The Online Bookstore system provides a scalable e-commerce platform for purchasing physical and electronic books with integrated recommendations, reviews, and secure checkout. The architecture utilizes AWS cloud services to handle 1 million MAU with 99.95% uptime across multiple global regions.]

## Key Elements
*   **Book Shopper**: Primary user persona executing searches, cart management, and secure checkouts.
*   **AWS API Gateway**: Entry point routing internal requests via HTTPS/gRPC.
*   **Order & Checkout Service**: Spring Boot modular monolith container handling cart management, checkout orchestration, and multi-currency conversion.
*   **Stripe/PayPal**: External payment processing systems.
*   **Amazon Aurora PostgreSQL**: Relational database for persistent order and cart state.
*   **Redis (ElastiCache)**: In-memory store for idempotency keys and caching.
*   **Amazon EventBridge / SQS**: Asynchronous event bus and messaging queue.
*   **AWS ECS (Fargate)**: Container execution platform across us-east-1, eu-west-1, and ap-southeast-1.

## Relationships
*   AWS API Gateway -> Order & Checkout Service: Routes order and checkout requests [Internal HTTPS / gRPC]
*   Order & Checkout Service -> Stripe/PayPal: Processes payments and risk assessments [HTTPS / REST]
*   Order & Checkout Service -> Amazon Aurora PostgreSQL: Persists transactional order and cart data [JDBC / AWS SDK]
*   Order & Checkout Service -> Redis (ElastiCache): Validates idempotency keys and caches exchange rates [TCP / Redis Protocol]
*   Order & Checkout Service -> Amazon EventBridge and Amazon SQS: Publishes order status events [AWS SDK]

## Technology Stack
*   **Spring Boot (Java)**: Core framework for the Order & Checkout Service container, enabling modular monolith design.
*   **Amazon Aurora PostgreSQL & HikariCP/RDS Proxy**: Relational persistence layer with optimized connection pooling for high concurrency.
*   **Redis Cluster**: High-availability caching and idempotency filter storage to prevent duplicate transactions.
*   **Resilience4j**: Circuit breaker implementation to isolate external payment gateway failures.
*   **AWS ECS (Fargate)**: Serverless container hosting ensuring multi-region scalability and 99.95% availability.

## Rationale
[This architecture combines a modular Spring Boot monolith with robust AWS cloud services to guarantee transactional integrity, fault tolerance, and low latency for global financial operations. Utilizing managed infrastructure like ECS Fargate, RDS Proxy, and Redis ElastiCache ensures stringent scalability, security, and 99.95% availability requirements are met.]