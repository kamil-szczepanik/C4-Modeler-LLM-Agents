## Overview
- The system is an online bookstore providing catalog search, shopping, recommendations, and reviews for global customers.
- Its core purpose is to deliver a scalable, secure, and performant e-commerce experience across AWS regions.

## Key Elements
- Shopper & Store Administrator (Users)
- React Single Page Application (SPA) (React, AWS S3, CloudFront)
- AWS API Gateway
- Catalog & Search Container (Spring Boot, Amazon OpenSearch, Amazon DynamoDB)
- Checkout & Order, Review & Rating, Notification Service, Recommendation containers
- AWS App Mesh & Security (AWS Secrets Manager, AWS KMS)

## Relationships
- AWS API Gateway -> Catalog & Search: Routes catalog and search requests [REST/gRPC with JWT]
- Catalog & Search -> Amazon OpenSearch: Executes full-text search and auto-suggestions [REST]
- Catalog & Search -> Amazon DynamoDB: Retrieves canonical product details and pricing [AWS SDK]
- Catalog & Search -> Recommendation Provider: Blends personalized recommendations [gRPC with mTLS]
- Catalog & Search -> AWS App Mesh & Security: Secures internal microservice communication [mTLS]

## Technology Stack
- Spring Boot: Selected for rapid API development and robust enterprise integration capabilities.
- Amazon OpenSearch: Chosen for high-performance full-text search, auto-suggestions, and faceted filtering.
- Amazon DynamoDB: Deployed for low-latency retrieval of canonical product metadata and pricing.
- AWS App Mesh: Utilized to enforce mTLS and secure internal microservice traffic.

## Rationale
- This architecture guarantees high availability (99.95%) and low-latency performance (<2s page load) to handle 1M MAU globally.
- It enforces strict GDPR/CCPA compliance and OWASP Top-10 security mitigations using AWS-native security controls.