## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform designed to support book browsing, secure checkout, reviews, and personalized recommendations. It ensures high availability, GDPR/CCPA compliance, and multi-currency transactions across a global audience.

## Key Elements
* Customer and Store Administrator
* Single Page App (SPA) container
* API Gateway (Amazon API Gateway)
* Services: Catalog Service (Go), Order & Checkout Service (Node.js), Recommendation Service (Python)
* Databases & Caching: Amazon DynamoDB, Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis)
* External Systems: Payment Gateway, Shipping Provider APIs, Identity Provider (IdP)
* SPA Components: Routing & Shell Component, Catalog & Search View, Cart & Checkout Module, Recommendation & Review Widget, Auth & State Management Client, Client-Side Cache & API Client

## Relationships
* Customer / Administrator -> Single Page App (SPA): Browses catalogue and manages orders [HTTPS via Amazon CloudFront]
* SPA Components -> Client-Side Cache & API Client: Data fetching and state updates [In-memory / Function Calls]
* Client-Side Cache & API Client -> API Gateway: Fetches data and submits orders [HTTPS / REST & GraphQL]
* Auth & State Management Client -> Identity Provider (IdP): User authentication [HTTPS / OIDC]

## Technology Stack
* React & TypeScript: Core SPA framework for type safety and component reusability.
* Amazon CloudFront & S3: Global static asset delivery for < 2s page load times on 3G.
* TanStack Query & Axios: Client-side caching, request deduplication, and optimistic updates.
* React Router: Client-side routing and lazy loading.
* AWS Fargate & ECS: Container orchestration for microservices.
* DynamoDB & Aurora PostgreSQL: Scalable persistent storage.

## Rationale
This architecture uses serverless and containerized AWS services to guarantee 99.95% uptime and scale seamlessly to 1 million MAU. Client-side caching and global CDN distribution directly meet strict performance targets under constrained network conditions.