## Overview
The Online Bookstore is a globally scaled e-commerce platform built on AWS, designed to handle 1M MAU with 99.95% availability while supporting book browsing, secure checkout, reviews, and personalized recommendations. It implements a decoupled, event-driven architecture to ensure low latency and strict GDPR/CCPA compliance across multi-currency transactions.

## Key Elements
* **Book Buyer & Reviewer**: End user browsing catalogues, purchasing books, and leaving reviews.
* **Store Administrator**: Back-office user managing inventory and administrative events.
* **Single-Page Application (SPA)**: React and TypeScript frontend hosted on AWS S3 and CloudFront.
* **Core E-Commerce API**: Node.js (NestJS) application running on AWS ECS (Fargate).
* **Recommendation Service**: Python (FastAPI) application running on AWS ECS (Fargate).
* **Amazon EventBridge**: Event bus containing Default Bus, Custom Event Bus (`bookstore.retail`), Event Rules & Routing, Target Dispatcher, and Event Archive (`bookstore-archive`).
* **Databases & Caching**: Amazon Aurora PostgreSQL (Multi-AZ) and Amazon ElastiCache (Redis).
* **External Services**: External Payment Gateway, Third-Party Shipping Provider API.

## Relationships
* **SPA -> Amazon API Gateway**: Routes frontend requests using HTTPS/GraphQL.
* **Amazon API Gateway -> Core E-Commerce API**: Forwards client requests via REST/GraphQL.
* **Core E-Commerce API -> Custom Event Bus**: Publishes domain events (`OrderPlaced`, `ItemReviewed`) via AWS SDK/HTTPS.
* **Custom Event Bus -> Event Archive**: Archives filtered events for compliance via Native EventBridge Rule.
* **Event Rules & Routing -> Amazon SQS**: Buffers routed events for downstream processing via AWS API.
* **Core E-Commerce API -> Amazon Aurora PostgreSQL**: Manages relational transactional data via PostgreSQL protocol.

## Technology Stack
* **Frontend**: React and TypeScript hosted on AWS S3 & CloudFront for rapid global content delivery.
* **Backend Compute**: Node.js (NestJS) and Python (FastAPI) on AWS ECS (Fargate) for scalable containerized microservices.
* **Database & Caching**: Amazon Aurora PostgreSQL (Multi-AZ) for ACID-compliant persistence and Amazon ElastiCache (Redis) for low-latency session and data caching.
* **Event Integration**: Amazon EventBridge with custom buses, rule engines, and encrypted archives for asynchronous, decoupled event-driven workflows.
* **Security & Compliance**: AWS IAM, TLS 1.3, and AWS KMS Customer-Managed Keys (CMK) ensuring data protection, PII payload restriction, and GDPR/CCPA compliance.

## Rationale
This AWS-native, event-driven architecture decouples heavy background processes like recommendations from synchronous user actions, protecting page load performance under high load (1M MAU). Utilizing managed services like ECS, Aurora, and EventBridge ensures high availability (99.95%), seamless horizontal scalability, and robust security controls tailored to strict regulatory constraints.