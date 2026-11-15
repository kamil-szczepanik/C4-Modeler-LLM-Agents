## Overview
An Amazon-style e-commerce online bookstore for physical and e-books. It handles multi-currency transactions, catalogue search, recommendations, and reviews at a scale of 1M MAU.

## Key Elements
* **Users:** Customer, Admin/Support Staff
* **Core System:** Online Bookstore (React SPA/Mobile App, AWS API Gateway, Core Microservices on AWS ECS Fargate)
* **Databases & Caching:** AWS RDS PostgreSQL, Amazon DynamoDB, Amazon ElastiCache Redis, Amazon OpenSearch
* **Messaging & Security:** Amazon SQS/SNS, AWS Secrets Manager
* **External Systems:** Payment Gateway (Stripe/PayPal), Shipping Provider APIs, Identity Provider (Auth0/Cognito), Notification Service (SES/SendGrid), Recommendation Service (Amazon Personalize), Tax Calculation Service (Avalara/TaxJar)

## Relationships
* Customer uses Online Bookstore via HTTPS
* Online Bookstore calls Payment Gateway, Shipping Provider, Identity Provider, Notification, Recommendation, and Tax Services via HTTPS/REST
* Core Microservices communicate internally via synchronous gRPC/REST and asynchronously via Amazon SQS/SNS

## Technology Stack
* **Frontend:** React / React Native hosted on AWS CloudFront/S3 for fast client-side performance
* **Compute:** AWS ECS with Fargate for scalable, low-overhead container orchestration
* **Databases:** AWS RDS PostgreSQL for transactional data; DynamoDB for cart/session state; Amazon OpenSearch for keyword search
* **Caching:** Amazon ElastiCache Redis for read performance
* **Messaging:** Amazon SQS/SNS for decoupled, asynchronous event-driven workflows
* **Cloud Infrastructure:** Multi-region AWS deployment (us-east-1, eu-west-1, ap-southeast-1)

## Rationale
This architecture leverages managed AWS cloud services to guarantee 99.95% availability, sub-2-second page loads, and seamless multi-region scaling for 1M MAU. Decoupling core workflows via asynchronous messaging and specialized third-party integrations ensures strict GDPR/CCPA compliance and operational resilience.