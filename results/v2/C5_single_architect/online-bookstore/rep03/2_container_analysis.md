## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform enabling customers to purchase physical and electronic books, view ratings, and receive recommendations. It is architected on AWS across multiple global regions to support 1 million MAU with 99.95% availability.

## Key Elements
* **Customer & Administrator**: External actors interacting via web browsers.
* **Single-Page App (SPA)**: React frontend hosted on AWS S3 & CloudFront.
* **API Gateway**: AWS API Gateway managing entry points, routing, and rate-limiting.
* **Core Microservices**: Catalog, Order & Checkout, Recommendation, and Email services running on Amazon ECS/Fargate.
* **Databases & Caching**: Amazon RDS (PostgreSQL), Amazon OpenSearch, Amazon ElastiCache (Redis), and Amazon DynamoDB.
* **Integration**: AWS EventBridge, Amazon SNS/SQS, and external Payment Gateway, Shipping Provider, and Tax APIs.

## Relationships
* **Customer to SPA**: HTTPS over TLS 1.3 for browsing, cart management, and checkout.
* **SPA to API Gateway**: HTTPS/JSON for all frontend-to-backend communication.
* **API Gateway to ECS Services**: Internal VPC routing via HTTP/gRPC.
* **Order Service to EventBridge**: Publishes `OrderPlaced` events via AMQP/JSON over HTTPS.
* **EventBridge to Microservices**: SQS queues deliver asynchronous events to Recommendation and Email services.

## Technology Stack
* **AWS S3 & CloudFront**: CDN and static hosting for fast global page loads (<2s).
* **Amazon ECS / Fargate**: Container orchestration for scalable microservices without server management.
* **Node.js / NestJS**: Lightweight backend runtime for core microservices.
* **Amazon RDS (PostgreSQL)**: ACID-compliant relational storage for orders and user data.
* **Amazon OpenSearch**: Dedicated search engine for catalogue keyword search.
* **Amazon DynamoDB**: NoSQL storage for high-throughput customer reviews and ratings.
* **Amazon ElastiCache (Redis)**: In-memory caching for sessions and recommendations.
* **AWS EventBridge & SQS**: Event-driven decoupling of downstream processing.

## Rationale
This container architecture uses microservices on AWS ECS/Fargate combined with Amazon CloudFront to easily scale to 1 million MAU while maintaining sub-2-second page loads. Decoupling core operations via AWS EventBridge and utilizing specialized data stores (RDS, OpenSearch, DynamoDB) ensures 99.95% availability and robust performance.