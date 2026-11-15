## Overview
The Online Bookstore system is a scaled-down e-commerce platform for purchasing physical and electronic books with recommendations and reviews. The Shopping Cart & Checkout Container manages carts, orders, secure checkout flows, multi-currency conversion, and promotional discounts.

## Key Elements
- Customers (Guest Shoppers & Registered Customers)
- Shopping Cart & Checkout Container (AWS ECS / EKS)
- Third-Party Payment Gateway
- Shipping Provider
- Amazon ElastiCache (Redis)
- Amazon SQS / SNS with Dead-Letter Queues
- AWS KMS
- AWS WAF

## Relationships
- API Gateway Container -> Shopping Cart & Checkout Container: Routes cart and checkout requests via mTLS (AWS App Mesh)
- Shopping Cart & Checkout Container -> Third-Party Payment Gateway: Processes secure payments and tokenization via HTTPS / TLS 1.3 with idempotency keys
- Shopping Cart & Checkout Container -> Shipping Provider: Coordinates order fulfillment via HTTPS with asynchronous queue fallback
- Shopping Cart & Checkout Container -> Amazon ElastiCache (Redis): Manages guest cart state and promotion caching
- Shopping Cart & Checkout Container -> Amazon SQS / SNS: Queues asynchronous order fulfillment and confirmation events with AWS KMS encryption

## Technology Stack
- AWS ECS / EKS: Orchestrates containerized checkout services for scalability and blue/green deployments.
- Amazon ElastiCache (Redis): Provides high-performance distributed caching for guest cart state and promotional discounts.
- AWS KMS: Implements envelope encryption for messages in SQS to protect PII and payment tokens.
- AWS WAF: Provides edge-level rate limiting to mitigate cart-stuffing and DDoS attacks.
- OpenTelemetry: Enables distributed tracing across payment and checkout workflows.

## Rationale
This architecture ensures 99.95% availability, PCI-DSS compliance, and GDPR/CCPA data protection under high-traffic retail conditions. Asynchronous queuing and distributed caching maintain performance and prevent database bottlenecks during sales spikes.