## Overview
The Online Bookstore is a globally distributed e-commerce platform built to handle high-volume catalogue searches, secure checkouts, and personalized recommendations for 1 million monthly active users. It delivers reliable retail operations across three international AWS regions while maintaining strict GDPR, CCPA, and OWASP security standards.

## Key Elements
- **Customers**: End-users browsing books, writing reviews, and purchasing items.
- **AWS CloudFront & WAF**: Edge caching and perimeter security layer.
- **Single Page Application (SPA)**: React/TypeScript frontend hosted on AWS S3.
- **API Gateway / ALB**: Ingress routing layer using AWS ALB and API Gateway.
- **Catalog & Search**: ECS Fargate container handling product browsing and queries.
- **Amazon OpenSearch**: Managed search engine container utilizing Apache Lucene.
- **Order & Checkout**: ECS Fargate container with Amazon Aurora PostgreSQL and DynamoDB.
- **Engagement Service**: ECS Fargate container managing reviews and recommendations.
- **Message Bus**: Asynchronous communication via Amazon SQS and SNS.
- **External Integrations**: Third-party Payment Gateways and Shipping APIs.

## Relationships
- `Customer -> AWS CloudFront & WAF`: Accesses frontend application [HTTPS / TLS 1.3]
- `SPA -> API Gateway / ALB`: Sends client requests [HTTPS / REST]
- `Catalog & Search -> Amazon OpenSearch`: Queries and indexes catalogue data [HTTPS / REST via AWS SigV4]
- `Order & Checkout -> Amazon Aurora PostgreSQL`: Reads and writes transactional data [TLS-encrypted TCP via AWS RDS Proxy]
- `Engagement Service -> Amazon S3`: Stores automated database snapshots [AWS SDK / HTTPS]

## Technology Stack
- **Compute**: AWS ECS Fargate for serverless container execution, ensuring rapid horizontal scaling.
- **Database**: Amazon Aurora PostgreSQL for ACID transactions and Amazon DynamoDB for high-throughput shopping carts.
- **Search**: Amazon OpenSearch Service powered by Apache Lucene for low-latency keyword searching.
- **Security & Networking**: AWS WAF, AWS KMS for encryption at rest, and AWS SigV4 for service-to-service authentication.
- **Storage**: Amazon S3 for frontend static assets and automated disaster recovery snapshots.

## Rationale
This architecture leverages managed AWS services across multiple availability zones and regions to guarantee 99.95% uptime and sub-2-second page loads. Decoupling compute, search, and storage ensures robust scalability for 1 million MAU while enforcing strict regional data protection regulations.