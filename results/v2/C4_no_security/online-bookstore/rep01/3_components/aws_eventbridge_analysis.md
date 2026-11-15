## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform designed to support physical and electronic book sales, search, reviews, and recommendations. It leverages a multi-region AWS cloud architecture to deliver high availability and performance for 1M MAU.

## Key Elements
- **Users**: Guest Shopper, Registered Customer, Store Administrator, Customer Support Agent
- **External Systems**: Payment Gateway, Shipping Provider API, Tax/Compliance Service, AWS Route 53
- **Containers**: Frontend Container (React, TypeScript, Amazon CloudFront, S3), API Management (Amazon API Gateway), Catalog & Search (Java, Spring Boot, Amazon OpenSearch), Checkout & Order (Node.js, Amazon RDS PostgreSQL), Recommendation (Python, FastAPI), Analytics Ingestion (Go, Amazon Kinesis)
- **Messaging & Data**: AWS SQS, AWS EventBridge (Default & Custom Event Buses, Event Rules, Input Transformers, API Destinations), Amazon DynamoDB, Amazon RDS (PostgreSQL)

## Relationships
- Frontend Container -> API Management: Routes client requests via HTTPS
- API Management -> Catalog & Search: Forwards product browse and search queries via gRPC/HTTPS
- API Management -> Checkout & Order: Manages shopping cart and secure checkout via HTTPS
- Checkout & Order -> Default Event Bus: Publishes `OrderPlaced` JSON events via HTTPS/AWS SDK
- Default Event Bus -> SQS Queue: Routes matched events via Amazon SQS (SDK/SQS protocol, HTTPS)
- Event Rules -> API Destinations: Dispatches external shipping events via HTTPS with connection throttling

## Technology Stack
- **Cloud Provider**: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region redundancy and low latency.
- **Frontend**: React, TypeScript, hosted on Amazon S3 and delivered via Amazon CloudFront.
- **Backend Services**: Java (Spring Boot) for catalog, Node.js for checkout, Python (FastAPI) for recommendations, Go for analytics ingestion.
- **Databases & Search**: Amazon RDS (PostgreSQL) for transactional data, Amazon DynamoDB for fast lookups, Amazon OpenSearch for catalog search.
- **Integration & Messaging**: AWS EventBridge and Amazon SQS for asynchronous event-driven decoupling and durable buffering.

## Rationale
This architecture uses serverless event-driven patterns with AWS EventBridge and SQS to decouple core domains, ensuring scalability to 1M MAU and 99.95% availability. Multi-region deployment and strict observability meet strict performance and compliance requirements.