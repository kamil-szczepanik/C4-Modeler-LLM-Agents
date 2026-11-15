## Overview
- Online Bookstore is a scaled-down Amazon-style e-commerce site for purchasing physical and electronic books with recommendations and reviews.
- The system provides high scalability, multi-region availability, and strict compliance for global retail operations.

## Key Elements
- Customers and Store Administrators
- Amazon API Gateway and React/TypeScript SPA
- ECS Fargate Microservices: Catalog Service, Order & Checkout Service, Recommendation Service, Auth Service, Privacy Service, Background Worker
- Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon OpenSearch, Amazon S3, Amazon CloudFront
- AWS RDS Proxy, Primary DB Instance, Replica DB Instances, Aurora Storage Volume, PostgreSQL Extension Manager (`pgAudit`, `pgcrypto`)
- Integration Services: Payment Gateway, Shipping Provider APIs, Identity Provider, Tax Calculation Service, Notification Service, Amazon SNS/SQS, Amazon CloudWatch, AWS X-Ray

## Relationships
- Customer -> SPA: Browses and interacts [HTTPS / TLS 1.3]
- SPA -> Amazon API Gateway: REST/GraphQL API calls [HTTPS / TLS 1.3]
- API Gateway -> ECS Fargate Microservices: Routes requests [Internal HTTP/gRPC]
- Order & Catalog Services -> AWS RDS Proxy: Routes database transactions [PostgreSQL Protocol / TCP/5432]
- RDS Proxy -> Primary / Replica DB Instances: Manages connection pools [PostgreSQL Protocol / TCP/5432]
- Primary DB Instance -> Aurora Storage Volume: Persists data [AWS Aurora Storage Fabric / TCP]

## Technology Stack
- Amazon Aurora PostgreSQL: Managed relational storage for ACID transactions and scalability.
- AWS RDS Proxy: Connection pooling to prevent ECS Fargate connection exhaustion.
- `pgAudit` & `pgcrypto`: Database-level auditing and column-level encryption for GDPR/CCPA compliance.
- ECS Fargate & Amazon API Gateway: Serverless container hosting and API management for 1M MAU scalability.
- AWS (us-east-1, eu-west-1, ap-southeast-1): Multi-region cloud infrastructure for global reach and 99.95% uptime.

## Rationale
- This architecture combines managed AWS services, connection pooling, and multi-AZ database replicas to easily handle 1M MAU with 99.95% uptime.
- Built-in database extensions and distributed storage ensure strict adherence to GDPR, CCPA, and OWASP Top-10 security constraints.