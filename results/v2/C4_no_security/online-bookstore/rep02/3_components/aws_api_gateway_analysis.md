## Overview
The Online Bookstore is a globally distributed e-commerce platform built on AWS, designed to handle 1M MAU with 99.95% uptime and sub-2-second page loads. It provides secure catalogue browsing, multi-currency checkout, and personalized book recommendations while ensuring GDPR and CCPA compliance.

## Key Elements
- Book Shopper, Book Author/Publisher, Store Administrator (Users)
- Single Page Application (React / TypeScript on Amazon S3)
- AWS API Gateway (REST / GraphQL, multi-region endpoints)
- Microservices: Catalog & Search, Order & Checkout, Personalization, Customer Review, Notification
- Databases & Caching: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon OpenSearch, Redis (ElastiCache)
- External Systems: Stripe/PayPal, FedEx/UPS, AWS SES, AWS Cognito/Auth0

## Relationships
- Single Page Application -> AWS API Gateway: Sends API requests [HTTPS / REST / GraphQL]
- AWS API Gateway -> Catalog & Search Service: Routes search requests [Internal HTTPS / gRPC]
- AWS API Gateway -> Order & Checkout Service: Routes secure checkout payloads [Internal HTTPS / gRPC]
- AWS API Gateway -> AWS Cognito/Auth0: Validates JWT tokens for authentication [HTTPS]
- Route 53 -> AWS API Gateway: Manages multi-region global failover [DNS / HTTPS]

## Technology Stack
- AWS API Gateway: Manages routing, regional caching, and throttling
- AWS WAF: Mitigates OWASP Top-10 vulnerabilities for security compliance (R-08)
- AWS X-Ray: Enables distributed tracing for latency monitoring (R-06)
- Amazon Aurora PostgreSQL & DynamoDB: Persists transactional and catalog data reliably
- Amazon OpenSearch: Powers fast keyword search for the catalogue

## Rationale
This multi-region, serverless-backed architecture ensures 99.95% uptime and sub-2-second page loads globally via Route 53 failover and API Gateway caching. Microservices isolation scales securely to meet the 1M MAU requirement while maintaining strict transactional integrity.