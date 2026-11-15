## Overview
An AWS-hosted online bookstore handles 1 million MAU across three global regions with high availability and GDPR/CCPA compliance. It supports physical and electronic book sales, search, secure checkout, reviews, and personalized recommendations.

## Key Elements
- **Customers**: Shoppers browsing catalogues and executing secure checkouts.
- **Book Authors / Publishers**: Stakeholders tracking sales performance and customer reviews.
- **Store Administrators**: Staff managing catalogue integrity, pricing, and moderation.
- **Online Bookstore (Software System)**: Core AWS-hosted microservices application.
- **Identity Provider**: External authentication service managing OAuth 2.0/OIDC and privacy consents.
- **Payment Gateway**: External system processing multi-currency transactions (USD, EUR, GBP).
- **Shipping Provider**: External partner managing physical order fulfillment.
- **Recommendation Engine**: External SaaS machine learning service for personalized suggestions.
- **Notification Service**: External SaaS handling transactional emails and alerts.

## Relationships
- **Customer -> Online Bookstore**: HTTPS (TLS 1.3) for browsing, cart management, and checkout.
- **Online Bookstore -> Identity Provider**: OAuth 2.0 / OIDC over HTTPS for authentication and RBAC.
- **Online Bookstore -> Payment Gateway**: REST/JSON over HTTPS with tokenized flows for payment processing.
- **Online Bookstore -> Shipping Provider**: REST/SOAP over HTTPS for fulfillment tracking.
- **Online Bookstore -> Recommendation Engine**: REST/JSON over HTTPS with pseudonymous IDs for real-time suggestions.
- **Online Bookstore -> Notification Service**: AWS SQS asynchronous queuing and REST/JSON over HTTPS for dispatching alerts.

## Technology Stack
- **Cloud Infrastructure**: AWS deployed across `us-east-1`, `eu-west-1`, and `ap-southeast-1` regions.
- **Traffic Routing**: AWS Route 53 latency-based DNS routing for multi-region failover.
- **Messaging & Decoupling**: AWS SQS for asynchronous notification dispatch.
- **Security & Secrets**: AWS Secrets Manager for automated API key rotation and TLS 1.3 for data in transit.

## Rationale
The microservices architecture deployed across multiple AWS regions ensures 99.95% uptime and low-latency performance globally. Offloading payments, authentication, recommendations, and notifications to specialized external services minimizes PCI-DSS and GDPR scope while maintaining high scalability.