## Overview
The Online Bookstore System is a scaled-down Amazon-style e-commerce platform enabling users to browse, search, and purchase books with integrated reviews and recommendations. It delivers a secure, multi-currency, and globally available shopping experience across web and mobile platforms.

## Key Elements
- Customer / Reviewer
- Single Page App / Mobile App (React / React Native)
- API Gateway / BFF Container (AWS API Gateway / Envoy)
- Catalog & Search Container (Node.js / Go)
- Checkout & Order Container (Java / Spring Boot)
- Notification & Review Container (Node.js / Express)
- Admin Dashboard Container (React)
- Database Containers (Amazon Aurora Global PostgreSQL)
- CDN Distribution Layer (Amazon CloudFront)
- Identity Provider (AWS Cognito / Auth0)
- Payment Gateway
- Shipping / Fulfillment Provider
- Notification Service (AWS SES / SendGrid)

## Relationships
- Customer / Reviewer -> Single Page App / Mobile App: HTTPS
- Single Page App / Mobile App -> API Gateway / BFF Container: HTTPS / REST
- Single Page App / Mobile App -> Identity Provider: JWT / JWKS via OpenID Connect
- API Gateway / BFF Container -> Catalog & Search Container: Internal mTLS / REST
- API Gateway / BFF Container -> Checkout & Order Container: Internal mTLS / REST
- Checkout & Order Container -> Payment Gateway: HTTPS / REST (TLS 1.3, PCI-DSS)
- Checkout & Order Container -> Shipping / Fulfillment Provider: HTTPS / REST Webhooks
- Checkout & Order Container -> Notification & Review Container: Amazon SQS / SNS
- Notification & Review Container -> Notification Service: SMTP / API

## Technology Stack
- Frontend: React / React Native for cross-platform web and mobile client interfaces
- Routing & State: React Router / Redux Toolkit for client-side state and localization
- Edge & CDN: Amazon CloudFront for global asset delivery across `us-east-1`, `eu-west-1`, and `ap-southeast-1`
- Gateway & Routing: AWS API Gateway / Envoy for backend-for-frontend routing
- Backend Services: Node.js / Go for catalogs, Java / Spring Boot for checkouts, Node.js / Express for notifications
- Database: Amazon Aurora Global PostgreSQL for transactional storage with cross-region replication
- Security: AWS Cognito / Auth0 for OIDC/OAuth 2.0 authentication and TLS 1.3 transport security

## Rationale
This architecture utilizes AWS cloud-native services and multi-region edge distribution via Amazon CloudFront to easily scale to 1M MAU while guaranteeing sub-2-second page loads on 3G networks. The containerized microservices and global PostgreSQL database ensure 99.95% uptime, strict GDPR/CCPA compliance, and robust OWASP Top-10 security mitigations.