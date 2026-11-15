## Overview
The Online Bookstore is a scaled-down e-commerce system for purchasing physical and electronic books with integrated recommendations and reviews. It provides a secure, high-performance retail platform supporting global users across multiple AWS regions.

## Key Elements
- **Customer:** End-user browsing and purchasing books via the SPA.
- **Single Page Application (SPA):** React and TypeScript hosted on Amazon S3 and distributed via Amazon CloudFront.
- **API Gateway:** AWS API Gateway routing client requests.
- **Containers:** Catalog & Search (Spring Boot, Amazon SageMaker), Order & Checkout (Node.js / Express), Recommendations (Python / FastAPI), Notification Service (Go).
- **Storage Components:** Amazon Aurora PostgreSQL Multi-Region, Amazon DynamoDB Global Tables, and Amazon ElastiCache for Redis.
- **External Systems:** Third-Party Payment Gateway, Third-Party Shipping Provider, Identity Provider, Currency Exchange Rate Service.

## Relationships
- Customer -> SPA: Browses and interacts via HTTPS.
- SPA -> API Gateway: REST/GraphQL API calls over HTTPS/TLS.
- Catalog & Search Container -> Catalog & User Relational DB: Queries structured book/review data [JDBC/SQL over TLS].
- Order & Checkout Container -> Cart & Session NoSQL Store: Reads/writes cart data [AWS SDK / HTTPS].
- Catalog & Search / Order & Checkout -> Cache Store: Reads cached data and session tokens [Redis Wire Protocol over TLS].
- System -> Third-Party Payment Gateway & Shipping Provider: Integrates via REST APIs over TLS.

## Technology Stack
- **Frontend:** React and TypeScript for responsive client-side rendering.
- **Backend Services:** Spring Boot, Node.js/Express, Python/FastAPI, and Go for microservice containers.
- **Databases:** Amazon Aurora PostgreSQL for ACID transactions and structured catalog data; Amazon DynamoDB Global Tables for low-latency shopping carts and sessions.
- **Caching:** Amazon ElastiCache for Redis for in-memory session and catalog caching.
- **Infrastructure:** AWS (us-east-1, eu-west-1, ap-southeast-1) using Amazon S3, CloudFront, API Gateway, EventBridge, and MSK.

## Rationale
This multi-region AWS architecture ensures 99.95% uptime and sub-2-second page loads for 1M monthly active users. Aurora PostgreSQL provides ACID compliance for financial orders, while DynamoDB and ElastiCache deliver the sub-10ms latency required for carts, sessions, and catalog browsing.