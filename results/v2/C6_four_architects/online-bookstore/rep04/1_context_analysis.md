## Overview
- An Amazon-style online bookstore system providing catalog browsing, secure checkout, reviews, and recommendations for 1M MAU.
- Engineered for global deployment on AWS with multi-currency support, strict regulatory compliance, and high availability.

## Key Elements
- **Customers**: End-users browsing, purchasing, reviewing, and receiving book recommendations.
- **Store Administrators**: Manage the product catalog, moderate reviews, and oversee fulfillment.
- **Online Bookstore System**: Core platform comprising an SPA, API Gateway, microservices, and databases.
- **External SaaS Integrations**: Payment Gateway (Stripe/PayPal), Shipping Provider APIs (FedEx/UPS), Identity Provider (Auth0/Cognito), Tax Calculation Service (Avalara/TaxJar), and Notification Service (SES/Twilio).
- **Data & Infrastructure Layers**: Amazon CloudFront/S3, Amazon ECS/EKS, Amazon Aurora Multi-Region, Amazon DynamoDB, Amazon ElastiCache (Redis), and Amazon SQS/EventBridge.

## Relationships
- **Customer** -> **Online Bookstore System**: HTTPS via UI interaction and Admin Dashboard.
- **Online Bookstore System** -> **Identity Provider**: HTTPS/OIDC for authentication.
- **Online Bookstore System** -> **Payment Gateway, Tax Service, & Shipping Provider APIs**: HTTPS/REST for secure transactions, tax computation, and fulfillment.
- **Online Bookstore System** -> **Notification Service**: HTTPS/REST via Amazon SES/Twilio for alerts.
- **SPA** -> **API Gateway**: HTTPS / JSON REST secured with OIDC JWT tokens.
- **API Gateway** -> **Core Services**: gRPC for internal service-to-service communication.
- **Core Services** -> **Databases & Cache**: TCP/TLS to Amazon Aurora, DynamoDB, and ElastiCache (Redis).
- **Core Services** -> **Async Workers**: Amazon SQS/EventBridge for background task processing.

## Technology Stack
- **Frontend**: React SPA hosted on Amazon CloudFront and S3 for sub-2s page loads on 3G networks.
- **Backend**: Containerized Node.js and Go microservices orchestrated via Amazon ECS/EKS.
- **API & Comms**: AWS API Gateway for edge routing; gRPC for internal low-latency microservice communication.
- **Databases & Caching**: Amazon Aurora Multi-Region for transactional data; Amazon DynamoDB for cart/catalog storage; Amazon ElastiCache (Redis) for high-read caching.
- **Async Processing**: Amazon SQS and EventBridge paired with AWS Lambda/ECS workers to decouple background tasks.

## Rationale
- The architecture uses managed cloud services and a containerized microservices topology to easily scale to 1M MAU while maintaining a 99.95% uptime SLA.
- Offloading authentication, payments, tax calculations, and notifications to specialized external SaaS APIs ensures GDPR/CCPA compliance and multi-currency support without custom engineering overhead.