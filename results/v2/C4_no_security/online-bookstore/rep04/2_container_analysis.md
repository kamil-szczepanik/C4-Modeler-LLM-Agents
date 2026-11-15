## Overview
- An Amazon-style online bookstore system enabling global book discovery, secure checkout, multi-currency purchasing, and personalized recommendations.
- Built to support 1 million monthly active users (MAU) with high availability and GDPR/CCPA compliance across three global AWS regions.

## Key Elements
- **Users**: Shopper, Customer Support Agent, Catalog Manager / Administrator, Compliance Officer.
- **Client Container**: Single Page Application (SPA) built with React/TypeScript.
- **Gateway & Edge**: AWS API Gateway, AWS CloudFront, Amazon S3, AWS Route 53.
- **Backend Services**: Amazon ECS/Fargate microservices (Catalog Service, Order & Checkout Service, User & Compliance Service, Notification Service, Recommendation Worker).
- **Data & Caching**: Amazon RDS PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis).
- **Messaging**: AWS SQS/SNS with Dead-Letter Queues (DLQs).
- **External Systems**: Payment Gateway, Shipping Provider APIs, Identity Provider, Third-Party Recommendation Engine.

## Relationships
- Shoppers and Administrators access the React SPA via HTTPS through AWS CloudFront and Amazon S3.
- SPA communicates with AWS API Gateway using HTTPS and REST/GraphQL.
- API Gateway routes requests to ECS/Fargate microservices via gRPC over TLS within private VPC subnets.
- Order & Checkout Service integrates with external Payment Gateway and Shipping Provider APIs.
- Backend services persist state in Amazon RDS PostgreSQL and Amazon DynamoDB, utilizing Amazon ElastiCache (Redis) for caching.
- Recommendation Worker and Notification Service consume events asynchronously via AWS SQS/SNS.

## Technology Stack
- **Frontend**: React and TypeScript hosted on Amazon S3 and distributed via AWS CloudFront for low-latency global delivery.
- **Backend**: Spring Boot and Node.js microservices running on Amazon ECS/Fargate for minimal operational overhead and auto-scaling.
- **Databases**: Amazon RDS PostgreSQL with cross-region read replicas and geo-partitioning; Amazon DynamoDB for low-latency promotional data.
- **Caching**: Amazon ElastiCache (Redis) to absorb read spikes and protect primary databases.
- **Messaging**: AWS SQS and SNS with DLQs for asynchronous processing and decoupling.
- **Cloud Provider**: AWS deployed across us-east-1, eu-west-1, and ap-southeast-1 regions with AWS X-Ray for distributed tracing.

## Rationale
- Containerized microservices on Amazon ECS/Fargate combined with Redis caching and global CDN distribution ensure sub-2-second page loads and 99.95% availability for 1M MAU.
- Geo-partitioned PostgreSQL databases and isolated compliance services strictly enforce GDPR and CCPA regulatory requirements across multiple AWS regions.