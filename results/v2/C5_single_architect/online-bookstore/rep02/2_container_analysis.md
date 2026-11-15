## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform enabling customers to purchase physical and electronic books, read reviews, and receive recommendations. It is designed to handle 1 million MAU globally with high availability and security on AWS.

## Key Elements
* **Customer & Store Administrator**: Primary users interacting with the platform.
* **Single Page Application (SPA)**: React frontend hosted in Amazon S3 and distributed via Amazon CloudFront.
* **API Gateway**: Amazon API Gateway managing routing, SSL termination, and rate limiting.
* **Core Services (Containers)**: Catalog Service (Go), Order & Checkout Service (Node.js), Recommendation Service (Python/FastAPI), and Customer Review Service (Node.js).
* **Databases & Caching**: Amazon Aurora (PostgreSQL), Amazon OpenSearch, Amazon DocumentDB, and Amazon ElastiCache (Redis).
* **Message Broker**: Amazon SQS / SNS for asynchronous decoupling.
* **External Systems**: Payment Gateway, Third-Party Shipping API, Notification Service, OAuth 2.0 Identity Provider, and Currency Exchange Rate Service.

## Relationships
* **Customer to SPA**: HTTPS / REST / GraphQL for user interactions.
* **SPA to API Gateway**: HTTPS / JSON for client requests.
* **API Gateway to Core Services**: HTTPS / REST / gRPC for routed traffic.
* **Order & Checkout Service to External APIs**: HTTPS to Payment Gateway and Third-Party Shipping API.
* **Internal Services to Message Broker**: Amazon SQS / SNS for asynchronous event publishing.

## Technology Stack
* **AWS**: Multi-region cloud provider (us-east-1, eu-west-1, ap-southeast-1) ensuring 99.95% availability (R-07).
* **React & TypeScript**: Frontend SPA cached globally via Amazon CloudFront to ensure page loads under 2 seconds on 3G (R-06).
* **Go & Node.js & Python**: Backend container runtimes chosen for performance and developer velocity.
* **gRPC**: Internal service-to-service communication protocol for low-latency operations.
* **Amazon Aurora PostgreSQL**: Relational database ensuring ACID compliance for transactions.
* **Amazon ElastiCache (Redis)**: Low-latency caching for shopping carts to meet performance constraints.
* **Amazon OpenSearch**: Dedicated search engine powering keyword catalogue browsing (R-01).

## Rationale
This container architecture uses decoupled microservices deployed on AWS to scale seamlessly past 1 million MAU while enforcing strict security and compliance. Specialized datastores and caching layers ensure fast response times globally under constrained network conditions.