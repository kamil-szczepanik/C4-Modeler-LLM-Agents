## Overview
- Scaled-down Amazon-style e-commerce site for physical and electronic books with recommendations and reviews.
- Built on AWS to support 1 million MAU, multi-currency transactions, and strict GDPR/CCPA compliance.

## Key Elements
- Users: Guest Shopper, Registered Customer, Store Administrator, Customer Support Agent
- Frontend: React, TypeScript, Amazon CloudFront, Amazon S3
- API Management: Amazon API Gateway
- Microservices: Catalog & Search (Java, Spring Boot), Checkout & Order (Node.js), Recommendation (Python, FastAPI), Analytics Ingestion (Go)
- Database: Amazon RDS (PostgreSQL) with PgBouncer connection pooler
- Messaging/Events: AWS SQS, Amazon EventBridge, Amazon Kinesis
- External: Payment Gateway, Shipping Provider API, Tax/Compliance Service

## Relationships
- Frontend -> Amazon API Gateway: HTTPS/REST/GraphQL
- Catalog & Search -> Amazon RDS (PostgreSQL): TLS-encrypted JDBC/TCP
- Checkout & Order -> Amazon RDS (PostgreSQL): TLS-encrypted JDBC/TCP
- Checkout & Order -> AWS EventBridge / SQS: Asynchronous messaging
- Analytics Ingestion -> Amazon Kinesis: Data streaming

## Technology Stack
- Frontend: React, TypeScript, Amazon CloudFront, S3 for global edge delivery
- Compute: AWS containerized microservices (Java/Spring Boot, Node.js, Python, Go)
- Database: Amazon RDS (PostgreSQL) with PgBouncer, Multi-AZ replication, and cross-region read replicas
- Messaging: AWS SQS and Amazon EventBridge for asynchronous decoupled workflows

## Rationale
- Microservices combined with Amazon RDS (PostgreSQL) ensure ACID compliance for orders while scaling independently to handle 1M MAU.
- Multi-region read replicas and global CDN distribution meet sub-2-second page load performance and 99.95% availability targets.