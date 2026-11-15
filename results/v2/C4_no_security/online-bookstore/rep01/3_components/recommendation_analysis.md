## Overview
The Online Bookstore system is a scalable e-commerce platform designed to provide catalogue browsing, secure checkout, 5-star reviews, and personalized product recommendations. It ensures high availability, strict regulatory compliance, and multi-currency support across global AWS regions.

## Key Elements
- **Users**: Guest Shopper, Registered Customer, Store Administrator, Customer Support Agent.
- **Containers**: Frontend Container (React, TypeScript), API Management (Amazon API Gateway), Recommendation (Python, FastAPI), Checkout & Order (Node.js).
- **Recommendation Components**: Recommendation API Controller, Algorithm Engine, Model Cache, Event Publisher, Event Consumer.
- **External Systems**: Payment Gateway, Shipping Provider API, Amazon DynamoDB, AWS SQS, AWS EventBridge.

## Relationships
- API Management -> Recommendation: Routes recommendation requests with rate limiting and JWT validation [HTTPS / JSON]
- Recommendation API Controller -> Algorithm Engine: Executes similarity logic [In-process]
- Algorithm Engine -> Model Cache: Fetches pre-computed scores [Redis Protocol / TCP]
- Algorithm Engine -> Amazon DynamoDB: Falls back for deep item similarity graphs on cache misses [HTTPS / boto3]
- Event Publisher -> AWS EventBridge: Emits telemetry events [HTTPS / AWS SDK]
- AWS SQS -> Event Consumer: Polls asynchronous domain events [AWS SQS Protocol]
- Event Consumer -> Model Cache: Invalidates or updates cached scores [Redis Protocol / TCP]

## Technology Stack
- **Python & FastAPI**: Powers the Recommendation service for rapid asynchronous request handling.
- **Amazon ElastiCache Global Datastore (Redis)**: Delivers sub-2s response times and multi-region cache availability.
- **Amazon DynamoDB**: Stores persistent item similarity graphs for fallback queries.
- **AWS ECS with Fargate**: Manages containerized microservice deployments with auto-scaling.
- **AWS SQS & EventBridge**: Handles asynchronous messaging, telemetry events, and cache invalidation.

## Rationale
This architecture uses an asynchronous event-driven pattern and in-memory caching to guarantee sub-second recommendations without blocking core rendering. The decoupled Fargate and ElastiCache design ensures high availability, fault tolerance, and seamless scalability to meet global performance targets.