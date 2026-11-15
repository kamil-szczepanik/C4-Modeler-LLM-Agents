## Overview
The Online Bookstore is a scaled-down, multi-region e-commerce platform designed for browsing catalogues, secure checkout, reviews, and personalized recommendations. It delivers high scalability, strict data security, and sub-2-second performance for global customers.

## Key Elements
- **Users**: Customers
- **External Systems**: Stripe/PayPal, FedEx/UPS, Auth0/AWS Cognito, SendGrid/AWS SES, Avalara/TaxJar
- **Containers**: Single Page Application (React, TypeScript), API Gateway (AWS API Gateway), Catalog Service (Node.js, Express), Order & Checkout Service (Spring Boot), Recommendation Service (Python, FastAPI), Review & Notification Service, Message Broker (Amazon SNS/SQS), Aurora PostgreSQL Database, OpenSearch Service, Redis Cache (Amazon ElastiCache for Redis)
- **Redis Cache Components**: Session Store, Shopping Cart Store, Catalogue Cache, Rate Limiting Store, Redis Persistence & Eviction Manager, Redis Key Namespace & TTL Policy Manager, Redis Telemetry & Metrics Exporter

## Relationships
- **Customer -> Single Page Application**: Browses catalogue and manages cart [HTTPS]
- **Single Page Application -> API Gateway**: Sends API requests [HTTPS/REST]
- **API Gateway -> Session Store Component**: Validates user sessions [Redis RESP]
- **API Gateway -> Rate Limiting Store Component**: Checks request counters [Redis RESP]
- **Catalog Service -> Catalogue Cache Component**: Reads/writes product data [Redis RESP]
- **Order & Checkout Service -> Shopping Cart Store Component**: Persists cart state [Redis RESP]
- **Recommendation Service -> Catalogue Cache Component**: Reads product recommendations [Redis RESP]
- **Redis Telemetry & Metrics Exporter -> Amazon CloudWatch**: Publishes operational metrics [AWS CloudWatch API]

## Technology Stack
- **Frontend**: React, TypeScript (hosted on Amazon S3, delivered via Amazon CloudFront) for a responsive client-side experience.
- **Backend Services**: Node.js/Express, Spring Boot, Python/FastAPI for scalable microservices.
- **Database & Search**: Amazon Aurora PostgreSQL for reliable relational data; Amazon OpenSearch Service for fast catalogue keyword search.
- **Caching & State**: Amazon ElastiCache for Redis with cluster mode, AOF snapshots, and `volatile-lru` eviction for high-performance session, cart, and rate-limiting data.
- **Infrastructure**: AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) ensuring global multi-region availability.

## Rationale
This architecture uses decoupled microservices deployed across multiple AWS regions to easily scale to 1M MAU while maintaining 99.95% uptime. Integrating Amazon ElastiCache for Redis guarantees sub-millisecond data retrieval to achieve sub-2-second page loads even under heavy retail traffic.