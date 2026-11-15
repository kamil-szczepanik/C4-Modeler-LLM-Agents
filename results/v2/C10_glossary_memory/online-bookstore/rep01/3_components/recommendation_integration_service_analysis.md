## Overview
The Online Bookstore is a multi-region e-commerce platform providing catalogue browsing, secure checkout, reviews, and personalized recommendations for 1 million monthly active users. The architecture uses a cloud-native, microservices-based approach deployed across multiple AWS regions to ensure high availability and sub-second performance.

## Key Elements
- Book Shopper [person]
- Web Frontend [container] (React SPA)
- Amazon API Gateway [container] (Amazon API Gateway)
- Recommendation Integration Service [container] (Node.js)
  - Recommendation API Controller [component] (Node.js / Express)
  - Recommendation Fallback Manager [component] (Node.js)
  - Contextual Fallback Cache [component] (Node.js / LRU-Cache)
  - Clickstream Event Publisher [component] (Node.js / AWS SDK)
- ML Recommendation Engine [externalSystem] (Amazon Personalize)
- Amazon Aurora PostgreSQL [container] (Amazon Aurora PostgreSQL)

## Relationships
- Book Shopper -> Web Frontend: Browses store [HTTPS via AWS CloudFront]
- Web Frontend -> Amazon API Gateway: Forwards API requests [HTTPS/REST with JWT validation]
- Amazon API Gateway -> Recommendation Integration Service: Routes recommendation requests [HTTPS/REST with JWT validation]
- Recommendation API Controller -> Recommendation Fallback Manager: Invokes fallback on failure [In-process function call]
- Recommendation Fallback Manager -> Contextual Fallback Cache: Queries category-specific fallback items [In-process memory lookup]
- Recommendation Fallback Manager -> Amazon Aurora PostgreSQL: Refreshes fallback cache [TCP]
- Clickstream Event Publisher -> ML Recommendation Engine: Publishes user interaction events [Asynchronous SQS/SNS]

## Technology Stack
- Node.js & Express: Lightweight runtime for building scalable microservices and APIs.
- Amazon ECS with AWS Fargate: Serverless container orchestration for secure, auto-scaling microservice deployment.
- Amazon Personalize: Managed machine learning service for real-time personalized recommendations.
- Amazon Aurora PostgreSQL: Multi-region relational database for persistent catalogue and sales data storage.
- AWS Secrets Manager: Secure credential storage injected dynamically into container runtimes.

## Rationale
This architecture ensures 99.95% availability and sub-2-second page loads via resilient microservices and caching. GDPR/CCPA compliance and data security are maintained through telemetry pseudonymization, TLS 1.3, and least-privilege database access.