## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce site designed for purchasing physical and electronic books with recommendations and reviews. The system uses a microservices architecture deployed on AWS across multiple global regions to ensure high availability, low latency, and regulatory compliance.

## Key Elements
- **Customers**: End-users browsing catalogues and purchasing books.
- **Client Tier**: React SPA hosted on Amazon S3 and distributed via Amazon CloudFront.
- **API Tier**: AWS API Gateway with Lambda Authorizer.
- **Microservices**: Catalog Service (Node.js/Express), Order & Checkout Service (Spring Boot), Recommendation Service (Python/FastAPI), Review & Notification Service (Node.js).
- **Data Tier**: Amazon Aurora PostgreSQL Database, Amazon OpenSearch Service, and Amazon Redis Cache.
- **Message Broker**: Amazon SNS and Amazon SQS.
- **External Systems**: Stripe/PayPal, FedEx/UPS, Auth0/AWS Cognito, SendGrid/AWS SES, Avalara/TaxJar.

## Relationships
- **Customer -> Amazon CloudFront**: HTTPS browsing and checkout requests.
- **SPA -> AWS API Gateway**: RESTful API calls using HTTPS/JSON.
- **API Gateway -> Microservices**: Internal service routing via HTTP/REST and AMQP.
- **Microservices -> Amazon Aurora PostgreSQL**: Database reads and writes using native TCP/TLS (PostgreSQL wire protocol) via Amazon RDS Proxy.
- **Microservices -> External APIs**: Payment, shipping, tax, and auth integrations via HTTPS/REST.

## Technology Stack
- **Frontend**: React and TypeScript for a responsive Single Page Application.
- **Backend**: Node.js/Express, Spring Boot, and Python/FastAPI for microservice modularity.
- **Database**: Amazon Aurora PostgreSQL with schema-per-service isolation (`catalog_db`, `order_db`, `review_db`) and `pg_trgm` extension for search.
- **Caching & Search**: Amazon Redis Cache for sessions and Amazon OpenSearch Service for keyword search.
- **Cloud Infrastructure**: AWS multi-region deployment (`us-east-1`, `eu-west-1`, `ap-southeast-1`) utilizing AWS KMS, AWS Secrets Manager, and RDS IAM Authentication for security and compliance.

## Rationale
This architecture uses a database-per-service pattern within a managed Aurora cluster to enforce strict GDPR/CCPA data boundaries while maintaining 99.95% availability. Utilizing serverless integration services, multi-region replication, and managed caching ensures scalability to 1M MAU and fast page loads under 2 seconds.