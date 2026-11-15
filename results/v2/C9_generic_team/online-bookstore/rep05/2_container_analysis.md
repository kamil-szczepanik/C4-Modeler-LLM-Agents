## Overview
- An Amazon-style multi-region online bookstore for physical and electronic books with recommendations, reviews, and secure checkout.
- Built to handle 1M MAU with 99.95% uptime while ensuring GDPR, CCPA, and OWASP compliance.

## Key Elements
- **Users:** Customers
- **Containers:** Web Application/API Gateway (with Envoy sidecar proxy), Catalog & Search Container, Checkout & Order Container, Recommendation Container, Customer & Reviews Container, Background Worker / Job Processing Container
- **External Systems:** CDN, Payment Gateway, Tax Calculation Service, Third-Party Shipping Provider, Notification Services, Identity Provider, Monitoring and Observability, Secret Management Service, Feature Flag Service, Currency Exchange Rate Service
- **Storage/Infrastructure:** Database-per-container data stores, AWS SQS/SNS, AWS ECS/EKS

## Relationships
- **Customers to Web Application/API Gateway:** HTTPS via CDN
- **Web Application/API Gateway to Core Containers:** gRPC/REST over TLS with OpenAPI contracts
- **Core Containers to External Systems:** HTTPS integrations with Payment Gateway, Tax Service, and Shipping APIs
- **Asynchronous Messaging:** AWS SQS/SNS for background tasks, notifications, and analytics

## Technology Stack
- **Compute & Orchestration:** AWS ECS/EKS across `us-east-1`, `eu-west-1`, and `ap-southeast-1` for global scalability
- **Resilience & Security:** Envoy proxy for rate limiting, circuit breaking, and OWASP Top-10 mitigation
- **Data Architecture:** Database-per-container pattern with isolated dedicated data stores
- **Messaging & Observability:** AWS SQS/SNS for event-driven flows, W3C Trace Context / AWS X-Ray for distributed tracing

## Rationale
- Microservices deployed on AWS ECS/EKS with asynchronous SQS/SNS decoupling guarantee high availability (99.95%) and scalability for 1M MAU.
- Database-per-container and strict API contracts isolate blast radiuses and ensure regulatory compliance for GDPR, CCPA, and OWASP security constraints.