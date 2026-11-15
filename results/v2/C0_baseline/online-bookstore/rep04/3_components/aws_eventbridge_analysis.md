## Overview
[An asynchronous, event-driven e-commerce platform built on AWS, designed to handle 1M MAU with 99.95% availability while supporting catalog browsing, secure checkout, and personalized recommendations.]

## Key Elements
- [Book Buyer / Customer, Registered Reviewer, Store Administrator / Content Manager]
- [React / TypeScript SPA, AWS API Gateway, Order & Catalog Services, Recommendations Service, Review Service]
- [Amazon RDS PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis)]
- [Custom Event Buses, Event Rules, Target Dispatchers, AWS SQS Buffers, AWS SQS DLQs]
- [Stripe / PayPal, FedEx / UPS, Auth0 / AWS Cognito, AWS SES, Currency Exchange Rate Service]

## Relationships
- [React SPA -> AWS API Gateway: HTTPS / REST API calls]
- [Microservices -> Custom Event Buses: Asynchronous event publishing via PutEvents API]
- [Custom Event Buses -> Event Rules -> Target Dispatchers: Internal event routing]
- [Target Dispatchers -> AWS SQS Shipping Buffers & DLQs: Asynchronous message queuing via HTTPS]
- [AWS SQS Buffers -> Third-party Shipping APIs: Outbound fulfillment integration via HTTPS / OAuth 2.0]

## Technology Stack
- [AWS EventBridge: Custom event buses for decoupled microservice communication]
- [AWS SQS & DLQs: Message buffering and failure isolation for reliable event delivery]
- [AWS KMS: Customer Managed Keys for encryption at rest to ensure GDPR and CCPA compliance]
- [AWS Secrets Manager: Secure storage for OAuth 2.0 and API credentials]

## Rationale
[Domain-isolated event buses prevent cascading failures, safeguarding the 99.95% uptime requirement for checkout flows. SQS buffering and encryption mechanisms guarantee secure, resilient data processing and strict regulatory compliance under peak load.]