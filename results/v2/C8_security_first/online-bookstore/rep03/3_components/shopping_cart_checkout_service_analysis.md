## Overview
The Online Bookstore system is a scalable global e-commerce platform built on AWS, designed to handle high-volume catalogue browsing, secure checkout, and multi-currency transactions. It ensures 99.95% availability, PCI-DSS compliance, and GDPR/CCPA data privacy across multiple geographic regions.

## Key Elements
* Shopper / Reviewer & Store Administrator (Users)
* Single Page Application (React, TypeScript, Amazon CloudFront, Amazon S3)
* API Gateway & Security (AWS API Gateway, AWS WAF)
* Shopping Cart & Checkout Service (AWS ECS Fargate)
  * Cart Management Component (Node.js/TypeScript)
  * Checkout Orchestrator Component (Node.js/TypeScript)
  * Payment & Shipping Integration Component (Node.js/TypeScript)
  * Currency & Tax Adapter Component (Node.js/TypeScript)
* Supporting Services: Catalogue, Review, Localization & Currency (AWS ECS Fargate)
* Data & Infrastructure: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis), AWS Secrets Manager, AWS SQS, AWS KMS
* External Systems: Payment Gateway, Shipping Provider APIs, Recommendation Engine

## Relationships
* Shopper -> Single Page Application: Browses and checks out [HTTPS via CloudFront]
* API Gateway & Security -> Shopping Cart & Checkout Service: Routes internal traffic [gRPC with mTLS]
* Cart Management Component -> Amazon DynamoDB & Amazon ElastiCache: Persists and caches cart data [Internal VPC Connection]
* Checkout Orchestrator Component -> Amazon Aurora PostgreSQL: Stores transactional orders [Internal VPC Connection]
* Checkout Orchestrator Component -> Amazon SQS: Queues asynchronous fulfillment tasks [Internal AWS API]
* Payment & Shipping Integration Component -> Payment Gateway & Shipping Provider APIs: Processes payments and fulfillment [HTTPS/REST via AWS NAT Gateway]
* Currency & Tax Adapter Component -> Localization & Currency Service: Fetches multi-currency and tax data [gRPC with mTLS]

## Technology Stack
* AWS ECS Fargate: Runs containerized microservices for elastic scalability without server management
* Amazon Aurora PostgreSQL: Provides ACID-compliant relational storage for transactional checkout data
* Amazon DynamoDB & ElastiCache (Redis): Ensures low-latency persistence and session caching for shopping carts
* AWS Secrets Manager & KMS: Manages runtime secrets and encrypts data at rest for security compliance
* AWS App Mesh & SQS: Handles circuit breaking, message queuing, and reliable asynchronous processing

## Rationale
This architecture leverages managed AWS services and decoupled container components to effortlessly scale and meet the 1M MAU and 99.95% availability requirements. Strict security controls, tokenization, and multi-region deployment ensure full PCI-DSS and GDPR compliance while maintaining sub-second performance.