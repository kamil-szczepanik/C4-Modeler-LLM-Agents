## Overview
The Online Bookstore is a globally distributed, cloud-hosted e-commerce platform designed to support book purchasing, reviews, and recommendations. Its core purpose is to deliver a high-performance shopping experience with robust scalability and multi-region availability.

## Key Elements
* **Actors**: Customer (Web/Mobile User), Admin/Content Manager.
* **External Systems**: Payment Gateway (Stripe/PayPal), Third-Party Shipping API (FedEx/UPS), Email/Notification Service (SES/SendGrid), External Identity Provider (AWS Cognito/Auth0), Tax Calculation Service (Avalara/TaxJar).
* **Containers**: Frontend SPA (React on AWS CloudFront/S3), API Gateway (AWS API Gateway), Catalogue & Search Service (Node.js/Go with Amazon OpenSearch), Checkout & Order Service (Java/Spring Boot), Recommendation Service (Python/FastAPI), Async Worker (AWS Lambda/ECS Fargate).
* **Data & Messaging**: Amazon Aurora Global Database, Amazon ElastiCache (Redis), Amazon DynamoDB, Amazon SQS/SNS.

## Relationships
* **Customer -> Frontend SPA**: Browses and interacts via HTTPS.
* **Frontend SPA -> API Gateway**: Sends requests via REST/gRPC over TLS.
* **API Gateway -> Core Containers**: Routes traffic using REST/gRPC over TLS, validating tokens with AWS Cognito.
* **Checkout & Order Service -> Amazon Aurora Global Database**: Executes ACID transactions via JDBC over TLS.
* **Catalogue Service -> Amazon ElastiCache**: Retrieves cached data via Redis Protocol over TLS.
* **Checkout Service -> Amazon SQS**: Publishes order events asynchronously.
* **Async Worker -> Third-Party Shipping API & Notification Service**: Integrates via REST/HTTPS for fulfillment and alerts.

## Technology Stack
* **Cloud Infrastructure**: AWS across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to ensure high availability and global reach.
* **Frontend**: React and AWS CloudFront/S3 for rapid content delivery and performance.
* **Backend Services**: Polyglot microservices (Node.js/Go, Java/Spring Boot, Python/FastAPI) mapped to specific domain requirements.
* **Databases & Caching**: Amazon Aurora Global Database for financial consistency, Amazon DynamoDB and OpenSearch for catalogue/recommendations, and Redis for low-latency caching.
* **Integration & Messaging**: Amazon SQS/SNS for decoupled event-driven workflows.

## Rationale
This architecture leverages multi-region AWS services and asynchronous workers to meet stringent 99.95% uptime and 1M MAU scalability targets while maintaining sub-second page loads. Polyglot microservices and managed global databases ensure optimal performance, multi-currency support, and strict GDPR/CCPA compliance.