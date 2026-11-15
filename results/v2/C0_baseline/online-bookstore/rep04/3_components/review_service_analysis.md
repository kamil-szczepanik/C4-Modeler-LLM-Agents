## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform that enables users to browse catalogues, purchase physical and electronic books, and interact with reviews and recommendations. The architecture leverages a microservices approach deployed on AWS to ensure high scalability, security, and global availability.

## Key Elements
- **Users**: Book Buyer / Customer, Registered Reviewer, Store Administrator / Content Manager.
- **Containers**: React / TypeScript SPA, AWS API Gateway, Order & Checkout Service, Catalog & Search Service, Recommendations Service, Review Service (Node.js).
- **Review Service Components**: Review Controller (Express.js), Review Business Logic Component, Data Access Layer & ElastiCache Read-Aside (Prisma ORM + Redis), Event Publisher Component (AWS SDK v3).
- **Data & Infrastructure**: Amazon RDS PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis), AWS EventBridge, AWS ECS (Fargate).
- **External Systems**: Stripe / PayPal, FedEx / UPS, Auth0 / AWS Cognito, AWS SES, Currency Exchange Rate Service.

## Relationships
- **React / TypeScript SPA -> AWS API Gateway**: Forwards frontend client requests [HTTPS / REST and GraphQL].
- **AWS API Gateway -> Review Service**: Routes review-related requests [mTLS / REST and gRPC].
- **Review Service -> Amazon RDS PostgreSQL**: Persists transactional review data [TCP / Prisma ORM].
- **Review Service -> Amazon ElastiCache (Redis)**: Caches rating summaries and handles rate-limiting [TCP / Redis Protocol].
- **Review Service -> AWS EventBridge**: Publishes `ReviewCreated`, `ReviewUpdated`, and GDPR anonymization events [Asynchronous HTTPS].

## Technology Stack
- **Node.js / Express.js**: Powers the Review Service backend for rapid I/O handling.
- **Prisma ORM & PostgreSQL**: Ensures ACID compliance and structured transactional review storage.
- **AWS ECS (Fargate) & ALB**: Provides containerized, multi-AZ scalability and high availability.
- **Amazon ElastiCache (Redis)**: Accelerates read performance and enforces API rate limiting.
- **AWS EventBridge**: Decouples services asynchronously to protect system availability.

## Rationale
This decoupled, event-driven architecture ensures 99.95% uptime and rapid page loads under high traffic by utilizing Redis caching and asynchronous AWS EventBridge communication. Furthermore, strict JWT authentication, AWS Secrets Manager, and GDPR-compliant data anonymization meet rigorous security and regulatory requirements.