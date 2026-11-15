## Overview
[An Amazon-style e-commerce platform for physical and electronic books with recommendations and reviews, designed to handle 1M MAU across three global AWS regions.]

## Key Elements
- Single Page App / Mobile App [container, React / React Native]
- API Gateway / BFF Container [container, AWS API Gateway / Envoy]
- Catalog & Search Container [container, Node.js / Go]
- Checkout & Order Container [container, Java / Spring Boot]
- Notification & Review Container [container, Node.js / Express]
- Admin Dashboard Container [container, React]
- Database Containers [container, Amazon Aurora Global PostgreSQL]
- External Systems: Payment Gateway, Shipping / Fulfillment Provider, Identity Provider, Notification Service

## Relationships
- Customer / Reviewer -> Single Page App / Mobile App (HTTPS)
- Single Page App / Mobile App -> API Gateway / BFF Container (HTTPS / REST)
- API Gateway / BFF Container -> Catalog & Search Container (Internal mTLS / REST)
- API Gateway / BFF Container -> Checkout & Order Container (Internal mTLS / REST)
- Checkout & Order Container -> Payment Gateway (HTTPS / REST, TLS 1.3, PCI-DSS)
- Checkout & Order Container -> Shipping / Fulfillment Provider (HTTPS / REST Webhooks)
- Checkout & Order Container -> Notification & Review Container (Amazon SQS / SNS)
- Online Bookstore System -> Identity Provider (JWT / JWKS via OpenID Connect)
- Online Bookstore System -> Notification Service (SMTP / API)

## Technology Stack
- **Compute:** Amazon ECS with AWS Fargate for containerized microservices without server management toil.
- **Frontend Delivery:** AWS CloudFront and S3 for low-latency static asset distribution.
- **Database:** Amazon Aurora Global PostgreSQL for transactional integrity, cross-region replication, and simplified operational overhead.
- **Messaging:** Amazon SQS / SNS for asynchronous event-driven decoupling between checkout and notifications.
- **Security & Secrets:** AWS Secrets Manager for dynamic secret injection; AWS KMS for column-level PII encryption.

## Rationale
[This microservices architecture isolates critical PCI-DSS checkout paths and scales catalog search independently to meet stringent sub-2-second performance goals. Multi-region deployment via Amazon Aurora Global PostgreSQL and AWS ECS Fargate ensures 99.95% uptime and high resilience.]