## Overview
The Online Bookstore system is an Amazon-style e-commerce platform that enables global customers to browse, purchase, and review physical and electronic books. It ensures high scalability, multi-currency support, and strict GDPR and CCPA compliance across AWS regions.

## Key Elements
- Customer / Reviewer [person]
- Store Administrator [person]
- Single Page App / Mobile App [container, React / React Native]
- API Gateway / BFF Container [container, AWS API Gateway / Envoy]
- Catalog & Search Container [container, Node.js / Go]
- Checkout & Order Container [container, Java / Spring Boot]
- Notification & Review Container [container, Node.js / Express]
- Admin Dashboard Container [container, React]
- Database Containers [container, Amazon Aurora Global PostgreSQL]
- Identity Provider [externalSystem, AWS Cognito / Auth0]
- Payment Gateway [externalSystem]
- Shipping / Fulfillment Provider [externalSystem]
- Notification Service [externalSystem, AWS SES / SendGrid]

## Relationships
- Customer / Reviewer -> Single Page App / Mobile App via HTTPS
- Single Page App / Mobile App -> API Gateway / BFF Container via HTTPS / REST
- API Gateway / BFF Container -> Catalog & Search Container via Internal mTLS / REST
- API Gateway / BFF Container -> Checkout & Order Container via Internal mTLS / REST
- Checkout & Order Container -> Notification & Review Container via Amazon SQS / SNS
- Notification & Review Container -> Notification Service via SMTP / API
- Online Bookstore System -> Database Containers via TCP / PostgreSQL

## Technology Stack
- Node.js & Express / Java Spring Boot: Powering resilient microservices backend containers.
- Amazon Aurora Global PostgreSQL: Providing scalable, multi-region transactional data storage.
- AWS API Gateway & Envoy: Managing secure ingress, routing, and rate-limiting.
- AWS Cognito / Auth0: Handling secure OIDC/OAuth 2.0 and JWT authentication flows.
- Amazon SQS / SNS: Asynchronously decoupling order, review, and notification event processing.

## Rationale
This architecture uses cloud-native AWS microservices to easily scale beyond 1 million monthly active users while preserving sub-2-second performance. Containerized separation of concerns combined with global database replication ensures strict adherence to 99.95% availability targets and multi-region data compliance.