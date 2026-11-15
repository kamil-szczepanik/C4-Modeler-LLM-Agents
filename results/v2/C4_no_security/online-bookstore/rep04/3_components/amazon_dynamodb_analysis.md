## Overview
The Online Bookstore system uses Amazon DynamoDB as a high-performance NoSQL data layer to manage ephemeral state, promotional metadata, and user activity. It supports 1 million monthly active users with sub-second latency while ensuring GDPR and CCPA compliance.

## Key Elements
* Shopping Cart Table (AWS DynamoDB Table)
* Promotions & Deals Table (AWS DynamoDB Table)
* User Activity Stream Table (AWS DynamoDB Table with DynamoDB Streams)
* Order & Checkout Service (Amazon ECS/Fargate)
* Catalog Service (Amazon ECS/Fargate)
* Recommendation Worker (Amazon ECS/Fargate)

## Relationships
* Order & Checkout Service -> Shopping Cart Table: Reads/writes ephemeral cart data via AWS SDK [HTTPS / IAM]
* Catalog Service -> Promotions & Deals Table: Reads promotional metadata via AWS SDK [HTTPS / IAM]
* User Activity Stream Table -> Recommendation Worker: Streams browse history via AWS SDK [HTTPS]

## Technology Stack
* Amazon DynamoDB: Selected for single-digit millisecond latency and high scalability.
* DynamoDB Global Tables: Deployed across `us-east-1`, `eu-west-1`, and `ap-southeast-1` for multi-region resilience and low-latency access.
* DynamoDB Streams: Enables asynchronous event-driven consumption for recommendations.
* Time-To-Live (TTL): Automates data hygiene to enforce GDPR/CCPA data minimization.
* Auto-Scaling & On-Demand Capacity: Handles unpredictable flash sales and traffic spikes.

## Rationale
This architecture meets 99.95% availability and sub-2-second performance requirements by isolating high-frequency ephemeral data into a managed NoSQL store. It guarantees regulatory compliance and cross-region resilience for a global e-commerce user base.