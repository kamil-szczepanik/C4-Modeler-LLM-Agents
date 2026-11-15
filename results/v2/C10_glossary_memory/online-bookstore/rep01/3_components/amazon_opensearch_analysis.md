## Overview
The Online Bookstore system is a multi-region e-commerce platform providing catalogue browsing, secure checkout, reviews, and personalized recommendations for 1 million monthly active users. It ensures high performance, multi-currency support, and GDPR compliance on AWS.

## Key Elements
- Book Shopper [person]
- Reviewer [person]
- Store Administrator [person]
- Web Frontend (React SPA) [container]
- Admin Portal (React SPA) [container]
- Amazon API Gateway [container]
- Catalogue Service (Node.js / Express) [container]
- Order and Checkout Service (Go) [container]
- Review Service (Python / FastAPI) [container]
- Admin Service (Node.js / Express) [container]
- Recommendation Integration Service (Node.js) [container]
- Amazon Aurora PostgreSQL [container]
- Amazon DynamoDB [container]
- Amazon OpenSearch (Search Index Engine, Ingestion & Indexing Pipeline, Cluster Management & Security) [container]
- Payment Gateway [externalSystem]
- Third-Party Shipping APIs [externalSystem]
- Identity Provider (Auth0 / AWS Cognito) [externalSystem]
- Email Service (Amazon SES) [externalSystem]
- ML Recommendation Engine (Amazon Personalize) [externalSystem]

## Relationships
- Book Shopper -> Web Frontend (HTTPS via AWS CloudFront)
- Store Administrator -> Admin Portal (HTTPS via AWS CloudFront)
- Web Frontend -> Amazon API Gateway (HTTPS/REST with JWT validation)
- Admin Portal -> Amazon API Gateway (HTTPS/REST with JWT validation)
- Amazon API Gateway -> Catalogue Service (HTTPS/REST with JWT validation)
- Amazon API Gateway -> Order and Checkout Service (HTTPS/REST with JWT validation)
- Order and Checkout Service -> Payment Gateway (HTTPS/REST)
- Order and Checkout Service -> Third-Party Shipping APIs (HTTPS/REST and Webhooks)
- Catalogue Service -> Amazon Aurora PostgreSQL (TCP)
- Catalogue Service -> Amazon OpenSearch (HTTPS/REST with SigV4)
- Admin Service -> Amazon OpenSearch (HTTPS/REST with SigV4)
- Recommendation Integration Service -> ML Recommendation Engine (HTTPS/REST and Asynchronous SQS/SNS)

## Technology Stack
- React SPA: Provides responsive customer and administrative user interfaces.
- Go & Node.js / Express / Python FastAPI: Ensures fast, scalable microservice execution.
- Amazon Aurora PostgreSQL: Multi-region relational storage for persistent application data.
- Amazon DynamoDB: Low-latency storage for user shopping carts and active sessions.
- Amazon OpenSearch: Delivers sub-second full-text and faceted search.
- AWS CloudFront & API Gateway: Secures ingress and routes traffic globally.

## Rationale
This architecture uses decoupled microservices and managed AWS data stores to guarantee sub-second page loads and 99.95% availability under high traffic. Strict regional isolation, IAM integration, and encryption mechanisms ensure robust scalability while satisfying GDPR and CCPA security constraints.