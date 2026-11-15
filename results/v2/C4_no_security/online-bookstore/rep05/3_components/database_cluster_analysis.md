## Overview
The Online Bookstore is a globally scaled e-commerce system providing book catalog browsing, secure checkout, reviews, and recommendations. The architecture leverages AWS multi-region services to ensure high availability, low latency, and regulatory compliance.

## Key Elements
- **Users**: Customer (Shopper), Book Author/Publisher, Store Administrator
- **External Systems**: Payment Gateway, Shipping Provider APIs, Identity Provider, Notification System, Tax Calculation Service
- **Containers**: React SPA, AWS API Gateway, ALB, Node.js Catalog & Search Service, Go/Java Checkout & Order Service, Python FastAPI Recommendation Service, Data Privacy Service, Localization Service, Amazon Aurora PostgreSQL Database Cluster, Amazon DynamoDB Session Cache, Amazon OpenSearch Search Index, Amazon SQS/SNS Messaging Bus
- **Database Components**: Primary Writer Instance, Cross-Region Read Replicas, PgBouncer Connection Pooler, Routing Proxy (Aurora Read-Write Endpoint)

## Relationships
- Checkout & Order Service -> Primary Writer Instance: Write transactions [TCP / TLS, PostgreSQL Wire Protocol]
- Catalog & Search Service -> Cross-Region Read Replicas: Read queries [TCP / TLS, PostgreSQL Wire Protocol]
- Data Privacy Service -> Primary Writer Instance: PII masking and GDPR/CCPA requests [TCP / TLS, PostgreSQL Wire Protocol]
- ECS Fargate Tasks -> Amazon Aurora: Authenticated via AWS Secrets Manager and IAM database authentication

## Technology Stack
- **Database**: Amazon Aurora (PostgreSQL) with Aurora Global Databases for multi-region replication
- **Connection Pooling**: PgBouncer for managing container connection spikes
- **Security & Compliance**: AWS KMS with regionally segregated keys, AWS Secrets Manager for credential rotation
- **Cloud Infrastructure**: AWS us-east-1, eu-west-1, ap-southeast-1 regions with Amazon ECS on Fargate

## Rationale
This architecture satisfies global scalability, performance, and 99.95% uptime requirements through multi-region read replicas and automated failovers. Strict data residency controls, encryption, and read-after-write consistency policies ensure full GDPR and CCPA compliance.