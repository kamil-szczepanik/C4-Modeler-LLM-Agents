## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform designed to support 1 million monthly active users, secure multi-currency transactions, and comprehensive book catalog management. It leverages a cloud-native AWS architecture to ensure high availability, global low-latency performance, and compliance with GDPR and CCPA regulations.

## Key Elements
- Customer & Admin / Support Staff: End-users and operators interacting with the platform.
- Single Page Application (SPA): React-based frontend hosted on Amazon S3 and distributed via Amazon CloudFront.
- API Gateway: Amazon API Gateway managing ingress and JWT authentication.
- Backend Services: Catalog Service (Go/Aurora PostgreSQL), Order & Checkout Service (Spring Boot/Aurora PostgreSQL), Recommendation Service (Python FastAPI/ElastiCache Redis), and Customer & Review Service (Node.js/MongoDB).
- SPA Internal Components: Routing & Layout, Catalog & Search, Cart & Checkout, Reviews & Ratings, Recommendations, Authentication Context / API Client, and Localization & Currency Context.
- External Systems: Payment Gateway, Shipping Provider APIs, Tax Calculation Service, and Identity Provider / SSO Service.

## Relationships
- Customer & Admin -> Single Page Application: Interacts via [HTTPS / HTML / JS].
- Single Page Application -> API Gateway: Sends API requests via [HTTPS / JSON (JWT authenticated)].
- API Gateway -> Catalog, Order, Recommendation, and Customer Services: Routes traffic via internal VPC network protocols.
- Services -> External Systems: Integrates with third-party payment, shipping, and tax APIs via secure webhooks and REST endpoints.

## Technology Stack
- Frontend: React, Zustand, React Router, deployed on Amazon S3 and distributed via Amazon CloudFront for optimized 3G load times (<2s).
- Backend & Database: Go, Spring Boot, Python FastAPI, Node.js, Amazon Aurora PostgreSQL, MongoDB, and Amazon ElastiCache (Redis) for scalability and performance.
- Infrastructure & Security: AWS (us-east-1, eu-west-1, ap-southeast-1), Amazon API Gateway, Amazon SQS/SNS, strict Content Security Policies (CSP), and in-memory JWT handling for OWASP mitigation.

## Rationale
This architecture uses decoupled microservices and global CDN caching to seamlessly handle 1 million MAU with 99.95% uptime and sub-second page loads. Strict adherence to compliance standards, secure token handling, and multi-currency context fulfill all regional and business constraints.