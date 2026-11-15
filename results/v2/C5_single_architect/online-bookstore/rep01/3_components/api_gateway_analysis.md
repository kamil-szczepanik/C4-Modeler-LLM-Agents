## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform designed for browsing, purchasing physical and electronic books, and accessing reviews and recommendations. It delivers a secure, multi-currency retail experience supporting high scalability and global availability.

## Key Elements
- **Customer**: End-user browsing and purchasing books.
- **Single Page Application (SPA)**: React and TypeScript frontend hosted on Amazon S3 and CloudFront.
- **API Gateway (AWS API Gateway)**: Edge component containing Routing & Dispatcher, Auth Filter, Rate Limiter, and Request Transformation/Caching components.
- **Backend Containers**: Catalog & Search (Spring Boot, Amazon SageMaker), Order & Checkout (Node.js/Express), Recommendations (Python/FastAPI), and Notification Service (Go).
- **External Systems**: Third-Party Payment Gateway, Third-Party Shipping Provider, Identity Provider / Auth Service, and Currency Exchange Rate Service.
- **Databases & Messaging**: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon EventBridge, and Amazon MSK.

## Relationships
- **Customer -> Single Page Application (SPA)**: Accesses web interface [HTTPS]
- **Single Page Application (SPA) -> API Gateway**: Sends API requests [HTTPS (REST/GraphQL)]
- **API Gateway -> Auth Filter -> Routing & Dispatcher**: Validates tokens and proxies payloads [Internal Memory]
- **API Gateway -> Backend Containers**: Routes gRPC payloads [gRPC over TLS across VPC private subnets]
- **Backend Containers -> Amazon Aurora PostgreSQL / DynamoDB**: Reads and writes transactional data [TCP/TLS]

## Technology Stack
- **AWS API Gateway**: Manages edge routing, rate limiting, and request transformations to meet availability and scalability targets.
- **React / TypeScript**: Provides a responsive, high-performance SPA frontend hosted on Amazon S3 with CloudFront CDN.
- **Spring Boot, Node.js, Python, Go**: Powers backend microservices tailored to specific domain logic (catalog, checkout, recommendations, notifications).
- **gRPC over TLS**: Ensures secure, high-performance internal communication between the API Gateway and backend containers.
- **Amazon Aurora PostgreSQL & DynamoDB**: Delivers reliable, scalable, and ACID-compliant data storage.

## Rationale
This architecture combines AWS cloud services and a containerized microservices approach to easily handle 1 million monthly active users and 99.95% uptime. Decoupling the frontend via a robust AWS API Gateway using gRPC over TLS ensures low-latency page loads and strong OWASP security mitigations.