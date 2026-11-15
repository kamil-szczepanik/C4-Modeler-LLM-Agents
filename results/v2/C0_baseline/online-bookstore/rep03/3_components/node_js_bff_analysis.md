## Overview
An AWS-hosted online bookstore serving 1M MAU with sub-2-second 3G page loads. It utilizes a Node.js Backend for Frontend (BFF) to orchestrate secure, multi-currency microservice interactions.

## Key Elements
- React Single Page App (SPA) via Amazon CloudFront and S3
- Amazon API Gateway and AWS Global Accelerator
- Node.js BFF (Express.js, Apollo Server, AWS ECS Fargate)
- Downstream Services: Checkout Service, Recommendations Service, Notification Service
- Data & Messaging: Amazon Aurora PostgreSQL, Amazon ElastiCache Redis, Amazon DynamoDB, Amazon EventBridge/SQS
- Security & Auth: Auth0/AWS Cognito, AWS Secrets Manager, AWS App Mesh (mTLS)

## Relationships
- React SPA -> Amazon API Gateway: Client requests over `HTTPS`
- API Gateway -> Node.js BFF: Routes requests using `mTLS` and `TLS 1.3`
- Node.js BFF API Router -> GraphQL Federation / Aggregator: Internal routing via `HTTP/2`
- GraphQL Aggregator -> Session & State Manager: Fetches session/cart data via `TCP+TLS`
- GraphQL Aggregator -> Downstream Services: Federated queries with circuit breakers via `gRPC` or `HTTP/2`
- Event Dispatcher -> Amazon EventBridge/SQS: Publishes domain events via `HTTPS`

## Technology Stack
- Node.js & Express.js: Powers the BFF container for rapid asynchronous request handling.
- GraphQL (Apollo Server): Federates data aggregation to minimize client payload sizes and round-trips.
- AWS ECS (Fargate): Container orchestration with auto-scaling to maintain 99.95% uptime.
- Amazon ElastiCache Redis: Low-latency session management via TLS-encrypted connections.
- AWS App Mesh: Enforces internal service-to-service mTLS for zero-trust networking.

## Rationale
This architecture decouples client presentation from backend microservices via a federated Node.js BFF, ensuring strict compliance with global performance SLAs on 3G networks. Furthermore, containerized scaling on AWS Fargate paired with built-in circuit breakers guarantees high availability and fault isolation during peak traffic spikes.