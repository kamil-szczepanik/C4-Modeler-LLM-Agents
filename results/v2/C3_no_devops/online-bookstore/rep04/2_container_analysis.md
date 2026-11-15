## Overview
An Amazon-style online bookstore providing catalog browsing, secure checkout, reviews, and recommendations for 1M MAU. It ensures 99.95% uptime and GDPR/CCPA compliance across multi-region AWS infrastructure.

## Key Elements
* **People:** Customer (Casual Reader, Returning Bibliophile), Store Administrator
* **Frontends:** React Single Page Application (SPA)
* **Gateways & Security:** AWS API Gateway, AWS App Mesh, AWS Secrets Manager, AWS KMS
* **Containers (Microservices):** Catalog & Search, Checkout & Order, Review & Rating, Notification Service, Recommendation
* **Data & Messaging:** Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon OpenSearch, Amazon SQS, Amazon SNS, AWS SES
* **External Systems:** Payment Gateway, Third-Party Shipping/Carrier APIs, Tax Calculation Service, Recommendation Provider, Identity Provider

## Relationships
* Customer (SPA) --(HTTPS/JSON, TLS 1.3)--> AWS API Gateway
* AWS API Gateway --(REST/gRPC with JWT)--> Catalog, Checkout, Reviews, and Recommendation Containers
* Internal Containers --(mTLS via AWS App Mesh)--> Private VPC Network
* Checkout Container --(HTTPS)--> Payment Gateway
* Checkout Container --(AWS SQS)--> Notification Service & Third-Party Shipping APIs
* Notification Service --(AWS SES/SNS)--> Customer

## Technology Stack
* **Frontend:** React hosted on AWS S3 & CloudFront for <2s 3G page loads
* **API Routing:** AWS API Gateway for TLS termination and OAuth2/OIDC token validation
* **Backend Services:** Spring Boot (Catalog), Node.js/Express (Checkout, Notifications), Python/FastAPI (Reviews, Recommendations)
* **Databases:** Amazon Aurora PostgreSQL (transactional order data), Amazon DynamoDB (sessions, catalogs, reviews)
* **Search & Messaging:** Amazon OpenSearch, Amazon SQS, Amazon SNS, AWS SES
* **Security & Cloud:** AWS KMS, AWS Secrets Manager, AWS App Mesh, multi-region AWS (us-east-1, eu-west-1, ap-southeast-1)

## Rationale
Isolating the Checkout container from Recommendation and Review containers protects revenue flow and maintains high availability during peak loads. Decoupled microservices on AWS scale independently to handle 1M MAU while meeting strict performance, OWASP security, and GDPR/CCPA compliance mandates.