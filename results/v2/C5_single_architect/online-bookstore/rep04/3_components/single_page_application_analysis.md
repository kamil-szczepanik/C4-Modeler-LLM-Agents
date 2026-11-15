## Overview
The Online Bookstore is a globally scaled e-commerce platform for purchasing physical and electronic books, supporting recommendations and reviews. The architecture utilizes a React SPA backed by distributed microservices deployed on AWS to meet high scalability and performance targets.

## Key Elements
* **Customer**: End-user browsing books and purchasing items.
* **Single Page Application (SPA)**: React/TypeScript frontend hosted on AWS S3/CloudFront.
* **SPA Internal Components**: Router/Navigation, State Management Store (Zustand), Catalog & Search UI, Checkout & Cart, Recommendations & Reviews, Auth & Consent Manager, and API Client.
* **API Gateway**: AWS API Gateway managing incoming requests.
* **Backend Services**: Catalog Service (Go), Order & Checkout Service (Node.js), Recommendation Service (Python FastAPI), Review Service (Java Spring Boot).
* **Data Stores**: PostgreSQL (RDS), MongoDB, Vector DB, and Amazon ElastiCache (Redis).
* **External Systems**: Payment Gateway, Shipping Provider API, Identity Provider / OAuth, Notification Service, Tax Calculation Service.

## Relationships
* **Customer -> Single Page Application**: Browses catalog, manages cart, and views recommendations via HTTPS.
* **Single Page Application -> API Gateway**: Sends API requests for catalog, orders, recommendations, and reviews via HTTPS/WSS.
* **API Gateway -> Microservices**: Routes traffic to Catalog, Order, Recommendation, and Review services using gRPC/REST.
* **Order & Checkout Service -> External Systems**: Integrates with Payment Gateway and Shipping Provider APIs over HTTPS.

## Technology Stack
* **Frontend**: React and TypeScript for type-safe UI development, hosted on AWS S3 and distributed via AWS CloudFront for low latency.
* **Backend**: Go (Catalog), Node.js (Orders), Python FastAPI (Recommendations), and Java Spring Boot (Reviews) to optimize each service for its specific domain workload.
* **Databases**: PostgreSQL for transactional data, MongoDB for reviews, and Vector DB for AI-driven recommendations.
* **Infrastructure**: AWS (us-east-1, eu-west-1, ap-southeast-1) with Amazon ElastiCache (Redis) for caching and AWS SQS/SNS for asynchronous messaging.

## Rationale
This multi-region AWS cloud architecture guarantees 99.95% uptime and supports 1 million MAU with low latency. Decoupled microservices combined with edge caching ensure page loads under 2 seconds even on constrained networks while maintaining GDPR and CCPA compliance.