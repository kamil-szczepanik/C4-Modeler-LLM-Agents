## Overview
The Online Bookstore is a multi-region e-commerce platform providing catalogue browsing, secure checkout, reviews, and personalized recommendations for 1 million monthly active users. It runs on AWS across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to deliver high availability and regulatory compliance.

## Key Elements
- Book Shopper, Reviewer, Store Administrator
- Web Frontend, Admin Portal (React SPA)
- Amazon API Gateway
- Catalogue Service (Node.js / Express), Order and Checkout Service (Go), Review Service (Python / FastAPI), Admin Service (Node.js / Express), Recommendation Integration Service (Node.js)
- Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon OpenSearch
- Payment Gateway, Third-Party Shipping APIs, Identity Provider, Email Service (Amazon SES), ML Recommendation Engine (Amazon Personalize)

## Relationships
- Book Shopper / Reviewer / Store Administrator -> Web Frontend / Admin Portal via HTTPS (CloudFront)
- Web Frontend / Admin Portal -> Amazon API Gateway via HTTPS/REST (JWT validation)
- Amazon API Gateway -> Microservices via HTTPS/REST
- Order and Checkout Service -> Payment Gateway via HTTPS/REST
- Order and Checkout Service -> Third-Party Shipping APIs via HTTPS/REST and Webhooks
- Microservices -> Amazon Aurora PostgreSQL via PostgreSQL Wire Protocol over TLS (TCP)
- Microservices -> Amazon DynamoDB / Amazon OpenSearch via TCP

## Technology Stack
- React: Powers responsive single-page web applications for customers and administrators.
- Go: Chosen for high-throughput, concurrent transaction handling in the Order and Checkout Service.
- Node.js & Python (FastAPI): Powers flexible microservices for catalogue, reviews, and administration.
- Amazon Aurora PostgreSQL: Provides multi-region relational persistence with global replication and high availability.
- Amazon DynamoDB: Delivers low-latency storage for user shopping carts and active sessions.
- Amazon OpenSearch: Enables sub-second keyword search capabilities for the book catalogue.
- AWS (CloudFront, API Gateway, SQS/SNS, SES): Delivers scalable cloud infrastructure, edge caching, and messaging.

## Rationale
This architecture uses cloud-native managed services and polyglot microservices to scale efficiently for 1 million monthly active users while ensuring sub-2-second page loads. Strict data governance, encryption, and multi-region deployment guarantee 99.95% uptime and full GDPR/CCPA compliance.