## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform designed to provide a fast, secure, and compliant shopping experience for physical and electronic books. It delivers resilient catalogue browsing, cart management, reviews, and recommendations supporting 1M monthly active users.

## Key Elements
* **Users & External Systems**: Guest/Registered Buyers, Store Administrators, Third-Party Vendors, Stripe/PayPal, FedEx/UPS, AWS SES, AWS Cognito/Auth0.
* **Frontend Container**: React.js Single Page Application hosted on AWS S3 and distributed via CloudFront.
* **API Gateway**: AWS API Gateway performing JWT validation via AWS Cognito and rate limiting.
* **Backend Containers**: Node.js/TypeScript Core E-Commerce, Python/FastAPI Recommendation & Review, and Node.js Tax & Currency containers deployed on Amazon ECS with AWS Fargate.
* **Databases & Caching**: Amazon Aurora PostgreSQL, Amazon DynamoDB, and Amazon ElastiCache Redis clusters (`cache-cart`, `cache-rec`, `cache-limit`).
* **Integration**: Amazon SQS / SNS Event Bus.

## Relationships
* **React.js SPA -> AWS API Gateway**: Routes client requests securely [HTTPS / REST & GraphQL].
* **AWS API Gateway -> Rate Limiter Component (`cache-limit`)**: Evaluates rate-limiting counters [RESP over TLS 1.3].
* **Core E-Commerce Container -> Cart Cache Component (`cache-cart`)**: Persists active shopping sessions and cart state [RESP over TLS 1.3].
* **Recommendation & Review Container -> Recommendation Cache Component (`cache-rec`)**: Reads and writes pre-computed product recommendations [RESP over TLS 1.3].
* **Core E-Commerce Container -> Amazon Aurora PostgreSQL**: Stores transactional order and catalogue data [PostgreSQL Wire Protocol over TLS].

## Technology Stack
* **Cloud Infrastructure**: AWS across `us-east-1`, `eu-west-1`, and `ap-southeast-1` for high availability and regional compliance.
* **Compute**: Amazon ECS with AWS Fargate for serverless container orchestration.
* **Caching & Storage**: Amazon ElastiCache Redis OSS with workload segregation (`noeviction` for carts, `allkeys-lru` for recommendations, `volatile-ttl` for rate limiting) and Amazon Aurora PostgreSQL.
* **Security & Auth**: AWS Cognito, Redis ACLs for least privilege, AWS KMS for encryption-in-transit (TLS 1.3) and at-rest.

## Rationale
This microservices-based architecture uses isolated Amazon ElastiCache Redis components to prevent noisy-neighbor memory exhaustion, protecting checkout resilience and maintaining sub-10ms cache latency. Multi-AZ AWS Fargate deployment and robust data partitioning guarantee 99.95% uptime and OWASP compliance under 1M MAU scale.