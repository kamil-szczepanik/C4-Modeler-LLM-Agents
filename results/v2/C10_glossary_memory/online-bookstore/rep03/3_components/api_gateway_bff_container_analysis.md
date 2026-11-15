## Overview
An Amazon-style online bookstore platform supporting physical and electronic book purchases, reviews, recommendations, and multi-currency transactions. The architecture relies on containerized microservices deployed globally on AWS to ensure high scalability and performance.

## Key Elements
- Customer / Reviewer [person]
- Store Administrator [person]
- Single Page App / Mobile App [container] (React / React Native)
- API Gateway / BFF Container [container] (AWS API Gateway / Envoy)
  - Routing & Edge Proxy Component [component] (AWS API Gateway / Envoy)
  - Customer BFF Router Component [component] (Node.js / Express)
  - Admin BFF Router Component [component] (Node.js / Express)
  - Security & Policy Enforcement Component [component] (Envoy Lua / WAF Plugin)
- Catalog & Search Container [container] (Node.js / Go)
- Checkout & Order Container [container] (Java / Spring Boot)
- Notification & Review Container [container] (Node.js / Express)
- Admin Dashboard Container [container] (React)
- Database Containers [container] (Amazon Aurora Global PostgreSQL)
- Identity Provider [externalSystem] (AWS Cognito / Auth0)
- Payment Gateway [externalSystem]
- Shipping / Fulfillment Provider [externalSystem]
- Notification Service [externalSystem] (AWS SES / SendGrid)

## Relationships
- Customer / Reviewer -> Single Page App / Mobile App [HTTPS]
- Single Page App / Mobile App -> Routing & Edge Proxy Component [HTTPS / REST]
- Routing & Edge Proxy Component -> Security & Policy Enforcement Component [Internal gRPC]
- Security & Policy Enforcement Component -> Customer BFF Router Component [Internal HTTP/2]
- Customer BFF Router Component -> Catalog & Search Container [Internal mTLS / REST]
- Customer BFF Router Component -> Notification & Review Container [Internal mTLS / REST]
- Customer BFF Router Component -> Database Containers [Internal mTLS / SQL]
- Checkout & Order Container -> Payment Gateway [HTTPS / REST, TLS 1.3, PCI-DSS]
- Checkout & Order Container -> Shipping / Fulfillment Provider [HTTPS / REST Webhooks]
- Checkout & Order Container -> Notification & Review Container [Amazon SQS / SNS]
- Single Page App / Mobile App -> Identity Provider [JWT / JWKS via OpenID Connect]
- Notification & Review Container -> Notification Service [SMTP / API]

## Technology Stack
- **AWS API Gateway / Envoy**: Manages edge routing, TLS 1.3 termination, and zero-latency policy enforcement.
- **Node.js / Express & Go**: Powers lightweight BFF routers, catalogue search, and asynchronous notification services.
- **Java / Spring Boot**: Handles high-reliability checkout, order processing, and payment integrations.
- **React / React Native**: Delivers cross-platform web and mobile client interfaces.
- **Amazon Aurora Global PostgreSQL**: Provides cross-region transactional replication with sub-2s latency.
- **AWS ECS Fargate**: Orchestrates container auto-scaling based on CPU and request concurrency.

## Rationale
Decomposing the API Gateway into specialized BFF and security proxy components minimizes mobile chattyness and enforces strict perimeter defense. Multi-region deployment on AWS guarantees 99.95% uptime and sub-2-second page loads for global users.