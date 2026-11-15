## Overview
- An Amazon-style online bookstore designed to handle 1M MAU across three global AWS regions.
- Provides scalable catalog browsing, secure multi-currency checkout, and fulfillment.

## Key Elements
- Customers (Shoppers) and Store Administrators.
- Online Bookstore System (Cloud-hosted AWS platform).
- External Payment Gateway (Stripe/PayPal).
- External Shipping Provider (FedEx/UPS APIs).
- External Identity Provider / OAuth2 Service (Auth0/AWS Cognito).
- External Email/Notification Service (AWS SES).

## Relationships
- Customer -> Online Bookstore: Browses, searches, and checks out via HTTPS (Web/Mobile).
- Store Administrator -> Online Bookstore: Manages inventory and orders via HTTPS.
- Online Bookstore -> Payment Gateway: Authorizes payments via REST/TLS.
- Online Bookstore -> Shipping Provider: Dispatches physical orders via REST/TLS.
- Online Bookstore -> Identity Provider: Validates sessions via OIDC/OAuth2 over HTTPS.
- Online Bookstore -> Notification Service: Triggers transactional emails via REST API/TLS.

## Technology Stack
- Cloud Platform: AWS across regions `us-east-1`, `eu-west-1`, and `ap-southeast-1` for global reach.
- Routing & CDN: Route 53 DNS routing and Content Delivery Network for performance (<2s load time).
- Database: Aurora Global Databases with active-active/active-passive replication for 99.95% uptime.
- Messaging: AWS SQS/SNS for asynchronous decoupling of shipping and notification tasks.
- Security: AWS KMS for encryption at rest, WAF for OWASP Top-10 mitigation, and TLS 1.3 in transit.

## Rationale
- Decoupling core workflows via SQS/SNS ensures checkout remains available during third-party outages.
- Multi-region AWS deployment with Aurora Global Databases and CDN routing meets strict uptime, latency, and compliance constraints.