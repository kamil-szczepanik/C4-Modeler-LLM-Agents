## Overview
The Online Bookstore system is a scalable e-commerce platform providing catalog browsing, secure checkout, 5-star reviews, and personalized book recommendations. It is architected for high availability, compliance, and multi-region performance.

## Key Elements
- **Users**: Customer (Shopper), Book Author/Publisher, Store Administrator
- **External Systems**: Payment Gateway, Third-Party Shipping API, Tax & Compliance Service, Edge Routing & CDN Layer
- **Containers**: Single Page Application (SPA), API Gateway, Catalog & Search Container, Checkout & Order Container, Recommendation Service, Shipping & Payment Integration Worker, Data Stores
- **Data Store Components**: Amazon Aurora PostgreSQL (Primary & Read Replicas), Amazon DynamoDB (Global Tables), Amazon RDS Proxy, AWS Secrets Manager, AWS KMS & CloudTrail

## Relationships
- **SPA -> API Gateway**: HTTPS / REST / GraphQL
- **API Gateway -> Catalog, Checkout & Recommendation Containers**: Internal HTTP / gRPC via AWS VPC Endpoints
- **Containers -> Amazon RDS Proxy / Aurora PostgreSQL**: TLS 1.3 / SQL via IAM Database Authentication
- **Containers -> Amazon DynamoDB**: HTTPS / NoSQL API via AWS PrivateLink
- **Data Stores -> AWS KMS**: API Calls for Encryption/Decryption and CMK Management

## Technology Stack
- **Database (Relational)**: Amazon Aurora PostgreSQL (Multi-AZ / Multi-Region) for ACID transactional data, orders, and reviews.
- **Database (NoSQL)**: Amazon DynamoDB (Global Tables) for ultra-low latency shopping carts, sessions, and recommendation vectors.
- **Connection Pooling**: Amazon RDS Proxy to prevent database connection exhaustion during surges.
- **Security & Compliance**: AWS KMS, AWS Secrets Manager, and Amazon CloudTrail for encryption at rest/transit and audit logging.
- **Deployment Cloud**: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) utilizing Amazon ECS Fargate.

## Rationale
This architecture uses Aurora PostgreSQL and DynamoDB behind RDS Proxy to guarantee low-latency reads, strict GDPR/CCPA compliance, and 99.95% uptime across multiple global regions. Private VPC isolation, IAM authentication, and KMS encryption fulfill stringent security and performance NFRs.