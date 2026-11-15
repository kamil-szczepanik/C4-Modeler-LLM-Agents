## Overview
• An Amazon-style online bookstore providing catalog browsing, secure checkout, reviews, and recommendations for 1M MAU.
• Designed for high availability (99.95% uptime) across three AWS regions while enforcing GDPR, CCPA, and PCI-DSS compliance.

## Key Elements
• Shopper, Registered Customer, Site Administrator, and Business Analyst
• React/TypeScript Single Page Application (SPA)
• AWS API Gateway
• Catalog & Search Container (Go/gRPC, Amazon OpenSearch, Aurora PostgreSQL)
• Order & Checkout Container (Node.js/Spring Boot, isolated Aurora PostgreSQL cluster)
• Recommendation Engine (Python/FastAPI)
• Customer Reviews & Ratings Container (Python/FastAPI, Amazon DynamoDB)
• External Payment Gateway and Third-Party Shipping APIs

## Relationships
• SPA interacts with API Gateway via HTTPS/JSON
• API Gateway routes requests to internal containers via gRPC over mTLS
• Order & Checkout container communicates with Payment Gateway and Shipping APIs via HTTPS/REST
• Recommendation Engine asynchronously consumes order events

## Technology Stack
• AWS ECS with Fargate for scalable container orchestration
• Amazon CloudFront and S3 for global static asset delivery
• Amazon Aurora PostgreSQL and DynamoDB for persistent storage
• AWS WAF and AWS Secrets Manager for security and compliance

## Rationale
• Microservices and managed AWS services ensure scalability to 1M MAU while meeting the <2s page load SLA on 3G.
• Strict network isolation and IAM least-privilege boundaries protect sensitive PII and isolate PCI-DSS scope.