## Overview
- Online Bookstore is a scaled-down Amazon-style e-commerce site for books featuring search, cart/checkout, reviews, and recommendations.
- Core purpose is delivering a scalable, multi-region retail platform meeting stringent availability, performance, and compliance standards.

## Key Elements
- **Users**: Customer, Admin/Content Manager
- **External Systems**: Payment Gateway, Third-Party Shipping API, Email/Notification Service, External Identity Provider, Tax Calculation Service
- **Containers**: AWS Route 53 & Amazon CloudFront, Frontend SPA (React), BFF Container (Next.js), AWS API Gateway, Compliance/Audit Lambda, Core E-Commerce Service (Spring Boot), Recommendation Engine (FastAPI), Search & Discovery (Amazon OpenSearch), Notification Worker, Amazon Aurora Global Database (PostgreSQL), Amazon DynamoDB, Amazon ElastiCache (Redis), Amazon MSK (Kafka), AWS Glue & Athena
- **Amazon DynamoDB Components**: Request Router / API Frontend, Partition Router / Storage Nodes, Replication Engine, DAX Service Node, Global Table Replicator, Streams Worker, Time-to-Live (TTL) Background Worker

## Relationships
- Core E-Commerce Service -> Amazon DynamoDB (DAX Service Node): Low-latency cache and NoSQL data access [TCP / TLS, AWS SigV4]
- Recommendation Engine -> Amazon DynamoDB (DAX Service Node): Fetches reviews and ratings [TCP / TLS, AWS SigV4]
- Partition Router -> Replication Engine & Global Table Replicator: Multi-AZ and cross-region replication [Internal AWS replication protocol over TLS]
- Streams Worker -> Compliance/Audit Lambda: Publishes change data capture events [HTTPS / TLS 1.3, IAM]

## Technology Stack
- **Cloud Provider**: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region global availability
- **Database**: Amazon DynamoDB with DAX for high-throughput, microsecond-latency NoSQL operations and session caching
- **Backend Services**: Spring Boot (Java) for Core E-Commerce, FastAPI (Python) for Recommendation Engine, Next.js/Node.js for BFF
- **Messaging & Streaming**: Amazon MSK (Apache Kafka) and DynamoDB Streams for event-driven workflows

## Rationale
- The architecture uses managed AWS infrastructure and multi-region replication to easily scale to 1M MAU while guaranteeing 99.95% uptime.
- In-memory caching via DAX and OpenSearch ensure fast page loads under 2 seconds even on constrained networks.